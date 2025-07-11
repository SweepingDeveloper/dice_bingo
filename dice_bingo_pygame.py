# NO REAL MONEY NOR PRIZES ARE AWARDED.
import pygame
import sys
import os
import random

#import dice_constants
TILESPOS_X = [0,64,128,192,256,0,64,128,192,256]
TILESPOS_Y = [0,0,0,0,0,64,64,64,64,64]


EGGCRATE_TEXT = "0123456789$,."



DICEPOS_X = [0,64,128,192,256,320]
DICEPOS_Y = [0,0,0,0,0,0]
DICE_WIDTH = 64
DICE_HEIGHT = 64



amounts_won = []
nat_20_conf = []
fin_min_conf = []
fin_strikes = []
win_methods = []
board = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
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


stop_roll = 0
max_stop_roll = random.randint(100,300)




pygame.init()
size = width, height = 800,600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
dice_rolling = True
AI = False
rolled = False
bailout = False
forced_win = False


pygame.display.set_caption("Dice Bingo Bonus Round")
running = True

counter = 0
dice_value = [0,0]


db = pygame.image.load("dice_blue.png")
dg = pygame.image.load("dice_green.png")

ns = pygame.image.load("numbers.png")
ts = pygame.image.load("tiles.png")

ec = pygame.image.load("eggcrate.png")


dice_blue = pygame.transform.scale(db, (384,64))
dice_green = pygame.transform.scale(dg, (384,64))
numbers = pygame.transform.scale(ns, (320,128))
tiles = pygame.transform.scale(ts, (320,128))
eggcrate = pygame.transform.scale(ec, (768,64))


def displayEggCrate(t,x,y):
    for a in range(0,len(t),1):
        screen.blit(eggcrate, (x + (48*a), y), (64 * EGGCRATE_TEXT.index(t[a]), 0, 40,56))
            

    


while running:
    # AI Code ##################################
    #############################################

    if (AI == True):
        if (dice_rolling == True):
            conf_roll = random.randint(1,20)
            stop_roll += 1

        if (stop_roll == max_stop_roll):
            stop_roll = 0
            max_stop_roll = random.randint(100,300)
            print ("Stop Roll: Conf Roll is "+ str(conf_roll) + " vs Min Conf Roll of " + str(min_conf_roll))
            bailout = False
            rolled = True
            if (strikes == 1):
                if (conf_roll < min_conf_roll and bank > 0):
                    bailout = True
                    counter = 20
                else:
                    min_conf_roll += .5

            if (strikes == 2):
                if (conf_roll < min_conf_roll and bank > 0):
                    bailout = True
                    counter = 20
                else:
                    min_conf_roll += 3

            if (conf_roll == 20):
                bailout = False
                nat_20 += 1
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and strikes > 0:
                    bailout = True
                    counter = 20
                if event.key == pygame.K_SPACE:
                    rolled = True

        



        #event.type == pygame.KEYDOWN
            #event.key == pygame.K_q
            #event.key == pygame.K_SPACE
            
    
    if bailout == True or win_flag == 1:
        dice_rolling = False
        
    elif rolled == True and dice_rolling == True:
        dice_rolling = False
        counter = -100
        
        screen.blit(dice_blue, (448,64), (DICEPOS_X[dice_value[0]],DICEPOS_Y[dice_value[0]],DICE_WIDTH,DICE_HEIGHT))
        screen.blit(dice_green, (512,64), (DICEPOS_X[dice_value[1]],DICEPOS_Y[dice_value[1]],DICE_WIDTH,DICE_HEIGHT))

        for a in range(0,2,1):
            if (dice_value[a] == 5):
                strikes += 1
            if (strikes >= 3):
                strikes = 3
                bank = 0
                counter = 20

        if (dice_value[0] != 5 and dice_value[1] != 5 and strikes < 3):
            if (board[dice_value[0]][dice_value[1]] == 1):
                bank += 2000
            else:
                board[dice_value[0]][dice_value[1]] = 1
                if (strikes == 0):
                    bank += 5000
                elif (strikes == 1):
                    bank += 10000
                elif (strikes == 2):
                    bank += 20000


            if (forced_win == True):
                board = [[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,0]]

                h_count = 0
                v_count = 0
                d1_count = 0
                d2_count = 0
                
            for a in range(0,5,1):
                if (board[a][a] == 1):
                    d1_count += 1
                else:
                    #print ("d1 failed at ("+str(a)+", "+str(a)+")")
                    d1_count = 0

                if (board[a][4-a] == 1):
                    d2_count += 1
                else:
                    #print ("d2 failed at ("+str(a)+", "+str(4-a)+")")
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

                #print (d1_count)
                #print (d2_count)

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
                counter = 20
                # Uncomment these two lines if you wish to play the game yourself.
                # Recomment the lines to return to simulation mode.
                
                #print ("Congratulations, you\'ve won the jackpot!")
                #print ("Bank: $"+str(bank))

        rolled = False 

             
        #print (die[0])
        #print (die[1])


            

    if (counter == 0):
        dice_rolling = True
        

    if (counter == 0 and dice_rolling == True):
        dice_value[0] = random.randint(0,5)
        dice_value[1] = random.randint(0,5)

    screen.fill((0,0,0))

    #displayEggCrate(str(min_conf_roll), 600,0)
    
    for a in range(0,5,1):
        screen.blit(numbers, (0,64+(a*64)), (TILESPOS_X[a], TILESPOS_Y[a], DICE_WIDTH, DICE_HEIGHT))
        screen.blit(numbers, (64+(a*64), 0), (TILESPOS_X[a+5], TILESPOS_Y[a+5], DICE_WIDTH, DICE_HEIGHT))
                    
        for b in range(0,5,1):
            if (dice_value[0] == a and dice_value[1] == b):
                if (dice_rolling == True):
                    screen.blit(tiles, (64+(b*64), 64+(a*64)), (TILESPOS_X[board[a][b]], TILESPOS_Y[board[a][b]], DICE_WIDTH, DICE_HEIGHT))
                else:
                    if (strikes >= 3):
                        screen.blit(tiles, (64+(b*64), 64+(a*64)), (TILESPOS_X[b], TILESPOS_Y[5], DICE_WIDTH, DICE_HEIGHT))
                    else:
                        if (counter % 20 > 10):                    
                            screen.blit(tiles, (64+(b*64), 64+(a*64)), (TILESPOS_X[board[a][b]], TILESPOS_Y[board[a][b]], DICE_WIDTH, DICE_HEIGHT))
                        else:
                            screen.blit(tiles, (64+(b*64), 64+(a*64)), (TILESPOS_X[0], TILESPOS_Y[0], DICE_WIDTH, DICE_HEIGHT))
                        
            else:
                screen.blit(tiles, (64+(b*64), 64+(a*64)), (TILESPOS_X[board[a][b]], TILESPOS_Y[board[a][b]], DICE_WIDTH, DICE_HEIGHT))
                

                                
                    

    scorelen = len(str(bank)) + 2 + int(bank / 1000000)
    scorelen_index = scorelen * 48
    maximum_len = 640
    adj_distance = maximum_len - scorelen_index
    

    
    if (counter < 20 and bank > 0):
        if (bank < 1000000):
            displayEggCrate("$"+ str(int(bank/1000)) + ",000",adj_distance,456)
        else:
            if (bank - 1000000) < 10000:
                displayEggCrate("$"+ str(int(bank/1000000)) + ",00" + str(int(bank/1000-1000)) + ",000", adj_distance, 456)
            elif (bank - 1000000) < 100000:
                displayEggCrate("$"+ str(int(bank/1000000)) + ",0" + str(int(bank/1000-1000)) + ",000", adj_distance, 456)
            else:
                displayEggCrate("$"+ str(int(bank/1000000)) + "," + str(int(bank/1000-1000)) + ",000", adj_distance, 456)
                
    elif (counter >= 20 and counter % 20 > 10 and bank > 0):
        if (bank < 1000000):
            displayEggCrate("$"+ str(int(bank/1000)) + ",000",adj_distance,456)
        else:
            if (bank - 1000000) < 10000:
                displayEggCrate("$"+ str(int(bank/1000000)) + ",00" + str(int(bank/1000-1000)) + ",000", adj_distance, 456)
            elif (bank - 1000000) < 100000:
                displayEggCrate("$"+ str(int(bank/1000000)) + ",0" + str(int(bank/1000-1000)) + ",000", adj_distance, 456)
            else:
                displayEggCrate("$"+ str(int(bank/1000000)) + "," + str(int(bank/1000-1000)) + ",000", adj_distance, 456)
        
        
    
    screen.blit(dice_blue, (448,64), (DICEPOS_X[dice_value[0]],DICEPOS_Y[dice_value[0]],DICE_WIDTH,DICE_HEIGHT))
    screen.blit(dice_green, (512,64), (DICEPOS_X[dice_value[1]],DICEPOS_Y[dice_value[1]],DICE_WIDTH,DICE_HEIGHT))

    # Display Strikes.
    for a in range (0,3,1):
        if (strikes > a):
            screen.blit(dice_blue, (128 + (64*a),384), (DICEPOS_X[5],DICEPOS_Y[5], DICE_WIDTH, DICE_HEIGHT))
        else:
            screen.blit(tiles, (128 + (64*a),384), (0,0, DICE_WIDTH, DICE_HEIGHT))
            
            
    

    #pygame.draw.rect(screen, (255,255,255), (64,384,320,64))
    #pygame.draw.rect(screen, (0,0,0), (64+4,384+4,320-8,64-8))
    #screen.blit(pygame.font.Font.render(pygame.font.Font(None, 32), "Test", True, (0, 0, 0)), (76,268))

    pygame.display.flip()
    #print (counter)
    clock.tick(60)
    counter += 1
    if (counter == 10):
        counter = 0
    if (counter == 200 and bank < 1000000):
        running = False
    elif (counter == 400 and bank >= 1000000):
        running = False
    
pygame.quit()

    
