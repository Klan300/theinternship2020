def bubble_sort(lst):
    """
    sorting by swap
    """
    for i in range(len(lst)):
        swapped = False
        i = 0
        while i < len(lst)-1:
            if len(lst[i]) < len(lst[i+1]):
                lst[i],lst[i+1] = lst[i+1],lst[i]
                swapped = True
            elif len(lst[i]) == len(lst[i+1]):
                if lst[i][0] > lst[i+1][0]:
                    lst[i],lst[i+1] = lst[i+1],lst[i]
                    swapped = True
            i += 1
        if swapped == False:
            return lst


n = int(input())
name_lst = []

for i in range(n):
    minimize = ""
    word = input()
    for j in word:
        if j == j.upper() and j != " ":
            minimize += j
    name_lst.append(minimize)

name_lst = bubble_sort(name_lst)

for name in name_lst:
    print(name)
