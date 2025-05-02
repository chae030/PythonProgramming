n = int(input('maximum order of the polynomial in [2, 5] n = '))
print('==========')
print(f'n\t{n:8d}')
if n < 2 or n > 5 :
    print('Error : invalid n (2 <= n <= 5)')
else :
    list = []
    for i in range(n+1) :
        a = int(input(f'coefficient a_{i} = '))
        list.append(a)
    print('==========')
    n_coef = len(list)
    print(f'n_coef\t{n_coef:8d}')
    a_0 = list[0]
    if a_0 == 0 :
        print('Error : a_0 is zero')
    else :
        print(f'a_0\t{a_0:8d}')
        x = int(input('x = '))
        print('==========')
        print(f'coefs : {list}')
        print(f'x\t{x:8d}')
        result = 0
        for i, num in enumerate(list):
           result += num * (x ** (len(list) - i - 1))
        print(f'result\t{result:8d}')
    