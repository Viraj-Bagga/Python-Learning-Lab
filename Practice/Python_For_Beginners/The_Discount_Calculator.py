def apply_discount(price, discount_percent = 10):
    final_price = price * (1 + (discount_percent/100))

    return final_price

price1 = print(apply_discount(50, 20))
price2 = print(apply_discount(100))
