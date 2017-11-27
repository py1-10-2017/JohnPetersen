#FIND AND REPLACE
# print the first instance of the word DAY
# Create a new string where the word day is replaced with the word MONTH

words = 'It\'s thanksgiving day. It\'s my birthday too!'
print words
print words.find('day')
words = words.replace('day', ' month')
print words



#MIN AND MAX
# print the min and max values in a list

x = [2,54,-2,7,12,98]
print x
print min(x)
print max(x)



#FIRST AND LAST
# print the first and last values in a list
# create a new list containing only the first and last values in the original list
#code should work for any list

x = ["hello",2,54,-2,7,12,98,"world"]
print x
print x[0], x[len(x)- 1]

new_list = [x[0], x[len(x)-1]]
print new_list



#NEW LIST
# sort list
# spilt list in half
# push the list created from the first half to position 0 of the list created from the second list

x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x

first_list = x[:len(x)/2]
second_list = x[len(x)/2:]
print "first list", first_list
print "second_list", second_list
second_list.insert(0,first_list)
print second_list
