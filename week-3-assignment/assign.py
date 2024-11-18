def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent/100)
        result = price - discount
        return result
    else:
        return price
    
try:
    price = float(input("Enter the price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    result = calculate_discount(price, discount_percent)
    if result < price:
        print(f"The final price after applying a {discount_percent}% discount is: ${result:.2f}")
    else:
        print(f"No discount applied. The original price remains: ${price:.2f}")
except ValueError:
    print("Invalid input. Please enter a numeric value for the price and discount percentage.")
