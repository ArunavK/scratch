# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%

###################
# Marble Gambling
###################

# This script simulates a gambling game between Human and the Mighty Gganbu
# Both the players start with 10 marbles each
# One player offers a certain hidden number of marbles, while the other has to make a guess whether he
# has an even or odd number of marbles in his hand. The guesser also bets a certain number of marbles.
# If the guessers guesses correctly, he wins the bet and the offerer has to give an amount of marbles
# equal to the guess. If the guesser guessed incorrectly, he will have to give up the same amount of
# marbles.

# The roles of guesser and offerer keep alternating in each game. The game ends when either player runs
# out of marbles.
# If the Human wins, Gganbu is vanquished and the Human is known far and wide as the Hero.
# If the Mighty Gganbu wins, he consumes the Human's soul and continues to torment the lives of the
# poor villagers, until the day another brave Human challenges him...

# This game is inspired by the similar game played in Episode 06 of Squid Game.
# I am aware that Gganbu is supposed to be friendly, but man, it does sound like a monster name. I'll
# stick to this theory


# %%
import numpy as np
import matplotlib.pyplot as plt
import random as rnd


# %%
def query(funds, human=True):
    if human:
        bet = int(input("How much do you bet? : "))
        while not(bet <= funds and bet > 0):
            print("Insufficient funds!")
            bet = int(input("How much do you bet? : "))
        print("What is your guess? 0: even, 1: odd")
        guess = int(input("What is your guess? : "))
    else:
        bet = rnd.randint(1, funds)
        guess = rnd.randint(0, 1)

    return int(bet), bool(guess)


# %%
def guess_2_str(guess):
    if(guess%2):
        return 'Odd'
    else:
        return 'Even'


# %%
def show_stats(i, A, B, offer, guess, bet):
    if(i%2):
        offerer = "Gganbu"
        guesser = "Human"
    else:
        offerer = "Human"
        guesser = "Gganbu"
    
    if guess:
        guess_str = 'Odd'
    else:
        guess_str = 'Even'

    print(f'{offerer} offered {offer}; {guesser} guessed {guess_str}')
    print(f'{guesser} bet {bet}')
    print(f'Human   : {A}')
    print(f'Gganbu  : {B}')


# %%
A = 10 # Human
B = 10 # Gganbu

i = 1
print(f'Human   : {A}')
print(f'Gganbu  : {B}')
while(A > 0 and B > 0):
    print('\n------------------------------')
    print(f'Game {i}') 
    print('------------------------------')
   
    if(i%2==1):
       # A guesses and bets 
        print("Gganbu: Your turn to bet, human.")
        bet, guess = query(funds=A)
        offer = rnd.randint(1, B)

        if offer%2 == guess%2:
            # A guessed correctly
            print("Gganbu: You got lucky!")
            A += bet
            B -= bet

        else:
            # A guessed incorrectly
            print("Gganbu: Pathetic")
            A -= bet
            B += bet

        show_stats(i, A, B, offer, guess, bet)

    else:
        # B guesses and bets
        bet, guess = query(funds=B, human=False)
        print("Offer your hand, mortal")
        offer = int(input("What do you offer? : "))
        
        if offer%2 == guess%2:
            # B guessed correctly
            print("Gganbu: You are no match for me!")
            A -= bet
            B += bet
        else:
            # B guessed incorrectly
            print("Gganbu: Grr...")
            A += bet
            B -= bet
        show_stats(i, A, B, offer, guess, bet)
        
    i += 1

# %%

if(A > B):
    # Human won
    print("Gganbu: How is this possible? How could a puny mortal like you defeat the mighty Gganbu?")
else:
    # Gganbu won
    print("Gganbu: Your soul is mine! Muhuhahahahaha!")