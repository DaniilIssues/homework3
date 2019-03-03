def f(a,b):
    f1 = 1
    f2 = 1
    c = []
    i = 0
    while i <= b:
        if i == 0:
            c.append(0)
        elif i == 1:
            c.append(1)
        sum = f1 + f2
        f1 = f2
        f2 = sum
        i += 1
        c.append(f1)
    return(c[a:b-1])
fib = f(int(input("n:")),int(input("m:")))
print(fib)