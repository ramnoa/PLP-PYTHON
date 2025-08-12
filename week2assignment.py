#creating an empty list 
my_list = []
# adding elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# modifying the list
my_list.insert(1, 15)
# extending the list with multiple elements
my_list.extend([50, 60, 70])
# removing an element from the list
my_list.remove(70)
#sorting the list in ascending order
my_list.sort()
# printing the modified list
print("Modified List:", my_list)
#finding the index of an element
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)