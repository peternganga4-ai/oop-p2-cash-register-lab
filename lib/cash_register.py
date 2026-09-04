#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0):
        self.discount = discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []


    def add_item(self, item, price, quantity=1):
            self.total += price * quantity

            for _ in range(quantity):
                self.items.append(item)

                self.previous_transactions.append({
                    "item": item,
                    "price": price,
                    "quantity": quantity
                })
    def apply_discount(self):
        if self.discount == 0:
             print("There is no discount to apply.")
        else:
             self.total = self.total - (self.total * self.discount / 100)
             print(f"After the discount, the total comes to ${self.total:.0f}.")
    def void_last_transaction(self):
         if self.previous_transactions:
              last_transaction = self.previous_transactions.pop()

              price = last_transaction["price"]
              quantity = last_transaction["quantity"]

              self.total -= price * quantity

              for _ in range(quantity):
                   self.items.pop()
                   
                   
               

        
    
