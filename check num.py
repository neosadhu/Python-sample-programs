
#checks if the first number is smaller than the second

input_number= (input('Enter two numbers')).split(' ')
num1=input_number[0]
num2=input_number[1]


def CheckNums(num1,num2):


    condition=True
    if num2<num1:
        condition= True
    elif num1>num2:
        condition= False
    elif num1==num2:
        condition='-1'

    return condition

print (CheckNums(num1,num2))


