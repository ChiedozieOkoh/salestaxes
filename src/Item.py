from tokenize import Double

def round_to_multiple(num,multiple): 
    return multiple * round(float(num)/multiple)

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def shelf_price(self,tax = 10):
        tmp_tax = (self.price * tax)/100
        tax_two_dp = round(tmp_tax,2)
        final_tax = round_to_multiple(tax_two_dp,0.05)
        price =  self.price + (self.price * tax)/100
        return round(price,2)
    
    def sales_tax(self,tax = 10):
        return round(self.shelf_price(tax) - self.price,2)
    

class Imported(Item):
    def shelf_price(self ):
        return super().shelf_price() + super().sales_tax(5)
