def check_delivery_status(status):
    if status.lower() == "delivered":
        print("The order has been delivered.")
    elif status.lower() == "processing":
        print("The order is still being processed.")
    elif status.lower() == "cancelled":
        print("The order has been cancelled.")
    else:
        print("The status is unknown.")

order_status = input("Enter the status of the order: ")
check_delivery_status(order_status)

def categorize_parcel(weight):
    categories = {
        'Light': range(1, 10),
        'Medium': range(10, 50),
        'Heavy': range(50, 1000)
    }

    for category, weight_range in categories.items():
        if weight in weight_range:
            return category

    return 'Undefined'

parcel_weight = float(input("Enter the weight of the parcel: "))

category = categorize_parcel(parcel_weight)
print(f"The parcel is categorized as: {category}")