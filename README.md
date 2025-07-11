# dice_bingo
NO REAL MONEY NOR PRIZES ARE AWARDED.

Dice Bingo is a game show bonus round idea I had.  I wrote this program to figure out the cost for insuring the top prize.

This is how you play:

You are given a 5x5 grid, and two distinct dice.  One die represents the row, the other represents the column.
Each die contains the numbers 1-5, plus a Strike symbol.  

Upon rolling the dice, you get one of three outcomes:

1. You roll a combination that's not on the board (for example, if you roll a 3 for the row and 4 for the column, and that hasn't been lit up, it lights up)
2. You roll a combination that's on the board (for example, you duplicate that roll)
3. One or two of your dice lands on a Strike, meaning that you can't put it on the board

For the first outcome, $5,000 goes into your bank.
For the second outcome, $2,000 goes into your bank.
For the third outcome, you get a strike, or possibly two.

If you have no strikes, you keep rolling without making any decisions.
If you have at least one strike, you must decide to either quit the game with the money in the bank, or continue rolling.
If you have three strikes, the game is over and you win nothing.

If you decide to continue rolling with one strike, any new boxes lit up add $10,000 to your bank.
If you decide to continue rolling with two strikes, any new boxes lit up add $20,000 to your bank.
Any duplicates still add just $2,000 to your bank.

If you get five boxes in a row lit, either horizontally, vertically, or diagonally, the game is over and
win the entire bank plus $1,000,000.

What I wanted to do with this program is figure out the viability of this game for television.  That is,
does this game pay out too much money?  Too little money?  Also, how many jackpot winners are produced
for every x games played?

When I last tested the original Python game, I ran it through 10,000 simulated games and produced between 45 - 70 jackpot winners.
The average winnings over 10,000 simulated games was between $30,000 and $34,000.  Your mileage may vary.

For a more visual experience, run the dice_bingo_pygame program.  Press SPACE to stop the dice, or Q to stop the game (presuming you have at least one strike).

I hope you enjoy!

