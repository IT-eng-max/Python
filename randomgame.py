#generate a number 1~10
#import random
from random import randint


answer = randint(1, 10)

while True:
    try:
        #print(answer)
        guess = input('guess a number from 1~10:    ')
        if int(guess)>0 and int(guess)<11:
            if int(guess) == answer:
                print('You are a genious')
                break
    except ValueError:
        print('please enter a number')
        continue


