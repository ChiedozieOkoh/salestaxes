import Item

def main(): 
   book = Item.TaxFree("book",12.49)
   cd = Item.Item("music CD",14.99)
   bar = Item.TaxFree("chocolate bar",0.85)

   order = [book,cd,bar]
   Item.print_recipt(order)


if __name__ == "__main__": 
    main()