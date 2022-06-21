# Program - convert two list into a dictionary

KeyList_1 = ['Name','Designation','Company']
ValueList_2 = ['Yashaswini R Y', 'Associate HR Executive Intern', ' Datasturdy Consulting Private Limited']

# Method - 1
'''In method-1 solution, the function zip() will provide values into the dictionary comprehension. So this comprehension will return a 
key-value pair of consecutive element within the return value of the zip() function as a dictionary'''
print("Method - 1")
dict_list = {k:v for k,v in zip(KeyList_1,ValueList_2)}
print(dict_list)
print("")


# Method -2
'''In method-2 solution, the range() funstion is used to iterate over 
both lists and use comprehension to build a dictionary out of it''' 
print("Method - 2")
dict_list = {KeyList_1[i]:ValueList_2[i] for i in range(len(KeyList_1))}
print(dict_list)
print("")