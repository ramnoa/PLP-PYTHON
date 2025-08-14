#function to calculate discounted price based on a given discount percentage
def calculate_discount(price, discount_percent):
    # Check if the discount percentage is 20% or more
    if discount_percent >= 20:
         # Calculate the discount amount and return the discounted price
        return price *(1 - discount_percent / 100)
    else:
        # If discount is less than 20%, return the original price
        return price
# Example usage:
original_price = 100.0      
discount = 25.0
discounted_price = calculate_discount(original_price, discount)
print("Original Price:", original_price)
print("Discounted Price:", discounted_price)
