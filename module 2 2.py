first = 123
second = 456
third = 789
if first==second==third:
    print(3)
elif first==second!=third or first==third!=second or second==third!=first:
    print(2)
else:
    print(0)

first = 42
second = 69
third = 42
if first==second==third:
    print(3)
elif first==second==third or first==third!=second or second==third!=first:
    print(2)
else:
    print(0)