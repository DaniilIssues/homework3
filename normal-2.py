def sort_(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return(a)

list_ = [1,5,9,4,56,7,4,6,7]

sort_list = sort_(list_)

print(sort_list)
