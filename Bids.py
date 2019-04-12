from stockxsdk import Stockx

stockx = Stockx()

while True:
    item = input('What product?:')
    if item == "":
        print("Program Ended")
        break
    print()
    product_id = stockx.get_first_product_id('{}'.format(item))
    product = stockx.get_product(product_id)
    size = input("What size?:")
    print()
    bids = stockx.get_bids(product_id)
    print("{} Size {}".format(product.title, size))
    print()
    for bid in bids:
        if bid.shoe_size == "{}".format(size):
            print("Size: {} ${} {} {}(s)".format(bid.shoe_size, bid.order_price, bid.num_orders, bid.order_type))
            print('--------------------------')
    print()


