dict_1 = { "Y":1, "A":2, "S":3, "H":4, "U":5}

# user must enter the key to be checked and store it in a variable
user_value = int(input("Enter any value to check: "))

'''An "if statement" and the "in operator" is used to check,
if the key is present in the list containing the keys of the
dictionary''' 
if user_value in dict_1.values():
    # If the value is present then it prints the below statement
    print("Value of a key exists in a dictionary!!")
else:
    # If the value is not present then it prints the below statement
    print("Value of a key isn't present in a dictionary!!")
    
# Finally Exit..