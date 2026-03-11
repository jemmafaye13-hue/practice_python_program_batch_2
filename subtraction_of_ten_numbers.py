#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

result = float(input("Enter number 1: "))
for i in range(2, 11):
    num = float(input(f"Enter number {i}: "))
    result -= num
print(f"The final result is: {result}")
