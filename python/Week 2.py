#------
# Task 1
#------

a = list(range(10))
a.pop(5)
a.pop(4)
a.pop(0)
print(a)

#------
# Task 2
#------
    
a = list(range(10))
del a[0:5]
print(a)

#------
# Task 3
#------

a = int(input("set number 1: "))
b = int(input("set number 2: "))

while b == 0:
    b = int(input("Number 2 must be not equal 0, set number 2: "))

print("Sum num1 and num2 is: ", a + b)
print("Subtraction num1 and num2 is: ", a - b)
print("Multiplication num1 and num2 is: ", a * b)
print("Division num1 and num2 is: ", a / b)

#------
# Task 4
#------

a = int(input("enter the number: "))
b = input("enter any word: ")

print(a * b)
print(10*(str(a) + "Python" + b + " "))

#------
# Task 5
#------

a = list(range(10))
b = max(a)
c = min(a)
a.pop(b)
a.pop(c)
print(a)

#------
# Task 6
#------

a = ['b', 'n', 'A', 'g', 'S', 'p', 'm', 'r', 'R', 'X', 'z', 'B', 'I', 'H', 'A', 'e', 't', 'k', 'k', 'k', 'l', 'c', 'g', 'S', 'P', 'q', 'Y', 'Q']
b = sorted(a)
c = b[::-1]
print(c)

