from product_data import product_list

total_profit = 0

def purchase(name):
    for product in product_list:
        if product.name == name:
            check_payment(product)
            return 1
    print("잘못 선택하셨습니다. 다시 선택하세요.\n")
    return 2

def check_payment(product):
    global total_profit
    while True:
        if not product.is_available():
            print(f"현재 {product.name}의 재고가 0입니다.")
            break
        print(f"\n{product.name}의 금액은 {product.price}입니다.")
        payment = int(input("금액을 지불하세요 (지불할 금액 입력) : "))
        if payment == product.price:
            print("\n정상 결제 완료되었습니다.")
            print(f"{product.name}가 나왔습니다.")
            total_profit += product.price
            product.purchase()
            break
        elif payment > product.price:
            get_change(product.price, payment)
            print(f"{product.name}가 나왔습니다.")
            total_profit += product.price
            product.purchase()
            break
        else:
            print("금액이 부족합니다. 다시 결제해주세요.")

def get_change(price, payment):
    change = payment - price
    print(f"\n잔돈 {change}원이 나왔습니다.")
    change_list = [1000, 500, 100, 50]
    change_result = []
    for c in change_list:
        change_result.append(change // c)
        change %= c
    print(f"(잔돈 구성 - 1000원: {change_result[0]}장, 500원: {change_result[1]}개, 100원: {change_result[2]}개, 50원: {change_result[3]}개)")
