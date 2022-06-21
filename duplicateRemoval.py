#  remove duplicates from the list of integers and print the unique values from the list 
#  list_1 = [1,1,2,3,4,5,6,13,4,6,2,1,3,5,67,7,89,0,7,6,5,787,9,0,12]

# Method - 1
# stored the values of list using set. Since Set data type helps to eliminate the duplicate
print("METHOD - 1")
list_1 = {1,1,2,3,4,5,6,13,4,6,2,1,3,5,67,7,89,0,7,6,5,787,9,0,12}
print("list_1 =", list_1)
print("")

# Method - 2
print("METHOD - 2")
list_1 = [1,1,2,3,4,5,6,13,4,6,2,1,3,5,67,7,89,0,7,6,5,787,9,0,12]
print("Values before removal of duplicates: ", list_1)

# removing duplicate values from a list
final_list = []

for i in list_1:
    if i not in final_list:
        final_list.append(i)

# printing the unique value list
print(" The final unique value list after removal of duplicates : ", final_list)