import random

num_guess= 0

print ("What is your name")
name= input()



rand_int= random.randint(1,20)

while num_guess <6:
    print ("Enter a number")

    guess = int(input())




    if rand_int==guess:
        print ("you guessed the number")
        break
    elif rand_int>guess:
        print ("Sorry the guess is too low")
    elif rand_int<guess:
        print ("Sorry the guess is too high")
    num_guess+=1

print ()
print ('You Lose')











