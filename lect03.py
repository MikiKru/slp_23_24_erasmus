numbers = [1.23, -3.44, 3.32, -4, -5, 4.33, 4.4]

for number in numbers:
    print(number)

print(numbers)
for index, number in enumerate(numbers):
    # print(index, number)
    print(numbers[len(numbers) - 1 - index], end=" ")
print()
# Print positive values - if it's negative print 0
for number in numbers:
    if (number <= 0):
        print(0, end=" ")
    else:
        print(number, end=" ")
print()
# find number form the list
to_find = 3.32

for number in numbers:
    if(to_find != number):
        print("Not yet!")
        continue
    print("I got it!")
    break