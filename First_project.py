# Cafe Billing and order system

menu = {
    'Espresso' : 150,
    'Ristretto' : 90,
    'Latte':120,
    'Macchiato':250,
    'Mocha':450,
    'Americano':850,
    'Cold Brew':340,
    'Nitro Cold Brew':550,
    'Flat White':250,
    'Iced Coffee':399,
    'Long Black Coffee': 245,
    'Blonde': 999
}

print("Welcome to STARK CAFE's")
print("Espresso : $150\nRistretto : $90\nLatte: $120\nMacchiato: $250\nMocha: $450\nAmericano: $850\nold Brew: $340\nNitro Cold Brew: $550\nFlat White: $250\nIced Coffee: $399\nLong Black Coffee: $245\nBlonde: $999")

order_total = 0

order_1 = input("Please tell me the name of COFFEE that you want.\n")
if order_1 in menu:
    order_total +=menu[order_1]
    print(f"Your item {order_1} has been added to your order.\n")

else:
    print("Please order something from the menu\n")

another_order = input("Do you want to add another item ? (y for Yes and n for No)")
if another_order == "y":
    order_2 = input("Please tell me what you want.\n")
    if order_2 in menu:
        order_total += menu[order_2]
        print(f"Your item {order_2} has been added to your order.\n")
        
    else:
        print("Please order something from the menu\n")

print(f"The total amount of your orders is {order_total}")
  