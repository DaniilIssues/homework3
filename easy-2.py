
def f(a):
    num1 = []
    num2 = []
    for i, v in enumerate(a, 1):
        if i < 4:
            num1.append(int(v))
        else:
            num2.append(int(v))
    if sum(num1) == sum(num2):
        s = 1
    else:
        s = 0
    return(s)

ticket = f(list(input("Введите номер билета:")))

if ticket == 1:
    print("билет счастливый")
else:
    print("билет не счастливый")
