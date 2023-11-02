cost_price = int(input("Enter a cost price: "))
selling_price = int(input("Enter a sellig price: "))

# if sp is more than cp --> profit

if selling_price > cost_price :
    profit = selling_price - cost_price
    print("We have made profit of", profit)

# if sp is less than cp --> loss
elif selling_price < cost_price :
    loss = cost_price -selling_price
    print("We habe incurred loss of:", loss)

else:
    print("We have no profit and no loss")
