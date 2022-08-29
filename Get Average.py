# I use the sample to help with the code set-up
a = []
total = 0

# while statement loop use for entering numbers
while(True):
    usernum = int(input("Enter any amount of numbers"))
    if (usernum == -9999):
        break
    else:
        a.append(usernum)
# the code is set-up for the user to input the following numbers in single order: 4, -3, -15, 0, 10, 22
# first input positive numbers,  non-positive numbers, and the average of all the numbers.
# End code by inputting (-9999)
# You will get the average.

print (a)
print ("average")
for number in a:
    total = total + number

# Print the average at the end
print(total/len(a))
