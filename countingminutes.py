
'''
takes a time in the following format (2:00am-11:00pm) and finds how many minutes
in between.
'''

import re

time = '2:00am-11:00pm'

def CountingMinutes(string):
    time_list=[]

    x =re.findall(r'(\d+):(\d+)(\w+)',string) #seperate the items from the string


    #concatenate the tuples into a single list
    for items in x:
        for tuples in items:
            time_list.append(tuples)



    #Convert the number strings into int types.

    for index, items in enumerate(time_list):
        if time_list[index].isdigit():
            time_list[index] = int(time_list[index])


    #convert into military timezones
    if time_list[2]=='pm':
        time_list[0]+=12
    if time_list[5]=='pm':
        time_list[3]+=12


#Convert the time into minutes
    first_time=time_list[0]*60+time_list[1]
    second_time=time_list[3]*60+time_list[4]

    total = second_time-first_time

#check to see if the went off to the next day.
    if total != abs(total):
        total+=1440
    return (total)

print (CountingMinutes(time))










