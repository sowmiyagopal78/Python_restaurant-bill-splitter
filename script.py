print("==========================================")
print("     WELCOME TO RESTAURANT BILL SPLITTER  ")
print("==========================================")
print()

# Taking user inputs
restaurant = input("What is the restaurant name? ").strip()
cost = float(input("Enter total food cost (₹): "))

# Handles inputs like '5' or '5%' without crashing
service_charge_input = input("GST or Service charge % (e.g., 5 or 18): ").replace('%', '').strip()
service_charge = float(service_charge_input) if service_charge_input else 0.0

group_size = int(input("How many people are splitting the bill? "))

# Calculations
service_charge_total = cost * (service_charge / 100)
grand_total = cost + service_charge_total
total_per_person = grand_total / group_size

# Printable Receipt
print()
print("=" * 42)
print(f"       {restaurant.upper()} - RECEIPT BREAKDOWN")
print("=" * 42)
print(f"Food Subtotal             : ₹{cost:,.2f}")
print(f"GST / Service Charge ({service_charge:.0f}%) : ₹{service_charge_total:,.2f}")
print(f"Group Size                : {group_size} people")
print("-" * 42)
print(f"Grand Total               : ₹{grand_total:,.2f}")
print("-" * 42)
print(f"Each Person Must Pay      : ₹{total_per_person:,.2f}")
print("=" * 42)