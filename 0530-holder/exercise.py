# please work on this file
# 이 파일을 수정하여 제출하시오

class CoinHolder:
    coin = [10, 50, 100, 500]
    def __init__(self) :
        self.coin_holder = []
    def push(self, den) :
        if den not in CoinHolder.coin :
            raise ValueError("값이 잘못되었습니다!")
        else :
            self.coin_holder.append(den)
    def pop(self) :
        if not self.coin_holder :
            raise IndexError("동전통이 비어 있습니다.")
        return self.coin_holder.pop()
    def balance(self) :
        return sum(self.coin_holder)

# All executable code in this file must be inside functions or classes.
# 이 파일의 모든 실행 가능한 코드는 함수 또는 클래스 안에 있어야 합니다.
