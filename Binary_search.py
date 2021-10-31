"""
Implementing Binary search Algorithm

note that in Binary search algorithm the data structure needs to be sorted for the algorithm to 
function efficiently and correctly. if the list is not sorted the algorithm might not return the target even if it exists

"""


def binary_search(list,target):

	first = 0
	last = len(list) -1
	count = 0

	while first <= last:
		midpoint = (first+last)//2
		count = count +1

		if target == list[midpoint]:
			print("Number of guesses: ",count)
			return midpoint
			break
		elif list[midpoint] < target:
			first = midpoint+1
		else:
			last = midpoint-1
	return None
def sort_list(list):
	"""
	Sort list function

	"""

	list.sort()

	return list
def verify(index):
	"""
	this function is used to verify if target was found in the dataset or not

	"""

	if index is not None:

		msg = "Target is found at index: "+ str(index)
	else:
		
		msg ="Target not found"
	return msg


# Target list, contains all targets the user can possibly search

target_list = [ 1,2,5,5,9,10,19,20,66,78,84,90]

# Ensure list is sorted before applying binary search algorithm

sorted_list = sort_list(target_list)

print("Sorted List: ",sorted_list)


# call the search function and return the target index position if target found else return None

result = binary_search(sorted_list,2)

# pass the result to verify function to check if target is found or not


print(verify(result))
