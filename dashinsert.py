'''


'''


num = 99946554
num_string=list(str(num))
#num_string.insert(2,'-')
empty=[]




for i in range(len(num_string)-1):
    if int(num_string[i])%2!=0 and int(num_string[i+1])%2!=0:
        empty.extend([num_string[i],'-'])
    else:
        empty.append(num_string[i])

empty.append(num_string[len(num_string)-1])

print (''.join(empty))





