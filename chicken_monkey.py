nums = range(1, 101)
for num in nums:
    if num % 15 is 0:
        print('ChickenMonkey')
    elif (num % 5 == 0): 
        print('Chicken')
    elif (num % 7 == 0):
        print('Monkey')
    else:
        print(num)