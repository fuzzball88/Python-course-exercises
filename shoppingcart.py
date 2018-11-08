# -*- coding: cp1252 -*-
class Cart:
    """This class manages the shopping cart. """
    
    shoppingcart = []
    def addstuff(self):
        esine = input("What will be added?: ")
        self.shoppingcart.append(esine)

    def checkout(self):
        print("Following objects were added:")
        for i in range(0,len(self.shoppingcart)):
            print(self.shoppingcart[i], end = " ")

class SmallerCart(Cart):
    """This is a small cart with limited space"""
    size = 2
    def checkout(self):
        print("Following was added: ")
        for i in range(0,self.size):
            print(self.shoppingcart[i])
        if len(self.shoppingcart) > self.size:
            print("Some items were left out.")

def main():
    customer = SmallerCart()
    while True:
        selection = input("Add more or go to checkout?: ")
        if selection == "checkout":
            customer.checkout()
            break
        else:
            customer.addstuff()
            
if __name__ == "__main__":
    main()
