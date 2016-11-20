PT=[3, 5, 20, 2, 9, 8, 3]
lostMost=[]

for i in range(0, len(PT)-1):

    buy_price=PT[1]
    for j in range(1, len(PT)):
        sell_price=PT[j]
        if sell_price<buy_price:
            lostMost.append((buy_price-sell_price))

    PT.remove(buy_price)

print max(lostMost)
