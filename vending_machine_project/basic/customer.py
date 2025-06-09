# 소비자 모드
# 관리자 모드 import 해서 음료 리스트, 금액 리스트 불러오기

import admin

product_list = admin.product_list
price_list = admin.price_list
stock_list = admin.stock_list
total_profit = 0

def purchase(product) :
    if product in product_list :
        check_payment(product)
    else :
        print("잘못 선택하셨습니다. 다시 선택하세요.\n")
        return 2
    
    return 1


def check_payment(product) :
    global total_profit
    index = product_list.index(product)
    price = price_list[index]
    while True :
        if stock_list[index] == 0 :
            print(f"현재 {product}의 재고가 0입니다.")
            break
        print(f"\n{product}의 금액은 {price}입니다.")
        payment = int(input("금액을 지불하세요 (지불할 금액 입력) : "))
        if payment == price :
            print("\n정상 결제 완료되었습니다.")
            print(f"{product}가 나왔습니다.")
            total_profit += price
            stock_list[index] -= 1
            break
        elif payment > price :
            get_change(price, payment)
            print(f"{product}가 나왔습니다.")
            total_profit += price
            stock_list[index] -= 1
            break
        else :
            print("금액이 부족합니다. 다시 결제해주세요.")


def get_change(price, payment) :
    change = payment - price
    print(f"\n잔돈 {change}원이 나왔습니다.")
    
    change_list = [1000, 500, 100, 50]
    change_result = []
    i = 0
    for c in change_list :
        change_result.append(change // c)
        change -= c*change_result[i]
        i += 1
    print(f"(잔돈의 구성 - 1000원 : {change_result[0]}장, 500원 : {change_result[1]}개, 100원 : {change_result[2]}개, 50원 : {change_result[3]}개)")
