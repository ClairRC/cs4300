def main():
    price = input("Enter price: ")
    discount = input ("Enter discount (%): ")

    print("Calculated discount: " + str(calculate_discount(float(price), float(discount))))

# Calculates discount based on price and discount value
def calculate_discount(price, discount):

    #Check if price and discount are numberical values
    if not isinstance(price, (int, float)):
        print("Price must be a number")
    if not isinstance(discount, (int, float)):
        print("Discount must be a number")
    if discount < 0 or discount > 100:
        print("Discount must be between 0 and 100")

    return price * (1 - discount / 100)

if __name__ == "__main__":
    main()