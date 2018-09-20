'''
A function called sumOfTwo() would takes in two inputs
and will return the sum of those two numbers.

fucntion name : sumOfTwo()
input : number_1 , number_2
output : number_1 + number_2

For example,

sumOfTwo(1,2) should return 3 as a sum.
'''

def sumOfTwo(number_1,number_2):
	return number_1 + number_2

number_1 = int(input("Enter first number = "))
number_2 = int(input("Enter second number = "))
print("The Sum is",sumOfTwo(number_1,number_2))