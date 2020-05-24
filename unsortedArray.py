#search operation


''' In unsorted Array, searching can only be done in linear fashion (from first element to last element)'''


def search(arr,key):

	for i in range(len(arr)):
		if arr[i]==key:
			return i

	return -1

# Insert operation


''' Insertion in unsorted array is faster as compared to sorted array.'''


def insert(arr,key):
	arr.append(key)



# Delete operation


''' Element is searched using linear search and then delete operation followed by shifting of elements.'''

def delete(arr,key):
	if key in arr:

		arr.remove(key)
		return
	print(str(key)+"  is not in array.")


if __name__=='__main__':

	list=[10,20,30,40,50,60,70]

	index=search(list,40)

	if index !=-1:
		print("Element found at index: " + str(index))
	else:
		print("Element not Found!!")



	insert(list,80)

	print(list)


	delete(list,50)
	print(list)


	delete(list,90)
	print(list)