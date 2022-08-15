def power(base, index):
    if index == 0:
        return 1
    return base * power(base,index-1)


print(power(10,3))