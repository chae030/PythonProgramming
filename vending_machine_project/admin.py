# 관리자 모드

drink_list = ["coke", "water"]
price_list = [3200, 950]

def print_drink() :
    print("\n음료 목록", drink_list, '\n')


def check_admin() :
    print("관리자 모드에 접근하셨습니다. 비밀번호를 입력하세요.")
    while True :
        password = int(input("비밀번호 : "))
        if password == 1234 :
            print("관리자 모드를 실행합니다.\n")
            # 실행 함수로 이동
            # 관리자 모드 종료 후 다시 자판기로 -> 음료 출력하고 return 1
            # 관리자 모드 종료 후 자판기도 종료 -> return 0
            return 0
        else :
            print("비밀번호를 잘못 입력하셨습니다.")
    
    return 1
