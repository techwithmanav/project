from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "food123"

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
    "Fast Food": [0, 1, 2],
    "Snacks": [3],
    "Drinks": [4]
}


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        if email == "manav@gmail.com" and password == "manav123":
            session["login"] = True

            return redirect(url_for("customer"))

        return render_template(
            "login.html",
            error="❌ Invalid email or password!"
        )

    return render_template("login.html")


@app.route("/customer", methods=["GET", "POST"])
def customer():

    if not session.get("login"):
        return redirect(url_for("login"))

    if request.method == "POST":

        name = request.form["name"]
        phone = request.form["phone"]
        address = request.form["address"]

        if len(phone) != 10 or not phone.isdigit():
            return render_template(
                "customer.html",
                error="❌ Enter a valid 10-digit phone number!"
            )

        if address.strip() == "":
            return render_template(
                "customer.html",
                error="❌ Address cannot be empty!"
            )

        session["name"] = name
        session["phone"] = phone
        session["address"] = address

        session["cart"] = []

        return redirect(url_for("menu"))

    return render_template("customer.html")


@app.route("/menu")
def menu():

    if not session.get("login"):
        return redirect(url_for("login"))

    return render_template(
        "menu.html",
        food=food,
        prices=prices,
        stock=stock,
        categories=categories
    )


@app.route("/add/<int:index>", methods=["POST"])
def add_to_cart(index):

    if not session.get("login"):
        return redirect(url_for("login"))

    quantity = int(request.form["quantity"])

    if quantity <= 0:
        return redirect(url_for("menu"))

    if quantity > stock[index]:

        return render_template(
            "menu.html",
            food=food,
            prices=prices,
            stock=stock,
            categories=categories,
            error=f"❌ Not enough stock for {food[index]}!"
        )

    cart = session.get("cart", [])

    item = {
        "index": index,
        "quantity": quantity,
        "subtotal": prices[index] * quantity
    }

    cart.append(item)

    stock[index] -= quantity

    session["cart"] = cart

    return redirect(url_for("cart"))


@app.route("/cart")
def cart():

    if not session.get("login"):
        return redirect(url_for("login"))

    cart_items = session.get("cart", [])

    total = 0

    for item in cart_items:
        total += item["subtotal"]

    return render_template(
        "cart.html",
        cart=cart_items,
        food=food,
        prices=prices,
        total=total
    )


@app.route("/remove/<int:item>")
def remove_item(item):

    cart = session.get("cart", [])

    if item >= 0 and item < len(cart):

        food_index = cart[item]["index"]
        quantity = cart[item]["quantity"]

        stock[food_index] += quantity

        cart.pop(item)

        session["cart"] = cart

    return redirect(url_for("cart"))


@app.route("/checkout", methods=["GET", "POST"])
def checkout():

    if not session.get("login"):
        return redirect(url_for("login"))

    cart = session.get("cart", [])

    if len(cart) == 0:
        return redirect(url_for("menu"))

    total = 0

    for item in cart:
        total += item["subtotal"]

    special_offer = 0

    for item in cart:

        index = item["index"]
        quantity = item["quantity"]

        if index == 0 and quantity >= 2:
            special_offer += 30

        elif index == 1 and quantity >= 2:
            special_offer += 50

        elif index == 4 and quantity >= 3:
            special_offer += 20

    amount = total - special_offer

    if amount >= 2500:
        discount = amount * 20 / 100

    elif amount > 1000:
        discount = amount * 10 / 100

    else:
        discount = 0

    coupon = request.form.get("coupon", "").lower()

    if coupon == "food50":
        coupon_discount = 50

    elif coupon == "food100":
        coupon_discount = 100

    else:
        coupon_discount = 0

    amount = amount - discount

    if coupon_discount > amount:
        coupon_discount = amount

    amount = amount - coupon_discount

    gst = amount * 5 / 100

    if total >= 500:
        delivery = 0
    else:
        delivery = 40

    final_amount = amount + gst + delivery

    return render_template(
        "checkout.html",
        cart=cart,
        food=food,
        prices=prices,
        total=total,
        special_offer=special_offer,
        discount=discount,
        coupon_discount=coupon_discount,
        gst=gst,
        delivery=delivery,
        final_amount=final_amount
    )


@app.route("/payment", methods=["POST"])
def payment():

    if not session.get("login"):
        return redirect(url_for("login"))

    payment_method = request.form["payment"]

    session["payment"] = payment_method

    return redirect(url_for("confirmation"))


@app.route("/confirmation", methods=["GET", "POST"])
def confirmation():

    if not session.get("login"):
        return redirect(url_for("login"))

    order_id = 1001

    if request.method == "POST":
        rating = request.form["rating"]
    else:
        rating = None

    return render_template(
        "checkout.html"
        if False else "confirmation.html",
        order_id=order_id,
        customer=session.get("name"),
        phone=session.get("phone"),
        address=session.get("address"),
        payment=session.get("payment"),
        rating=rating
    )


if __name__ == "__main__":
    app.run(debug=True)