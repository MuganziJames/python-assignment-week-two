my_list = []                      # create empty list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15)             # insert 15 at second position
my_list.extend([50, 60, 70])      # add more elements
my_list.pop()                     # remove last element
my_list.sort()                    # sort in ascending order
index_of_30 = my_list.index(30)   # find index of 30
print("Index of 30:", index_of_30)
