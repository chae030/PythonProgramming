import customer
from product_data import product_list

def print_drink():
    print("\n상품 목록", [p.name for p in product_list], '\n')

def check_admin():
    print("관리자 모드에 접근하셨습니다. 비밀번호를 입력하세요.")
    while True:
        password = int(input("비밀번호 : "))
        if password == 1234:
            print("관리자 모드를 실행합니다.\n")
            admin_start()
            while True:
                restart = input("다시 자판기로 돌아가시겠습니까? (y / n) : ")
                if restart.lower() == 'y':
                    return 1
                elif restart.lower() == 'n':
                    return 0
                else:
                    print("잘못 입력하셨습니다. 다시 입력해주세요.")
        else:
            print("비밀번호를 잘못 입력하셨습니다. 다시 입력해주세요.")

def admin_start():
    while True:
        admin_menu()
        while True:
            restart = input("\n관리자 모드를 계속 실행하시겠습니까? (y / n) : ")
            if restart.lower() == 'y':
                break
            elif restart.lower() == 'n':
                return
            else:
                print("잘못 입력하셨습니다. 다시 입력해주세요.")

def admin_menu():
    while True:
        print('*' * 40)
        print("\n실행할 메뉴를 선택하세요.")
        print("1. 재고 현황  2. 재고 채우기  3. 음료 항목 추가  4. 음료 항목 삭제  5. 가격 수정  6. 품절 처리  7. 수익 조회\n")
        print('*' * 40)
        menu = input()
        if menu == '1':
            show_stock()
            return
        elif menu == '2':
            fill_stock()
            return
        elif menu == '3':
            add_product()
            return
        elif menu == '4':
            remove_product()
            return
        elif menu == '5':
            edit_price()
            return
        elif menu == '6':
            mark_soldout()
            return
        elif menu == '7':
            show_profit()
            return
        else:
            print("잘못 선택하셨습니다. 메뉴를 다시 선택해주세요.")

def show_stock():
    print("\n현재 재고 현황\n")
    if len(product_list) == 0:
        print("현재 등록된 재고가 없습니다.")
    for p in product_list:
        print(f"제품명 : {p.name} / 재고 : {p.stock}")

def fill_stock():
    while True:
        product = input("\n재고를 채울 품목을 입력하세요 : ")
        found = next((p for p in product_list if p.name == product), None)
        if not found:
            print(f"'{product}' 항목이 제품 리스트에 없습니다. 다시 입력해주세요.")
            continue
        stock = int(input("채울 수량을 입력하세요 : "))
        if stock < 0:
            print("수량을 잘못 입력하셨습니다.")
            continue
        found.stock += stock
        print(f"{found.name}의 재고는 현재 {found.stock}개 입니다.")
        return

def add_product():
    name = input("\n추가할 제품명을 입력하세요 : ")
    price = int(input(f"{name}의 가격을 입력하세요 : "))
    stock = int(input(f"{name}의 초기 수량을 입력하세요 : "))
    from product_data import Product
    product_list.append(Product(name, price, stock))
    print(f"{name} : {price}원, 수량 {stock}개로 등록되었습니다.")

def remove_product():
    while True:
        name = input("\n삭제할 제품명을 입력하세요 : ")
        found = next((p for p in product_list if p.name == name), None)
        if not found:
            print(f"{name}가 제품 목록에 없습니다. 다시 입력해주세요.")
        else:
            check = input("제품 삭제는 되돌릴 수 없습니다. 정말 삭제하시겠습니까? (y / n) : ")
            if check.lower() == 'n':
                print("삭제를 취소합니다.")
                return
            elif check.lower() == 'y':
                product_list.remove(found)
                print(f"{name} 제품 정보가 삭제되었습니다.")
                return
            else:
                print("잘못 입력하셨습니다. 다시 입력해주세요.")

def edit_price():
    while True:
        name = input("\n가격을 수정할 제품명을 입력해주세요 : ")
        found = next((p for p in product_list if p.name == name), None)
        if not found:
            print(f"{name}가 제품 목록에 없습니다. 다시 입력해주세요.")
        else:
            price = int(input(f"{name}의 현재 가격은 {found.price}입니다. 변경할 가격을 입력해주세요 : "))
            if price <= 0:
                print("가격은 0 이하로 설정할 수 없습니다.")
            else:
                found.price = price
                print(f"{name}의 가격이 {price}원으로 변경되었습니다.")
                return

def mark_soldout():
    while True:
        name = input("\n품절 처리할 제품명을 입력해주세요 : ")
        found = next((p for p in product_list if p.name == name), None)
        if not found:
            print(f"{name}가 제품 목록에 없습니다. 다시 입력해주세요.")
        else:
            found.stock = 0
            print(f"{name}의 수량이 0으로 변경, 품절 처리되었습니다.")
            return

def show_profit():
    print(f"\n총 수익 : {customer.total_profit} 원")