# 자판기 프로그램

import customer
import admin

def choice() :
    check = 1
    while check :
        drink = input("\n음료를 선택하세요 : ")
        if drink == "admin" : # 관리자 모드로 전환
            print("\n관리자 모드를 시작합니다.")
            check = admin.check_admin()
            if check == 0 :
                return 0
        else :
            check = customer.purchase(drink)
            if check == 1 :
                break

    return 1


def program() : # return 0 : 프로그램 종료
    program = choice()
    while program :
        buy_more = input("\n추가로 이용하시겠습니까? (y / n) : ")
        if (buy_more.lower() == "n") :
            print("\n이용해 주셔서 감사합니다.")
            return
        elif (buy_more.lower() == "y") :
            print("추가 구매를 실행합니다.\n")
            print('*'*40)
            admin.print_drink()
            print('*'*40, '\n')
            program = choice()
        else :
            print("y / n 중 선택해주세요.")
    return


print('*'*40)
print("\n어서오세요. 자판기 프로그램입니다.\n")
admin.print_drink()
print('*'*40)

program()
print("\n프로그램을 종료합니다.\n")
print('*'*40)
