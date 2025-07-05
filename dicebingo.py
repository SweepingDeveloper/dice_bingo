# NO REAL MONEY NOR PRIZES ARE AWARDED.
import random


amounts_won = []
nat_20_conf = []
fin_min_conf = []
fin_strikes = []
win_methods = []
board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
die = [0,0]
bank = 0
strikes = 0
win_flag = 0
bailout = 0
games = 0
nat_20 = 0
win_method = 0
jackpot_winners = 0

min_conf_roll = 2
conf_roll = 0



i = ""

print ("THIS IS JUST A SIMULATION.")
print ("NO REAL MONEY NOR PRIZES ARE AWARDED.")

# To play this game yourself, uncomment the sections as directed,
# and change 'games < 100000' to 'games < 1'.

while (games < 10000):
    board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    die = [0,0]
    bank = 0
    strikes = 0
    win_flag = 0
    bailout = 0
    win_method = 0 
    nat_20 = 0
    min_conf_roll = 0
    i = ""

    while (strikes < 3 and win_flag == 0 and bailout == 0):
        # Uncomment this section if you wish to play the game yourself.
        # To return to simluation mode, comment the first if statement,
        # and all print statements.
        
        #if (strikes == 0):
        #    print ("Bank: $"+str(bank))
        #    print ("Strikes: 0")

        #print ("")
        #print ("Press ENTER to roll.")
        #i = input("")


        # Roll dice.
        for a in range (0,2,1):
            die[a] = random.randint(1,6)
            #print (die[a])
            if (die[a] == 6):
                strikes += 1
                #print ("You got a strike.")
                if (strikes == 1):
                    min_conf_roll += ((20 - min_conf_roll) / 10)
                if (strikes == 2):
                    min_conf_roll += ((20 - min_conf_roll) / 5)
            if (strikes >= 3):
                strikes = 3
                bank = 0
                #print ("I\'m sorry, but you\'ve struck out.")
                #print ("Bank: $0")
        

        # Process good roll.
        if (die[0] != 6 and die[1] != 6):
            if (board[die[0]-1][die[1]-1] == 1):
                bank += 2000
                #print ("You rolled a duplicate.")
            else:
                board[die[0]-1][die[1]-1] = 1
                if (strikes == 0):
                    bank += 5000
                elif (strikes == 1):
                    bank += 10000
                elif (strikes == 2):
                    bank += 20000

        #########################################
        


        # Display board.  (Uncomment the following if you wish to play the game yourself.
        # Recomment all in this section to return to simulation mode.
        #for a in range(0,5,1):
            #for b in range(0,5,1):
                #if (board[a][b] == 0):
                    #print ("[ ]", end="")
                #if (board[a][b] == 1):
                    #print ("[*]", end="")
                    
            #print ("")
        #########################################



        # Check for 5 in a row.
        for a in range(0,5,1):
            h_count = 0
            v_count = 0
            d1_count = 0
            d2_count = 0
            if (board[a][a] == 1):
                d1_count += 1
            else:
                d1_count = 0

            if (board[a][4-a] == 1):
                d2_count += 1
            else:
                d2_count = 0
            
            for b in range(0,5,1):
                if (board[a][b] == 1):
                    h_count += 1
                else:
                    h_count = 0
                if (board[b][a] == 1):
                    v_count += 1
                else:
                    v_count = 0

            if (h_count == 5 or v_count == 5 or d1_count == 5 or d2_count == 5):
                win_flag = 1
                if (h_count == 5):
                    win_method = 1
                if (v_count == 5):
                    win_method = 2
                if (d1_count == 5):
                    win_method = 3
                if (d2_count == 5):
                    win_method = 4

        if (win_flag == 1):
            bank += 1000000
            jackpot_winners += 1
            # Uncomment these two lines if you wish to play the game yourself.
            # Recomment the lines to return to simulation mode.
            
            #print ("Congratulations, you\'ve won the jackpot!")
            #print ("Bank: $"+str(bank))




        # Comment this section if you wish to play the game yourself.
        # Uncomment the section to return to simulation mode.
        conf_roll = random.randint(1,20)
        
        if (strikes == 1):
            if (conf_roll < min_conf_roll and bank > 0):
                bailout = 1
            else:
                min_conf_roll += .5

        if (strikes == 2):
            if (conf_roll < min_conf_roll and bank > 0):
                bailout = 1
            else:
                min_conf_roll += 3
                


        if (conf_roll == 20):
            bailout = 0
            nat_20 += 1

        ########################################
            
            # Uncomment this section if you wish to play the game yourself.
            # Recomment this section to return to simulation mode.
            #print ("Bank: $"+str(bank))
            #print ("Strikes: "+str(strikes))
            #print ("Select an option:")
            #print ("1. Continue playing")
            #print ("2. Stop playing")
            #while (i != "1" and i != "2"): 
            #    i = input(">")
            #if (i == "2"):
            #    bailout = 1    
            #####################################

         
    amounts_won.append(bank)
    nat_20_conf.append(nat_20)
    fin_min_conf.append(min_conf_roll)
    fin_strikes.append(strikes)
    win_methods.append(win_method)
    games += 1




average_winnings = 0

# $ won: Money won in that game
# N 20s: Nat 20s rolled, meaning automatic confidence to continue playing
# Min  : Final minimum confidence roll to continue playing
# Str  : Number of strikes player had when game ended

# Uncomment this section if you wish to see statistics of each game.

#print ("")
#print ("")
#print ("$ won\t\tN 20s\tMin\tStr\tWM")
for a in range(0,len(amounts_won),1):
#    if (amounts_won[a] < 1000000):
#        print ("$"+str(amounts_won[a])+"\t\t"+str(nat_20_conf[a])+"\t"+str(int(fin_min_conf[a]))+ "\t"+str(fin_strikes[a])+ "\t"+str(win_methods[a]))
#    else:
#        print ("$"+str(amounts_won[a])+"\t"+str(nat_20_conf[a])+"\t"+str(int(fin_min_conf[a]))+ "\t"+str(fin_strikes[a])+ "\t"+str(win_methods[a]))
#######################################

    average_winnings += amounts_won[a]

average_winnings = int(average_winnings / len(amounts_won))

print ("")
print ("Number of Games: "+ str(games))
print ("Jackpot Winners: "+str(jackpot_winners))
print ("Average Winnings: $"+str(average_winnings))
        



