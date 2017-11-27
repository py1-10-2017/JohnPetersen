#COMPARE LISTS
# write a program that compares two lists and prints a message depending on if the inputs are identical or not
# program should be able to accept and compare two lists: list_one and list_two
# if identical print "The lists are the same"
# if lists are different print "The lists are not the same"



def compare_lists(list_one, list_two):
    if list_one == list_two:
        print "The lists are the same"
    else:
        print "The lists are not the same"

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

print list_one, list_two
compare_lists(list_one, list_two)


list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]

print list_one, list_two
compare_lists(list_one, list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]

print list_one, list_two
compare_lists(list_one, list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

print list_one, list_two
compare_lists(list_one, list_two)