# This is a guess the umber game.
import random # 帶入random模組
minNumber = 1
maxNumber = 20
secretNumber = random.randint(minNumber, maxNumber) # 產生1~20其中一個數字
print('I am thinking of a number between', str(minNumber), 'and', str(maxNumber))

# Ask the player to guess 6 times.
minGuesses = 1
maxGuesses = 7
for guessesTaken in range(minGuesses, maxGuesses): # 從1開始到7 有6次機會
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber: # 猜得太小
        print('Your guess is too low.')
    elif guess > secretNumber: # 猜的太大
        print('Your guess is too high.')
    else: # 猜對數字
        break # 跳出迴圈
if guess == secretNumber: # 猜的數字 等於 答案
    print('Good job! You guessed my number in', str(guessesTaken), 'guesses!')
else: # 如果都沒猜對
    print('Nope. The number I was thinking of was', str(secretNumber))
    
