# a file to perform the project of the data structures section


# TASK 1

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']        # declare an array of fruits

fruits.append('mango')              # add a mango

fruits.remove('apple')              # get rid of an element

print(fruits[::-1])                 # print the reversed fruits

# TASK 2

my_dictionary = {}

my_dictionary["age"] = 21           # set age to 21
my_dictionary["name"] = "John"      # set my name
my_dictionary["city"] = "Grinnell"  # set my college town
my_dictionary["favorite color"] = "Blue"        # set favorite color
my_dictionary["city"] = "Palo Alto" # set my hometown

# print keys and values
print("Keys are " +  str(my_dictionary.keys()))
print("values are " + str(my_dictionary.values()))


# PART 3

my_tuple = ("John", 21, "student")            # declare a tuple
print(len(my_tuple))                          # print the length of the tuple
my_tuple[1] = "22"                            # attempt to modify the tuple (not possible)
