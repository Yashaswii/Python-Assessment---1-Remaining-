dict_1 = {"y":1,"A":2,"S":3,"H":4,"U":5}
print("key before renaming in a dictionary: \n", dict_1)
print("")

new_key = "Y"
old_key = "y"

'''EXPLANATION: In order to rename the dictionary key, i've used the dictionary pop()
function which typically helps to remove the old key from the dictionary
and return its value.Later the addition of new key with the same value to the
dictionary is made'''
dict_1[new_key] = dict_1.pop(old_key)
print("key after renaming in a dictionary: \n",dict_1)
