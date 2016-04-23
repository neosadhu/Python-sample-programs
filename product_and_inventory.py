'''
product class has price, id and quantity on hand

inventory class which keeps track of various products and can
sum up the inventory value

product class:
initialize with a price and id.

methods will be able to change the price. update the quantity



'''
from collections import Counter

class Product (object):

    counter_items=0

    def __init__(self,name,price):
        self.name = name
        self.price = price
        Product.counter_items+=1
        self.product_id='id' + str(Product.counter_items)

#update price method
    def update_price(self,new_price):
        self.price=new_price

#get the name of the product
    def get_name(self):
        return self.name



    def __str__ (self):
        return ' Product: %s \n Price: %s \n Product ID:%s' %(self.name, self.price,self.product_id)



class Inventory():


    def __init__(self):
        self.product_list=[]

    def add_product(self,item):
        self.product_list.append(item)


    def get_total(self,product='default'):

        product_names=[] #a list of products inside the inventory

        for item in self.product_list:
            product_names.append(item.get_name())

        total_product=Counter(product_names)

        if product=='default':
            return total_product


        else:
            return (product_names.count(product))


#Sample adding products in the inventory.

i=Inventory()



#print a itemized list of how many products

if __name__  == '__main__' :

    run=True
    #ask for name of the product, and price:

    while run:

        print ('')

        print (' 1.Add:  \n 2.view:  \n 3.Quit:')
        print ('')
        choice = int(input('Enter Choice: '))
        print ('')

        if choice == 2:
            for items in i.product_list:
                print (items)

        elif  choice ==3:
            run=False
        elif choice ==1:
            name=  input ('Product: ')
            price= input('Price: ')
            item=Product(name,price)
            i.add_product(item)





