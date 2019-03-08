# # easy-1
#
# list_in = list(input("Введите числа:"))
# list_out = [int(i)**2 for i in list_in]
#
# print(list_out)

##easy-2
#
# list_prod1 = input("Input list1:")
# list_prod2 = input("Input list2:")
# list_prod3 = [c for c in list_prod1.split(" ") for d in list_prod2.split(" ") if d is c]
#
# print(list_prod3)

##easy-3

# list_nums = input("Введите числа:")
# list_nums_out = [int(i) for i in list_nums.split(" ") if int(i) % 3 == 0 and int(i) > 0 and int(i) % 4 != 0]
#
# print(list_nums_out)

##normal-1
# import random
#
#
# def f():
#     n = []
#     m = str()
#     while len(n) < 2500:
#         n.append(random.randint(0, 9))
#
#     for i in n:
#         m += str(i)
#     return(m)
#
# d = open('numbers.txt', "w")
# d.write(f())
# d.close()
#
# d = open('numbers.txt', "r")
# list_ = []
# n = 0
# for i in d:
#     for j in i:

# не смог(



##normal-2

# import random
# matr = []
# n = int(input("Введите число:"))
# for i in range(n):
#     row = []
#     for j in range(n):
#         row.append(random.randint(1,100))
#     row[random.randint(0,n-1)] = 0
#     matr.append(row)
#
# for row in matr:
#     for el in row:
#         print(el, end=" ")
#     print()

##hard-1
# import random
# n = int(input("Введите число:"))**3
# matr = []
# for i in range(n):
#     row = []
#     for j in range(n):
#         row.append(random.randint(0,1))
#     matr.append(row)
#
# for row in matr:
#     for el in row:
#         print(el, end=" ")
#     print()

# не смог(
#
##hard-2

# d = open("pwd.txt", "r")
# n = 0
# password = []
# for i in d:
#     for j in i.split(";"):
#         n += 1
#         if n % 2 == 0:
#             password.append(j)
#
# не смог(

##hard-3

# n = int(input("input:"))
# matr = []
# m = 0
# for i in range(n):
#     row = []
#     for j in range(n):
#         m += 1
#         row.append(m)
#     matr.append(row)
#
# for row in matr:
#     for el in row:
#         print(el, end=" ")
#     print()
# не смог(


