# ---------------- PART A ----------------
# Mutable Default Argument Bug

def add_item(item, cart=[]):
    cart.append(item)
    return cart


print("PART A OUTPUT")

print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))


# Expected Output:
# ['apple']
# ['apple', 'banana']
# ['bread', 'milk']
# ['apple', 'banana', 'eggs']


# ---------------------------------------------------
# PART B — Correct Version Using None
# ---------------------------------------------------

def add_item_fixed(item, cart=None):

    # Create a fresh list every time
    # if no cart is provided

    if cart is None:
        cart = []

    cart.append(item)

    return cart


print("\nPART B OUTPUT")

print(add_item_fixed("apple"))
print(add_item_fixed("banana"))


# Expected Output:
# ['apple']
# ['banana']


# ---------------------------------------------------
# PART C — Shopping Cart Program
# ---------------------------------------------------


# Create cart function
def create_cart(owner, discount=0):

    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


# Add items into cart
def add_to_cart(cart, name, price, qty=1):

    item = {
        "name": name,
        "price": price,
        "qty": qty
    }

    cart["items"].append(item)


# Tuple immutability demonstration
def update_price(price_tuple, new_price):

    # Tuples are immutable
    # This will raise TypeError

    price_tuple[1] = new_price


# Calculate final total
def calculate_total(cart):

    total = 0

    for item in cart["items"]:

        total += item["price"] * item["qty"]

    # Apply discount
    discount_amount = total * (cart["discount"] / 100)

    final_total = total - discount_amount

    return final_total


# ---------------- MAIN PROGRAM ----------------

# Create two separate carts
cart1 = create_cart("Alice", 10)
cart2 = create_cart("Bob", 5)


# Add items to Alice cart
add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 1000, 2)


# Add items to Bob cart
add_to_cart(cart2, "Phone", 20000, 1)
add_to_cart(cart2, "Charger", 500, 3)


# Display carts
print("\nALICE CART")
print(cart1)

print("\nBOB CART")
print(cart2)


# Display totals
print("\nAlice Total =", calculate_total(cart1))
print("Bob Total =", calculate_total(cart2))


# Tuple immutability demo
price_data = ("Laptop", 50000)

print("\nTUPLE IMMUTABILITY DEMO")

try:

    update_price(price_data, 60000)

except TypeError:

    print("TypeError: Tuples are immutable and cannot be modified.")


# ---------------------------------------------------
# DISCUSSION POINTS
# ---------------------------------------------------

# 1. Why is discount=0 safe but cart=[] dangerous?
#
# discount=0 is safe because integers are immutable.
#
# cart=[] is dangerous because lists are mutable
# and shared between function calls.


# 2. Difference between rebinding and mutating
#
# Rebinding:
# Variable points to a new object.
#
# Example:
# x = [1, 2]
# x = [3, 4]
#
# Mutating:
# Changing the existing object itself.
#
# Example:
# x.append(5)


# 3. Mutable and Immutable types
#
# Mutable:
# list, dict, set
#
# Immutable:
# tuple, str, int


# 4. If a list is passed into a function and modified,
# do changes reflect outside?
#
# Yes.
#
# Because lists are mutable and functions
# receive references to the same object.
