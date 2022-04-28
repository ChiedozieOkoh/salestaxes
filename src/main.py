import Item

def main(): 
    cd = Item.Item("blue",14.99)
    print("name:  {:s}".format(cd.name))
    print("base price:  {:0.2f}".format(cd.price))
    print("shelf price: {:0.2f}".format(cd.shelf_price()))
    print("tax amount:  {:0.2f}".format(cd.sales_tax()))

if __name__ == "__main__": 
    main()