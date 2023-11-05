from binary_search_tree import bst

def traverse(t, str_list):
	if t == None:
		str_list.append('x')
		return

	str_list.append(str(t.value))
	traverse(t.leftChild, str_list)
	traverse(t.rightChild, str_list)

def check_sequence(t1, t2):
	str1 = []
	str2 = []

	traverse(t1, str1)
	traverse(t2, str2)

	str1_string = ' '.join(str1)
	str2_string = ' '.join(str2)

	return str2_string in str1_string

t1 = bst([3,2,1,2,3,4 ,3, 2, 3,4,5,1,3,5])
t2 = bst([3,4,5,1,3,5])

print(check_sequence(t1, t2))

