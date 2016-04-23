'''
Add up all the numbers up until that number'''



def SimpleAdding (number):
    total=0

    for x in range(1,number+1):
        total=total+x

    return (total)


print (SimpleAdding(int(input())))

