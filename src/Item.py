from tokenize import Double

def round_to_multiple(num,multiple): 
    return multiple * round(float(num)/multiple)

def print_recipt(items = []):
    total_price = 0.0
    total_tax = 0.0
    for item in items: 
        print("{:s} : {:0.2f}".format(item.name,item.shelf_price()))
        total_price += item.shelf_price()
        total_tax += item.sales_tax()
    
    print("Sales Taxes: {:0.2f}".format(total_tax))
    print("Total: {:0.2f}".format(total_price))

class Item:
    def __init__(self, name, price,tax = 10):
        self.name = name
        self.price = price
        self.tax = tax

    def shelf_price(self):
        tmp_tax = (self.price * self.tax)/100
        tax_two_dp = round(tmp_tax,2)
        final_tax = round_to_multiple(tax_two_dp,0.05)
        price =  self.price + (self.price * self.tax)/100
        return round(price,2)

    def shelf_price_with_tax(self,tax):
        tmp_tax = (self.price * tax)/100
        tax_two_dp = round(tmp_tax,2)
        final_tax = round_to_multiple(tax_two_dp,0.05)
        price =  self.price + (self.price * tax)/100
        return round(price,2)

    def sales_tax(self):
        return round(self.shelf_price() - self.price,2)
    
    def sales_tax_of(self,tax):
        return round(self.shelf_price_with_tax(tax) - self.price,2)

class Imported(Item):
    def shelf_price(self ):
        return super().shelf_price() + super().sales_tax_of(5)

    def sales_tax(self):
        return self.shelf_price() - self.price


class TaxFree(Item):
    def __init__(self, name, price):
        super().__init__(name, price,0)