# 관리자 모드

import customer

product_list = []
price_list = []
stock_list = []

def print_drink() :
    print("\n상품 목록", product_list, '\n')


def check_admin() :
    print("관리자 모드에 접근하셨습니다. 비밀번호를 입력하세요.")
    while True :
        password = int(input("비밀번호 : "))
        if password == 1234 :
            print("관리자 모드를 실행합니다.\n")
            admin_start()
            while True :
                restart = input("다시 자판기로 돌아가시겠습니까? (y / n) : ")
                if restart.lower() == 'y' :
                    return 1
                elif restart.lower() == 'n' :
                    return 0
                else :
                    print("잘못 입력하셨습니다. 다시 입력해주세요.")
        else :
            print("비밀번호를 잘못 입력하셨습니다. 다시 입력해주세요.")


def admin_start() :
    while True :
        admin_menu()
        while True :
            restart = input("\n관리자 모드를 계속 실행하시겠습니까? (y / n) : ")
            if restart.lower() == 'y' :
                break
            elif restart.lower() == 'n' :
                return
            else :
                print("잘못 입력하셨습니다. 다시 입력해주세요.")


def admin_menu() :
    while True :
        print('*'*40)
        print("\n실행할 메뉴를 선택하세요.")
        print("1. 재고 현황  2. 재고 채우기  3. 음료 항목 추가  4. 음료 항목 삭제  5. 가격 수정  6. 품절 처리  7. 수익 조회\n")
        print('*'*40)
        menu = input()
        if menu == '1' :
            show_stock()
            return
        elif menu == '2' :
            fill_stock()
            return
        elif menu == '3' :
            add_product()
            return
        elif menu == '4' :
            remove_product()
            return
        elif menu == '5' :
            edit_price()
            return
        elif menu == '6' :
            mark_soldout()
            return
        elif menu == '7' :
            show_profit()
            return
        else :
            print("잘못 선택하셨습니다. 메뉴를 다시 선택해주세요.")


def show_stock() :
    print("\n현재 재고 현황\n")
    if len(product_list) == 0 :
        print("현재 등록된 재고가 없습니다.")
    for i in range(len(product_list)) :
        print(f"제품명 : {product_list[i]}, 재고 : {stock_list[i]}")


def fill_stock() :
    while True :
        product = input("\n재고를 채울 품목을 입력하세요 : ")
        if len(product_list) == 0 :
            print("현재 등록된 상품이 없습니다. 먼저 상품을 등록해주세요.")
            return
        elif product in product_list :
            stock = int(input("채울 수량을 입력하세요 : "))
            if stock < 0 :
                print("수량을 잘못 입력하셨습니다.")
                continue
            else :
                stock_list[product.index(product)] += stock
                print(f"{product}의 재고는 현재 {stock_list[product_list.index(product)]}개 입니다.")
                return
        else :
            print(f"'{product}' 항목이 제품 리스트에 없습니다. 다시 입력해주세요.")


def add_product() :
    product = input("\n추가할 제품명을 입력하세요 : ")
    price = int(input(f"{product}의 가격을 입력하세요 : "))
    stock = int(input(f"{product}의 초기 수량을 입력하세요 : "))
    product_list.append(product)
    price_list.append(price)
    stock_list.append(stock)
    print(f"{product} : {price}원, 수량 {stock}개로 등록되었습니다.")


def remove_product() :
    while True :
        product = input("\n삭제할 제품명을 입력하세요 : ")
        if len(product_list) == 0 :
            print("현재 등록된 상품이 없어 삭제할 수 없습니다.")
            return
        elif product not in product_list :
            print(f"{product}가 제품 목록에 없습니다. 다시 입력해주세요.")
        else :
            while True :
                check = input("제품 삭제는 되돌릴 수 없습니다. 정말 삭제하시겠습니까? (y / n) : ")
                if check.lower() == 'n' :
                    print("삭제를 취소합니다.") # 여기에 다음에 어디로 넘어가는지도 적어주면 좋을듯
                    return
                elif check.lower() == 'y' :
                    index = product_list.index(product)
                    product_list.pop(index)
                    price_list.pop(index)
                    stock_list.pop(index)
                    print(f"{product} 제품 정보가 삭제되었습니다.")
                    return
                else :
                    print("잘못 입력하셨습니다. 다시 입력해주세요.")
                    

def edit_price() :
    while True :
        product = input("\n가격을 수정할 제품명을 입력해주세요 : ")
        if product not in product_list :
            print(f"{product}가 제품 목록에 없습니다. 다시 입력해주세요.")
        else :
            while True : 
                price = int(input(f"{product}의 현재 가격은 {price_list[product_list.index(product)]}입니다. 변경할 가격을 입력해주세요 : "))
                if price <= 0 :
                    print("가격은 0 이하로 설정할 수 없습니다.")
                else :
                    price_list[product_list.index(product)] = price
                    print(f"{product}의 가격이 {price_list[product_list.index(product)]}원으로 변경되었습니다.")
                    return


def mark_soldout() :
    while True :
        product = input("\n품절 처리할 제품명을 입력해주세요 : ")
        if len(product_list) == 0 :
            print("현재 등록된 상품이 없어 품절 처리할 수 없습니다.")
        elif product not in product_list :
            print(f"{product}가 제품 목록에 없습니다. 다시 입력해주세요.")
        else :
            stock_list[product_list.index(product)] = 0
            print(f"{product}의 수량이 0으로 변경, 품절 처리되었습니다.")
            return


def show_profit() :
    print(f"\n총 수익 : {customer.total_profit} 원")
