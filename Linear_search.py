"""
Implementing Linear search Algorithm

note that in linear search algorithm the data structure does not need to be sorted for the algorithm to 
function efficiently.

"""



def linear_search_algo(list,target):

	""" 
	This function return the index position of the target else returnn None if target not found

	"""

	count = 0

	for i in range(0,len(list)):
		count +=1
		if target == list[i]:
			print("Number of guesses: ",count)
			return i
			break # stop and exit the loop when the target has been found

	return None # return none when the target is not found in the list

def verify(index):
	"""
	this function is used to verify if target was found in the dataset or not

	"""

	if index is not None:

		print("Target is found at index: ", index)
	else:

		print("Target not found")


# Target list, contains all targets the user can possibly search

target_list = [ 1,2,5,5,9,10,19,20,66,78,84,90]



# call the search function and return the target index position if target found else return None
# pass the result to verify function to check if target is found or not



verify(linear_search_algo(target_list, 90))