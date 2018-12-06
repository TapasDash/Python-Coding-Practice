'''
This is a simple programme which takes in input from the user as a series of numbers 
then, filter out the even and odd ones and
append them in two different lists naming them oddList and evenList

Input : 1,2,3,4,5,6
Output : oddList = [1,3,5]
		 evenList = [2,4,6] 	
'''
myList = [eval(x) for x in input("Enter series of numbers = ").split(",")]
oddList = []
evenList = []
for x in myList:
	if(x % 2 == 0):
		evenList.append(x)a
	else:
		oddList.append(x)

print("Odd List=",oddList)
print("Even List=",evenList)
