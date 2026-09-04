#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
         return self._discount

    
    @discount.setter
    def discount(self, value):
         if isinstance(value, int) and 0 <= value <= 100:
              self._discount = value
         else:
              print("Not valid discount")




    def add_item(self, item, price, quantity=1):
            # add the total cost of the items to the register total
            self.total += price * quantity
#add each item to items list based on quantity
            for _ in range(quantity):
                self.items.append(item)
#save the transaction so it can be voided later
                self.previous_transactions.append({
                    "item": item,
                    "price": price,
                    "quantity": quantity
                })
    def apply_discount(self):
        #check on discout whether it is provided
        if self.discount == 0:
             print("There is no discount to apply.")
        else:
             #calculate& subtract the discout from the total
             self.total = self.total - (self.total * self.discount / 100)
             #Display the updated total
             print(f"After the discount, the total comes to ${self.total:.0f}.")
    def void_last_transaction(self):
         # checks if there is a trasaction that can be voided
         if self.previous_transactions:
              # Get and remove the most recent transaction
              last_transaction = self.previous_transactions.pop()
#
              price = last_transaction["price"]
              quantity = last_transaction["quantity"]
#substract the transaction from the total
              self.total -= price * quantity
#remove the items from the the total
              for _ in range(quantity):
                   self.items.pop()
              else:
                   print("There is no transaction to void.")
                   

                   
               

        
    
