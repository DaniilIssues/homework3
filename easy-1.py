def f(a,b=0):
    m = int('1'+'0'*b)
    q = a*m
    c = int(q)
    i = int((q-c)*10)
    if i >= 5:
        c += 1
    return c/m

num_ = f(float(input("введите число 1:")), int(input("введите число 2:")))
print(num_)