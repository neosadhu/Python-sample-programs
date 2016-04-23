'''
takes a list of integers and checks to see if the sum of any possible
combination of the integers results in the largest integer in the list.
ex. [1,2,3,4,5] results in true (1+4=5,2+3=5), [1,2,5] results in false
'''

import itertools

def ArrayAddition(list1):

    largest_number= list1.pop(list1.index(max(list1)))
    all_comb=[]
    sum_sublist=[]

#use itertool to create all possible subslists from the list.

    for x in range(1,len(list1)):
        all_comb.append(list(itertools.combinations(list1,x)))

    print (all_comb)

#add up the sublist store the result in sum_sublist
    for a in all_comb:
        for b in a:
            sum_sublist.append((sum(b)))


    print (largest_number,'largest number')

    if (largest_number) in sum_sublist:
        return True
    else:
        return False



print (ArrayAddition([1, 2,5]))












