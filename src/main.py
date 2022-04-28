import Item

def main(): 
    perfume = Item.Item("imported perfume ",47.50)
    print("name:  {:s}".format(perfume.name))
    print("base price:  {:0.2f}".format(perfume.price))
    print("shelf price: {:0.2f}".format(perfume.shelf_price() + perfume.sales_tax(5)))
    print("tax amount:  {:0.2f}".format(perfume.sales_tax(10)))

    imp_perfume = Item.Imported("imported perfume ",47.50)
    print("name:  {:s}".format(imp_perfume.name))
    print("base price:  {:0.2f}".format(imp_perfume.price))
    print("shelf price: {:0.2f}".format(imp_perfume.shelf_price()))
    #print("tax amount:  {:0.2f}".format(perfume.sales_tax(10)))


    print("====================")
    bar = Item.Item("penguin",0.85)
    print(bar.price)
    print(bar.shelf_price())
    print(bar.sales_tax())
    print("====================")
    bar = Item.Item("penguin",0.85)
    print(bar.price)
    print(bar.shelf_price())

if __name__ == "__main__": 
    main()