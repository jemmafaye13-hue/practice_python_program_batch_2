#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

start = min(num1, num2)
end = max(num1, num2)
print(f"Numbers between {start} and {end}:")
for i in range(min(start, end) + 1, max(start, end)):
    print(i)
