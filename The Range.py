#code for part 1#

for i in range(10): #i used an range 10 to get 0-9 output#
    print()
    for j in range(10): # j range help with the horizontal set-up#
        print(j,end="  ")
    print() # positioning of the print() play a major factor in the code#



#code for part 1-b#

for i in range(10): #i used an range 10 to get 0-9 output#
    print(i,end ="  ")
    for j in range(10): # j range help with the horizontal set-up#
        print(i,end="  ") # j is switch with i for the new output#
    print() # positioning of the print() play a major factor in the code#




#code for part 2#

for i in range(10): #i used an range 10 to get 0-9 output#
    for j in range(i+1): # j range with i plus 1#
        print(abs(j),end="  ") # j is added with abs for left justified output#
    print() # positioning of the print() play a major factor in the code#
