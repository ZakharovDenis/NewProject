my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

list = 0
print(my_list)

while list < len(my_list):
    num = my_list[list]
    list = list + 1
    if num == 0:
        continue
    elif num < 0:
        print(num)
        break
    elif list == len(my_list):
        print(num)
    else:
        print(num)
