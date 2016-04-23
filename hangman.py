import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama\
mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan \
tiger toad trout turkey turtle weasel whale wolf wombat zebra'''.split()


correct_letter=''
missed_letter=''

def random_word():
    rand_word=words[random.randint(0,1+len(words))]
    return rand_word



def user_input():
    print ("Enter a letter: ")
    letter=input()
    letter.lower()
    return letter


def check_letter(guess,word):
    global correct_letter
    global missed_letter
    if guess in word:
        correct_letter+=guess
        return True
    else:
        missed_letter+=guess
        return False


def check_repeat(guess):
    all_entered=correct_letter + missed_letter
    if guess in all_entered:

        return True
    else:
        return False


def create_blanks(word):
    gameend=False
    blanks='_' * len(word)
    for i in range(len(word)):
        if word[i] in correct_letter:
            blanks = blanks[:i] + word[i] + blanks[(i+1):]
    return (blanks)






def main_game(word):
    guess=0
    print ()
    print ('HANGMAN VERSION PYTHON' + '  ' + HANGMANPICS[0])
    print ()
    print ()

    while guess<=4:
        print()

        create_blanks(word)
        print (create_blanks(word))
        print (word, 'M.S ', missed_letter)


        if word==create_blanks(word):
            print ('You Win')
            break




        else:
            letter=user_input()
            print ()


            if check_repeat(letter):
                print ('Already Entered')

            else:
                check_letter(letter,word)
                if not check_letter(letter,word):
                    guess+=1


               print ('correct', correct_letter) #test
               print ('missed', missed_letter)   #test

            if guess==5:
                print ('Out of Guess')





game = True

while game:
    main_game(random_word())

    ask=input('Again Y/N: ')
    if ask == 'Y':
        correct_letter=''
        missed_letter=''
        main_game(random_word())

    else:
        game = False
        break





