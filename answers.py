def calculate_discount(price, discount_percent):
    # Calculates the final price after applying a discount.
    # Only applies the discount if it is 20% or higher.
    # Parameters:
    # price (float): Original price of the item
    # discount_percent (float): Discount percentage
    # Returns:
    # float: Final price after discount (if applicable)

    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if final_price != price:
        print(f"Final price after {discount_percent}% discount: {final_price:.2f}")
    else:
        print(f"No discount applied. Original price: {price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
    #Output
    #Enter the original price of the item: 200
#Enter the discount percentage: 30
#Final price after 30.0% discount: 140.00