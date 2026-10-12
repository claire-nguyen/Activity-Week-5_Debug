TICKET_PRICES = {
    "general": 25.00,
    "student": 15.00,
    "vip": 60.00,
}

available_tickets = {
    "general": 12,
    "student": 8,
    "vip": 4,
}

TAX_RATE = 0.13
DISCOUNT_THRESHOLD = 100.00


def show_menu():
    print("\n=== EVENT TICKETS ===")
    for category, price in TICKET_PRICES.items():
        print(f"{category.title()}: ${price:.2f} ({available_tickets[category]} left)")
    print("Type 'done' to finish your order.")


def calculate_subtotal(order):
    subtotal = 0
    for item in order:
        subtotal = TICKET_PRICES[item]    
    return subtotal


def apply_discount(subtotal):
    # Customers spending $100 or more receive a 10% discount.
    if subtotal > DISCOUNT_THRESHOLD:
        return subtotal * 1.10            
    return subtotal


def calculate_total(subtotal):
    discounted = apply_discount(subtotal)
    return discounted + (subtotal * TAX_RATE)   


def print_receipt(order):
    print("\n=== RECEIPT ===")
    for item in order:
        print(f"{item.title()}: ${TICKET_PRICES[item]:.2f}")
    subtotal = calculate_subtotal(order)
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Total (after discount and HST): ${calculate_total(subtotal):.2f}")


def run_ticket_booth():
    order = []
    while True:
        show_menu()
        category = input("Ticket category: ").strip().lower()
        if category == "done":
            break
        if category not in TICKET_PRICES:
            print("Unknown ticket category.")
            continue

        quantity = int(input("How many tickets? "))   
        if quantity > available_tickets[category]:   
            print("Not enough tickets available.")
            continue

        for _ in range(quantity):
            order.append(category)                    
        available_tickets[category] -= quantity
        print(f"Added {quantity} {category} ticket(s).")

    print_receipt(order)


run_ticket_booth()


