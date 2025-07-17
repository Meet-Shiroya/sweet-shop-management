class Sweet:
    def __init__(self, sweet_id, name, category, price, quantity):
        self.id = sweet_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.id}: {self.name} ({self.category}) - ₹{self.price}, Qty: {self.quantity}"


class SweetShop:
    def __init__(self):
        self.sweets = []

    def add_sweet(self, sweet):
        self.sweets.append(sweet)
        print(f"✅ Sweet '{sweet.name}' added successfully!")

    def view_sweets(self):
        print("\n🍭 Available Sweets:")
        for sweet in self.sweets:
            print(sweet)

    def search_sweets(self, keyword):
        print(f"\n🔍 Search results for '{keyword}':")
        found = False
        for sweet in self.sweets:
            if keyword.lower() in sweet.name.lower() or keyword.lower() in sweet.category.lower():
                print(sweet)
                found = True
        if not found:
            print("❌ No sweets found with that keyword.")

    def purchase_sweet(self, sweet_id, quantity):
        for sweet in self.sweets:
            if sweet.id == sweet_id:
                if sweet.quantity >= quantity:
                    sweet.quantity -= quantity
                    total = sweet.price * quantity
                    print(f"🛒 Purchased {quantity} x {sweet.name} for ₹{total}")
                    return
                else:
                    print(f"❌ Only {sweet.quantity} units available. Cannot purchase {quantity}.")
                    return
        print(f"❌ Sweet with ID {sweet_id} not found.")

    def restock_sweet(self, sweet_id, quantity):
        for sweet in self.sweets:
            if sweet.id == sweet_id:
                sweet.quantity += quantity
                print(f"🔄 Restocked {quantity} units of '{sweet.name}'. Total now: {sweet.quantity}")
                return
        print(f"❌ Sweet with ID {sweet_id} not found.")


# Demo
if __name__ == "__main__":
    shop = SweetShop()
    sweet1 = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    sweet2 = Sweet(1002, "Gulab Jamun", "Milk-Based", 30, 50)
    sweet3 = Sweet(1003, "Gajar Halwa", "Vegetable-Based", 40, 25)

    shop.add_sweet(sweet1)
    shop.add_sweet(sweet2)
    shop.add_sweet(sweet3)

    shop.view_sweets()

    # Purchase some sweets
    shop.purchase_sweet(1001, 5)

    # Restock sweets
    shop.restock_sweet(1001, 10)
    shop.restock_sweet(9999, 5)  # Invalid ID

    shop.view_sweets()
