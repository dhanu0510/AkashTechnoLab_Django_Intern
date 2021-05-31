def add(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print("Sum is",sum)

add(10)
add(10,20,30,40)