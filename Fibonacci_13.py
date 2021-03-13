def gen_fib():
    i = 1
    count = int(input('Input Fib Count --- '))
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1,1]
    elif count > 2:
        fib = [1,1]
        while i < count - 1:
            fib.append(fib[i] + fib[i-1])
            i +=1
        return fib

y = gen_fib()
print(y)
