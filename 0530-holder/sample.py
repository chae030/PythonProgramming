# begin sample.py
# This file is to show how we can use the functions defined in exercise.py
# 이 파일은 exercise.py에 정의된 함수를 어떻게 사용할 수 있는지 보여주기 위한 것입니다.
# This file is not to be evaluated.
# 이 파일은 평가되지 않습니다.

import random


# Import the module containing the functions
# 학생이 작성한 exercise.py 모듈을 import
import exercise

# Set the random seed
# (유사) 난수 발생기를 초기화
random.seed()


def main():
    # Create a CoinHolder instance
    holder = exercise.CoinHolder()

    # List of valid coin values
    valid_coins = (10, 50, 100, 500)

    # Push 5 random valid coins
    print("Pushing 5 random coins:")
    for _ in range(5):
        coin = random.choice(valid_coins)
        holder.push(coin)
        print(f"Pushed coin: {coin}")

    # Print current balance
    print(f"\nCurrent balance: {holder.balance()}")

    # Pop one coin and display it
    popped_coin = holder.pop()
    print(f"Popped coin: {popped_coin}")

    # Print final balance
    print(f"Final balance: {holder.balance()}")


if __name__ == "__main__":
    # Lines below are executed only when this file is run directly
    # 이 파일이 직접 실행될 때만 아래의 코드가 실행됩니다.
    # When this file is imported, the lines below are not executed.
    # 이 파일이 import될 때는 아래의 코드가 실행되지 않습니다.
    main()

# end sample.py
