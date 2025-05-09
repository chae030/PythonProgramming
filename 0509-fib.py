def sum_odd_fibonacci_below(a, b, n) :
    # n 미만의 홀수 피보나치 수열의 합을 반환
    fib = fibonacci_below(a, b, n)
    result = 0
    for f in fib :
        if (f < n) and is_add(f) :
            result += f
    return result

def next_fibonacci(a, b) :
    # 두 항으로부터 다음 피보나치 수열의 값을 반환
    return (a + b)
    
def is_add(n) :
    # n이 홀수이면 True, 아니면 False 를 반환
    if n % 2 == 0 :
        return False
    else : 
        return True
    
def fibonacci_below(a, b, n) :
    # a와 b로 시작하여 n미만의 모든 피보나치 수열의 합을 반환
    fib = [a, b]
    next = 0
    while True :
        next = next_fibonacci(a, b)
        if not(next < n) :
            break
        fib.append(next)
        a = b
        b = next
    return fib

def main():
    """
    Main function to run example cases.
    예제 케이스를 실행하는 메인 함수입니다.
    """

    print("Calculating sum of odd Fibonacci numbers below n, starting from a and b.")
    print("a와 b로 시작하는 n 미만의 홀수 피보나치 수의 합을 계산합니다.")
    print("-" * 60)

    # --- Example 1: Standard-like start (1, 2), small n ---
    # --- 예제 1: 표준과 유사한 시작 (1, 2), 작은 n ---
    a1, b1, n1 = 1, 2, 10
    # Sequence: 1, 2, 3, 5, 8, ...
    # Odd terms < 10: 1, 3, 5
    # Expected Sum: 1 + 3 + 5 = 9
    result1 = sum_odd_fibonacci_below(a1, b1, n1)
    print(f"Sum of odd Fibonacci numbers starting {a1}, {b1} below {n1}:")
    print(f"계산 결과 ({a1}, {b1} 시작, {n1} 미만 홀수 항 합): {result1}")
    print(f"(Expected/예상값: 9)")
    print("-" * 60)

    # --- Example 2: Standard-like start (1, 2), larger n ---
    # --- 예제 2: 표준과 유사한 시작 (1, 2), 큰 n ---
    a2, b2, n2 = 1, 2, 90
    # Sequence: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    # Odd terms < 90: 1, 3, 5, 13, 21, 55, 89
    # Expected Sum: 1 + 3 + 5 + 13 + 21 + 55 + 89 = 187
    result2 = sum_odd_fibonacci_below(a2, b2, n2)
    print(f"Sum of odd Fibonacci numbers starting {a2}, {b2} below {n2}:")
    print(f"계산 결과 ({a2}, {b2} 시작, {n2} 미만 홀수 항 합): {result2}")
    print(f"(Expected/예상값: 187)")
    print("-" * 60)

    # --- Example 3: Different start (0, 1), small n ---
    # --- 예제 3: 다른 시작 (0, 1), 작은 n ---
    a3, b3, n3 = 0, 1, 10
    # Sequence: 0, 1, 1, 2, 3, 5, 8, ...
    # Odd terms < 10: 1, 1, 3, 5
    # Expected Sum: 1 + 1 + 3 + 5 = 10
    result3 = sum_odd_fibonacci_below(a3, b3, n3)
    print(f"Sum of odd Fibonacci numbers starting {a3}, {b3} below {n3}:")
    print(f"계산 결과 ({a3}, {b3} 시작, {n3} 미만 홀수 항 합): {result3}")
    print(f"(Expected/예상값: 10)")
    print("-" * 60)

    # --- Example 4: Different start (0, 1), larger n ---
    # --- 예제 4: 다른 시작 (0, 1), 큰 n ---
    a4, b4, n4 = 0, 1, 90
    # Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    # Odd terms < 90: 1, 1, 3, 5, 13, 21, 55, 89
    # Expected Sum: 1 + 1 + 3 + 5 + 13 + 21 + 55 + 89 = 188
    result4 = sum_odd_fibonacci_below(a4, b4, n4)
    print(f"Sum of odd Fibonacci numbers starting {a4}, {b4} below {n4}:")
    print(f"계산 결과 ({a4}, {b4} 시작, {n4} 미만 홀수 항 합): {result4}")
    print(f"(Expected/예상값: 188)")
    print("-" * 60)

    # --- Example 5: Edge case - n is very small ---
    # --- 예제 5: 경계 조건 - n이 매우 작음 ---
    a5, b5, n5 = 1, 2, 1
    # Odd terms < 1: None
    # Expected Sum: 0
    result5 = sum_odd_fibonacci_below(a5, b5, n5)
    print(f"Sum of odd Fibonacci numbers starting {a5}, {b5} below {n5}:")
    print(f"계산 결과 ({a5}, {b5} 시작, {n5} 미만 홀수 항 합): {result5}")
    print(f"(Expected/예상값: 0)")
    print("-" * 60)

    a6, b6, n6 = 1, 2, 2
    # Odd terms < 2: 1
    # Expected Sum: 1
    result6 = sum_odd_fibonacci_below(a6, b6, n6)
    print(f"Sum of odd Fibonacci numbers starting {a6}, {b6} below {n6}:")
    print(f"계산 결과 ({a6}, {b6} 시작, {n6} 미만 홀수 항 합): {result6}")
    print(f"(Expected/예상값: 1)")
    print("-" * 60)


if __name__ == "__main__":
    # Lines below are executed only when this file is run directly
    # 이 파일이 직접 실행될 때만 아래의 코드가 실행됩니다.
    # When this file is imported, the lines below are not executed.
    # 이 파일이 import될 때는 아래의 코드가 실행되지 않습니다.
    main()

# end sample.py
