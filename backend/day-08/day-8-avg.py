my_list = [5, 9, 2, 3, 1]

def avg(numlist):
    sum = 0

    for num in numlist:
        sum += num

    return sum / len(numlist)

print(avg(my_list))