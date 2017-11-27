#TYPE LIST
# Write a program that takes a list and prints a message for each element in the list based on that elements data type
# For each item in the list, test its data type
# STRINGS concatenate it into a new string
# NUMBER add it to a running sum
# At the end of the program print the string, then number and what the list contains. If it contains only one type, print that type or otherwise print MIXED


mixed_list = ['magical unicorns',19,'hello',98.98,'world']
integer_list = [2,3,1,7,4,12]
string_list = ['magical','unicorns']

def identify_list_type(list):
    new_string = ''
    total = 0

    for value in list:
        if isinstance(value, int) or isinstance(value, float):
            total += value
        elif isinstance(value, str):
            new_string += value

    if new_string and total:
        print "The array you entered is of mixed type"
        print "String:", new_string
        print "Total:", total

    elif new_string:
        print "The array you entered is a string type"
        print "String:",new_string

    else:
        print "The array you entered is a number type"
        print "Total:", total

print identify_list_type(mixed_list)
print identify_list_type(integer_list)
print identify_list_type(string_list)