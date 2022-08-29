import random
# Finally I got the random to work per boot of program.

numAttempts = 0
number = 20

Name = input("What is your name?")
print("Hello",Name)

number = random.randint(1, 20)
print('Well, ' + Name + ', I am thinking of a number between 1 and 20.')


while numAttempts < 3:
     print('Take a guess.') 
     guess = input()
     guess = int(guess)


# I use the if, and break for the attempts it was simple to me.     
     numAttempts = numAttempts + 1

#The indented statements
     if guess < number:
         print('Your guess is too low.') 

     if guess > number:
         print('Your guess is too high.')

     if guess == number:
         break


# I use + sign for the number of guesses
if guess == number:
    numAttempts = str(numAttempts) #str the for numberAttempts
    print('Good job, ' + Name + '! You guessed my number in ' + numAttempts + ' guesses!')

# guess != is not equal to number
if guess != number:
     number = str(number)#str the for number
     print('Your three guesses are over, the number I was thinking of was'  + number)
