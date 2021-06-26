
# ordinal numbers indicate their position in a list...
# ...such as '1st' or '3rd'
numbers = [0,1,2,3,4,5,6,7,8,9]
for n in numbers:
    if n == 0:
        print(f'{n}\n')
    elif n == 1:
        print(f'{n}st\n')
    elif n == 2:
        print(f'{n}nd\n')
    elif n == 3:
        print(f'{n}rd\n')
    else:
        print(f'{n}th\n')