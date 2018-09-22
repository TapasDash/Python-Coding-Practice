'''
This is the FizzBuzz Problem programme:-
	--> First off, it will print out the numbers ranging from 1 to 100
	-->Those numbers which are multiple of 3, will get replaced by string "Fizz"
	-->Those numbers which are multiple of 5, will get replaced by string "Buzz"
	-->Those numbers which are multiple of both 3 and 5, will get replaced by string "FizzBuzz"
	-->Remaing numbers will get print out on the console as it is,
'''
for num in range(1,101):	
	if (num % 3 == 0 and num % 5 == 0):
		print("FizzBuzz")
	elif (num % 3 == 0):
		print("Fizz")
	elif (num % 5 == 0):
		print("Buzz")
	else:
		print(num)
