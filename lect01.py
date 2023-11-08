# CTRL + / - comment
# CTRL + D - duplication line
# ALT + Enter - auto-tip
import math
from math import pi

name = "Michal"
gender = 'M'

name = "Michael"
# new_name - snake case
new_name = name
salary_net = 1123.45

print("Name:", name, sep=";", end="/")
print("Name:", name)
print("Name:", name)
# delete object from memory
# del(name)
# print(name)
print(type(name))
print(type(salary_net))
print(salary_net * 2)
print(str(salary_net) * 2)

print(float(str(math.pi)[0:4]))
print(round(math.pi, 2))

print("I'm Michael. My favaourite quote is : \"To be or not to be!\"")
print("http:\\\\myservice.com\\xyz")
print("http://myservice.com/xyz")

name1 = "11"
# 1name = "11" - forbidden
if(name1 is None):
    print("IS")
else:
    print("IS NOT")


print(3 > 5)
# A-65 vs J-74
print("Alan" > "Aloe")
print((len("Alan") > len("Joe")) and False)


# height = int(input("What is your height in cm?"))
# print(height,"cm", "it's", height/100,"m" )
num1 = 3
num2 = 2
result = num1//num2
print(result)
print(num1/num2)
