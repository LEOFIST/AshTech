# Edit Check by Carlton F Ashley Jr.
# I use an Boolean Functions to help with the code
def RPSGame():
    def RPS():
        
# made a input to make game run better
        player1=input('R, P or S?')
        player2=input('R, P or S?')

# code is long, I use the old fashioned way. I used your methods and repeat the values.        

        if player1==player2:
            return 0
        if (player1==('R'or'r')and player2==('S'or's'))or(player1==('S'or's')and player2==('P'or'p'))or(player1==('P'or'p')and player2==('R'or'r')):
            return 1
        if (player2==('R'or'r')and player1==('S'or's'))or(player2==('S'or's')and player1==('P'or'p'))or(player2==('P'or'p')and player1==('R'or'r')):
            return 2

    result=RPS()
    return result

# this is the scoring setup command I use samples from other programs for the system

numWinsP1=0
numWinsP2=0

# i use part of the if, else code from the part 1 assignment
for i in range(5): # play repeatedly say 5 times
    result=RPSGame()
    if result==0:
        print("Nobody Wins") # code set for no winner
    elif result==1:
        numWinsP1=numWinsP1+1
        print('Player 1 wins.')# player1 winner
    else:
        numWinsP2=numWinsP2+1
        print('Player 2 wins.')# player2 winner
    print("Scores:  Player 1:",numWinsP1,"   Player 2:",numWinsP2)

print('Thanks For Playing')
