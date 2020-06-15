numbers=[3,8,7,5,3,4,15,14,12,10]
max = numbers[0]
for number in numbers:
    if number > max:
        max=number
print("THE LARGEST NUMBER IN THE LIST:",max)