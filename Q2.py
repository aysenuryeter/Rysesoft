#Ayşenur YETER
#aysenuryeter@gmail.com

#Python

import random

def verify(guess,random,guessNumber):
    print("Gizli Sayı -> ",random)
    print("Denenen Sayı -> ",guess)

    if guess > random:
        print("Eşleşmiyor. Kalan Hakkınız -> ", guessNumber)
        out = 1
    elif guess < random:
        print("Eşleşmiyor. Kalan Hakkınız -> ", guessNumber)
        out = -1
    else:
        print("KAZANDINIZZZ")
        out = 0
        exit()
    print("Dönen değer ->", out , "\n")
    if (guessNumber == 0):
        print("HAK BİTTİ!")


rand= random.randint(1,1000000)

guessNumber = 500;

while guessNumber != -1:
    guess = random.randint(1, 1000000)
    output = verify(guess, rand,guessNumber)
    guessNumber = guessNumber - 1
