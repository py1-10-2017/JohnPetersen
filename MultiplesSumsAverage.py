#MULTIPLES, SUM, AVERAGE

#MULTIPLES
# write code that prints all the odd numbers from 1 to 1000
# use the FOR loop and do use a list to do this exercise

for count in range (1, 1001, 2):
  print count

# create another program that prints all the multiples of 5 from 5 to 1 million

for count in range (5, 1000001, 5):
  print count



#SUM LIST
# create a program that prints the sum of all the values a list

a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
  sum += i
print sum



#AVERAGE LIST
# create a program that prints the average of the values in a list

a = [1, 2, 5, 10, 255, 3]
print sum/len(a)