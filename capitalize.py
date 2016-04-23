'''
Capitalizes the first letter of each word of a user inputted string
 '''


def letter_capitalize(string):



    string=string.split()
    cap_string=[]
    for words in string:
        (cap_string.append(words[0].upper()+words[1:len(words)]))


    return(' '.join(cap_string))

print(letter_capitalize(input()))












