from stockxsdk import Stockx

stockx = Stockx()

while True:
    try:
        item = input('What product?:')
        if item == "":
            print("Program Ended")
            break
        print()
        product_id = stockx.get_first_product_id('{}'.format(item))

        product = stockx.get_product(product_id)

        size = input("What size?:")
        print()
        asks = stockx.get_asks(product_id)
        print("{} Size {}".format(product.title, size))
        print()
        for ask in asks:
            if ask.shoe_size == "{}".format(size):
                print("Size: {} ${} {} ask(s)".format(ask.shoe_size, ask.order_price, ask.num_orders))
                print('--------------------------')
        print()
    except:
        print('No Results for {}'.format(item.title()))
        print()
