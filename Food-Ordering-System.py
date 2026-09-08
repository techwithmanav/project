db = ["manav@gmail.com", "manav123"]

while True:
    email = input("📧 Enter your email: ")

    if email in db:
        break
    else:
        print("❌ Enter valid email!")


while True:
    password = input("🔐 Enter your password: ")

    if password == db[1]:
        print("✅ Login successful!")
        break
    else:
        print("❌ Enter valid password!")


customer = input("\n👤 Enter your name: ")

while True:
    phone = input("📞 Enter your phone number: ")

    if len(phone) == 10 and phone.isdigit():
        break
    else:
        print("❌ Enter a valid 10-digit phone number!")


while True:
    address = input("🏠 Enter your delivery address: ")

    if address.strip() != "":
        break
    else:
        print("❌ Address cannot be empty!")


print(f"\n👋 Welcome, {customer}!")
print("🍽️ Please select items from the menu")


food = [
    "🍔 Burger",
    "🍕 Pizza",
    "🥪 Sandwich",
    "🍟 French Fries",
    "🥤 Cold Drink"
]

prices = [120, 250, 100, 80, 50]
stock = [10, 5, 8, 15, 20]


categories = {
    1: "🍔 Fast Food",
    2: "🍟 Snacks",
    3: "🥤 Drinks"
}


category_items = {
    1: [0, 1, 2],
    2: [3],
    3: [4]
}


order_id = 1001


def select_category():
    while True:
        print("\n===== 📂 FOOD CATEGORIES =====")
        print("1. 🍔 Fast Food")
        print("2. 🍟 Snacks")
        print("3. 🥤 Drinks")

        choice = input("📂 Select category: ")

        if choice.isdigit():
            choice = int(choice)

            if choice in categories:
                return choice

        print("❌ Invalid category! Please try again.")


def display_menu(category):
    print(f"\n===== {categories[category]} MENU =====")

    for i in range(len(category_items[category])):
        food_index = category_items[category][i]

        print(
            f"{i + 1}. {food[food_index]} - ₹{prices[food_index]} "
            f"| 📦 Stock: {stock[food_index]}"
        )


def select_food(category):
    while True:
        choice = input(
            "\n🍕 Enter food number: "
        )

        if choice.isdigit():
            choice = int(choice)

            if (
                choice >= 1
                and choice <= len(category_items[category])
            ):
                food_index = category_items[category][choice - 1]

                print(
                    f"✅ Selected food: "
                    f"{food[food_index]}"
                )

                return food_index

        print("❌ Invalid food number! Please try again.")


def enter_quantity():
    while True:
        quantity = input(
            "🔢 Enter quantity: "
        )

        if quantity.isdigit():
            quantity = int(quantity)

            if quantity > 0:
                return quantity

        print("❌ Quantity must be greater than 0!")


def available_quantity(food_index):
    return stock[food_index]


def calculate_price(food_index, quantity):
    total_price = prices[food_index] * quantity
    return total_price


def food_order():
    total = 0

    order_items = []
    order_quantities = []
    order_prices = []

    while True:
        category = select_category()

        display_menu(category)

        food_index = select_food(category)

        quantity = enter_quantity()

        if quantity > available_quantity(food_index):
            print(
                f"❌ Not enough stock for "
                f"{food[food_index]}!"
            )

            print(
                f"📦 Available stock: "
                f"{available_quantity(food_index)}"
            )

            print("🔄 Please select another quantity!")
            continue

        price = calculate_price(
            food_index,
            quantity
        )

        total = total + price

        stock[food_index] = (
            stock[food_index] - quantity
        )

        order_items.append(food_index)
        order_quantities.append(quantity)
        order_prices.append(price)

        print("\n===== 🛒 ORDER DETAILS =====")
        print(f"🍽️ Item: {food[food_index]}")
        print(f"💵 Price: ₹{prices[food_index]}")
        print(f"🔢 Quantity: {quantity}")
        print(f"🧾 Subtotal: ₹{price}")
        print(f"💰 Current Total: ₹{total}")

        while True:
            more = input(
                "\n🔄 Do you want to order anything more? "
                "(yes/no): "
            ).lower()

            if more == "yes":
                break

            elif more == "no":
                return (
                    total,
                    order_items,
                    order_quantities,
                    order_prices
                )

            else:
                print("❌ Please enter yes or no!")


def display_cancel_items(
    order_items,
    order_quantities,
    order_prices
):
    for i in range(len(order_items)):
        print(
            f"{i + 1}. "
            f"{food[order_items[i]]} x "
            f"{order_quantities[i]} = "
            f"₹{order_prices[i]}"
        )


def remove_cancelled_item(
    choice,
    total,
    order_items,
    order_quantities,
    order_prices
):
    index = choice - 1
    item = order_items[index]
    stock[item] += order_quantities[index]
    total -= order_prices[index]

    print(f"❌ Removed {food[item]}")
    order_items.pop(index)
    order_quantities.pop(index)
    order_prices.pop(index)
    print(f"💰 Current Total: ₹{total}")
    return total


def cancel_items(
    total,
    order_items,
    order_quantities,
    order_prices
):
    while True:
        print("\n===== ❌ CANCEL ITEM =====")

        if len(order_items) == 0:
            print("❌ No items in your order!")
            return total

        display_cancel_items(
            order_items,
            order_quantities,
            order_prices
        )

        print("0. ✅ Finish")

        choice = input(
            "❌ Enter item number to remove: "
        )

        if choice.isdigit():
            choice = int(choice)

            if choice == 0:
                return total

            if 1 <= choice <= len(order_items):
                total = remove_cancelled_item(
                    choice,
                    total,
                    order_items,
                    order_quantities,
                    order_prices
                )
            else:
                print("❌ Invalid item number!")

        else:
            print("❌ Enter a valid number!")


def display_cart(
    order_items,
    order_quantities,
    order_prices,
    total
):
    print("\n========== 🛒 YOUR CART ==========")

    for i in range(len(order_items)):
        print(f"\n{i + 1}. {food[order_items[i]]}")
        print(f"   💵 Price: ₹{prices[order_items[i]]}")
        print(f"   🔢 Quantity: {order_quantities[i]}")
        print(f"   🧾 Subtotal: ₹{order_prices[i]}")
        print("----------------------------")

    print(f"💰 Cart Total: ₹{total}")


def special_offers(
    order_items,
    order_quantities
):
    offer_discount = 0

    for i in range(len(order_items)):
        food_index = order_items[i]
        quantity = order_quantities[i]

        if food_index == 0 and quantity >= 2:
            offer_discount += 30
            print(
                "🎉 Burger Offer: ₹30 discount!"
            )

        elif food_index == 1 and quantity >= 2:
            offer_discount += 50
            print(
                "🎉 Pizza Offer: ₹50 discount!"
            )

        elif food_index == 4 and quantity >= 3:
            offer_discount += 20
            print(
                "🎉 Cold Drink Offer: ₹20 discount!"
            )

    if offer_discount == 0:
        print("\nℹ️ No special offer applied.")

    else:
        print(
            f"🎁 Total Special Offer Discount: "
            f"₹{offer_discount}"
        )

    return offer_discount


def calculate_discount(total):
    if total >= 2500:
        discount = total * 20 / 100

    elif total > 1000:
        discount = total * 10 / 100

    else:
        discount = 0

    return discount


def delivery_charge(total):
    if total >= 500:
        return 0
    else:
        return 40


def apply_coupon():
    while True:
        coupon = input(
            "\n🎟️ Enter coupon code "
            "(food50 / food100 / no): "
        ).lower()

        if coupon == "food50":
            print("🎉 ₹50 coupon applied!")
            return 50

        elif coupon == "food100":
            print("🎉 ₹100 coupon applied!")
            return 100

        elif coupon == "no":
            print("❌ No coupon applied.")
            return 0

        else:
            print("❌ Invalid coupon code!")


def payment_method():
    while True:
        print("\n===== 💳 PAYMENT METHOD =====")
        print("1. 💵 Cash")
        print("2. 📱 UPI")
        print("3. 💳 Card")

        choice = input(
            "💳 Select payment method: "
        )

        if choice == "1":
            return "Cash"

        elif choice == "2":
            return "UPI"

        elif choice == "3":
            return "Card"

        else:
            print(
                "❌ Invalid choice! "
                "Please select 1, 2 or 3."
            )


def calculate_bill(
    total,
    special_offer_discount,
    coupon_discount
):
    amount_after_offer = (
        total - special_offer_discount
    )

    discount = calculate_discount(
        amount_after_offer
    )

    amount_after_discount = (
        amount_after_offer - discount
    )

    if coupon_discount > amount_after_discount:
        coupon_used = amount_after_discount
    else:
        coupon_used = coupon_discount

    amount_after_coupon = (
        amount_after_discount - coupon_used
    )

    gst = amount_after_coupon * 5 / 100

    delivery = delivery_charge(total)

    final_amount = (
        amount_after_coupon
        + gst
        + delivery
    )

    return (
        discount,
        coupon_used,
        gst,
        delivery,
        final_amount
    )


def rating():
    while True:
        rating_value = input(
            "\n⭐ Rate our service from 1 to 5: "
        )

        if rating_value.isdigit():
            rating_value = int(rating_value)

            if rating_value >= 1 and rating_value <= 5:
                break

        print(
            "❌ Rating must be between 1 and 5!"
        )

    if rating_value == 5:
        print("😍 Excellent! Thank you!")

    elif rating_value >= 3:
        print("😊 Thank you for your feedback!")

    else:
        print("🙏 We will improve our service!")


while True:

    total, order_items, order_quantities, order_prices = food_order()

    while True:
        cancel = input(
            "\n❌ Do you want to remove any item? "
            "(yes/no): "
        ).lower()

        if cancel == "yes":

            total = cancel_items(
                total,
                order_items,
                order_quantities,
                order_prices
            )

            if total == 0:
                print("\n⚠️ Your order is empty!")
                print("🍽️ Please order at least one item.")
                break
            else:
                break

        elif cancel == "no":
            break

        else:
            print("❌ Please enter yes or no!")

    if total > 0:
        break


display_cart(
    order_items,
    order_quantities,
    order_prices,
    total
)


special_offer_discount = special_offers(
    order_items,
    order_quantities
)


coupon_discount = apply_coupon()


discount, coupon_used, gst, delivery, final_amount = calculate_bill(
    total,
    special_offer_discount,
    coupon_discount
)


payment = payment_method()


print("\n========== 🧾 ORDER SUMMARY ==========")

print(f"🆔 Order ID: ORD{order_id}")

for i in range(len(order_items)):
    print(
        f"\n{i + 1}. {food[order_items[i]]}"
    )

    print(
        f"   💵 Price: ₹{prices[order_items[i]]}"
    )

    print(
        f"   🔢 Quantity: "
        f"{order_quantities[i]}"
    )

    print(
        f"   🧾 Subtotal: "
        f"₹{order_prices[i]}"
    )


print("\n========== 💵 FINAL BILL ==========")

print(f"🆔 Order ID: ORD{order_id}")
print(f"👤 Customer Name: {customer}")
print(f"📞 Phone Number: {phone}")
print(f"🏠 Delivery Address: {address}")

print(f"\n💰 Food Total: ₹{total:.2f}")

print(
    f"🎉 Special Offer Discount: "
    f"₹{special_offer_discount:.2f}"
)

print(
    f"🎁 Discount: "
    f"₹{discount:.2f}"
)

print(
    f"🎟️ Coupon Discount: "
    f"₹{coupon_used:.2f}"
)

print(
    f"🧾 GST (5%): "
    f"₹{gst:.2f}"
)

print(
    f"🚚 Delivery Charge: "
    f"₹{delivery:.2f}"
)

print(
    f"💳 Payment Method: "
    f"{payment}"
)

print(
    f"💵 Final Amount: "
    f"₹{final_amount:.2f}"
)


print("\n========== 📦 ORDER STATUS ==========")

print("✅ Order Status: Confirmed")
print("👨‍🍳 Kitchen Status: Preparing")
print("🚚 Delivery Status: Order will be delivered soon")
print("⏱️ Estimated Delivery Time: 30-40 minutes")


print("\n📧 Confirmation email will be sent shortly.")

rating()

print("\n🙏 Thank you for ordering!")
print("🎉 Have a great day! 😊")