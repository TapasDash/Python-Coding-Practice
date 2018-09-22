'''
This is the Programme in which user will input some values which would be stored as a list
in myList variable
Then, using sorted() function which would take in the above list will sort the elements out 
 '''
print("""Please input your element using comma
	for eg:- 1,2,3,4,5
	""")
myList = [eval(x) for x in input("Enter any sequence=").split(",")]
reverse = input("Do you want to sort the list in reverse order(yes / no) = ")
if( reverse == "yes"):
	reversedSortedList = sorted(myList, reverse = True)
	print('Your reversed sorted List',reversedSortedList)
else:
	sortedList = sorted(myList)
	print('Your  sorted List',sortedList)
