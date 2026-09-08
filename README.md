
# 🍔 Food Ordering System

<div align="center">

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Level-Beginner-2EA44F?style=for-the-badge" />
<img src="https://img.shields.io/badge/Project-Mini%20Project-FF8C00?style=for-the-badge" />
<img src="https://img.shields.io/badge/Platform-Console-24292F?style=for-the-badge" />

<br><br>

🍔 &nbsp; 🍕 &nbsp; 🥪 &nbsp; 🍟 &nbsp; 🥤

<h2>🐍 A Beginner-Friendly Python Console Application</h2>

<p>
  <b>Login • Menu • Stock • Cart • Offers • Coupons • Payment • Rating</b>
</p>

<br>

<a href="#-features">
  <img src="https://img.shields.io/badge/✨%20Explore%20Features-ff6b35?style=for-the-badge" />
</a>

&nbsp;

<a href="#-installation--setup">
  <img src="https://img.shields.io/badge/▶️%20Run%20Project-2ea44f?style=for-the-badge" />
</a>

<br><br>

<a href="https://github.com/techwithmanav/Food-Ordering-System">
  <img src="https://img.shields.io/badge/View%20on-GitHub-181717?style=for-the-badge&logo=github" />
</a>

</div>

---

> 🍽️ **A practical Python mini project that combines basic programming concepts to simulate a real-world food ordering system.**

---

## 📑 Table of Contents

- [🌟 Overview](#-overview)
- [📊 Project Snapshot](#-project-snapshot)
- [✨ Features](#-features)
- [🍕 Menu](#-menu)
- [🎉 Special Offers](#-special-offers)
- [🎟️ Coupon System](#️-coupon-system)
- [🛒 Cart](#-cart)
- [📦 Stock Management](#-stock-management)
- [🧾 Billing](#-billing)
- [💳 Payment](#-payment)
- [📦 Order Status](#-order-status)
- [⭐ Rating](#-rating)
- [🔄 Application Flow](#-application-flow)
- [🧩 Functions](#-functions)
- [🛠️ Technologies & Concepts](#️-technologies--concepts)
- [📂 Project Structure](#-project-structure)
- [🚀 Installation & Setup](#-installation--setup)
- [🖥️ Terminal Preview](#️-terminal-preview)
- [📚 Learning Outcomes](#-learning-outcomes)
- [💡 Why This Project](#-why-this-project)
- [🚀 Future Roadmap](#-future-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 🌟 Overview

The **Food Ordering System** is a Python-based console application that simulates a simple food ordering experience.

Customers can:

- 🔐 Login
- 👤 Enter personal details
- 📂 Browse food categories
- 🍔 Select food
- 🔢 Enter quantity
- 📦 Check stock
- 🛒 Manage the cart
- ❌ Cancel items
- 🎉 Use special offers
- 🎟️ Apply coupons
- 🎁 Get discounts
- 🧾 Calculate GST
- 🚚 Calculate delivery charges
- 💳 Select payment
- 📦 View order status
- ⭐ Rate the service

The project is intentionally designed using **beginner-level Python concepts up to functions**.

---

## 📊 Project Snapshot

<div align="center">

| 🐍 Python | 🎯 Level | 🛒 Cart | 📦 Stock | 💳 Payment |
|:---:|:---:|:---:|:---:|:---:|
| 3.x | Beginner | ✅ | ✅ | ✅ |

| 🔐 Login | 🎉 Offers | 🎟️ Coupons | 🧾 GST | ⭐ Rating |
|:---:|:---:|:---:|:---:|:---:|
| ✅ | ✅ | ✅ | ✅ | ✅ |

</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 **Login System** | Valid email and password required |
| 👤 **Customer Details** | Name, phone number and delivery address |
| 📞 **Phone Validation** | Requires a valid 10-digit number |
| 🏠 **Address Validation** | Prevents empty addresses |
| 📂 **Food Categories** | Fast Food, Snacks and Drinks |
| 🍔 **Food Menu** | Displays food, price and stock |
| 🔢 **Quantity Validation** | Accepts positive quantities |
| 📦 **Stock Management** | Prevents ordering unavailable quantities |
| 🔄 **Multiple Orders** | Allows customers to order additional items |
| 🧾 **Subtotal** | Calculates price × quantity |
| 🛒 **Shopping Cart** | Displays the complete order before billing |
| ❌ **Cancellation** | Removes items and restores stock |
| 🎉 **Special Offers** | Item-based discounts |
| 🎟️ **Coupons** | Supports `food50` and `food100` |
| 🎁 **Discount System** | 10% / 20% based on amount |
| 🧾 **GST** | Calculates 5% GST |
| 🚚 **Delivery Charge** | Free above ₹500 |
| 💳 **Payment** | Cash, UPI and Card |
| 🆔 **Order ID** | Displays the order ID |
| 📦 **Order Status** | Displays confirmation and delivery status |
| ⭐ **Rating** | Rating from 1–5 |
| 📧 **Confirmation** | Displays order confirmation |

---

# 🍕 Menu

## 🍔 Fast Food

| No. | Food Item | Price | Stock |
|---:|---|---:|---:|
| 1 | 🍔 Burger | ₹120 | 10 |
| 2 | 🍕 Pizza | ₹250 | 5 |
| 3 | 🥪 Sandwich | ₹100 | 8 |

## 🍟 Snacks

| No. | Food Item | Price | Stock |
|---:|---|---:|---:|
| 1 | 🍟 French Fries | ₹80 | 15 |

## 🥤 Drinks

| No. | Food Item | Price | Stock |
|---:|---|---:|---:|
| 1 | 🥤 Cold Drink | ₹50 | 20 |

---

# 🎉 Special Offers

| Food Item | Requirement | Discount |
|---|---:|---:|
| 🍔 Burger | 2 or more | ₹30 OFF |
| 🍕 Pizza | 2 or more | ₹50 OFF |
| 🥤 Cold Drink | 3 or more | ₹20 OFF |

```text
🍔 Burger × 2

🎉 Burger Offer: ₹30 discount!
````

---

# 🎟️ Coupon System

| Coupon Code |  Discount |
| ----------- | --------: |
| `food50`    |   ₹50 OFF |
| `food100`   |  ₹100 OFF |
| `no`        | No coupon |

```text
🎟️ Enter coupon code: food50
🎉 ₹50 coupon applied!
```

---

# 🛒 Cart

Before billing and payment, the complete cart is displayed.

```text
╭──────────────────────────────────────╮
│           🛒 YOUR CART               │
├──────────────────────────────────────┤
│ 🍔 Burger                            │
│ 💵 Price    : ₹120                   │
│ 🔢 Quantity : 2                      │
│ 🧾 Subtotal : ₹240                   │
│                                      │
│ 🍕 Pizza                             │
│ 💵 Price    : ₹250                   │
│ 🔢 Quantity : 1                      │
│ 🧾 Subtotal : ₹250                   │
│                                      │
│ 💰 Cart Total : ₹490                 │
╰──────────────────────────────────────╯
```

---

# ❌ Order Cancellation

Customers can remove an item before completing the bill.

```text
===== ❌ CANCEL ITEM =====

1. 🍔 Burger × 2 = ₹240
2. 🍕 Pizza × 1 = ₹250
3. 🥤 Cold Drink × 3 = ₹150

0. ✅ Finish
```

When an item is removed:

* 💰 Its amount is removed from the total.
* 📦 Its quantity is returned to stock.

---

# 📦 Stock Management

The system checks available stock before accepting an order.

```text
🍕 Pizza
📦 Available Stock: 5

🔢 Enter quantity: 8

❌ Not enough stock for 🍕 Pizza!
📦 Available stock: 5
🔄 Please select another quantity!
```

---

# 🧾 Billing

The billing sequence is:

```text
💰 Food Total
      ↓
🎉 Special Offer
      ↓
🎁 Regular Discount
      ↓
🎟️ Coupon
      ↓
🧾 GST 5%
      ↓
🚚 Delivery Charge
      ↓
💵 Final Amount
```

### 🎁 Discount Rules

|      Food Total |    Discount |
| --------------: | ----------: |
|   ₹2500 or more |         20% |
| More than ₹1000 |         10% |
|   ₹1000 or less | No discount |

### 🚚 Delivery Charges

```text
₹500 or more → 🚚 FREE
Below ₹500   → 🚚 ₹40
```

---

# 💳 Payment

```text
╭──────────────────────────────╮
│      💳 PAYMENT METHOD       │
├──────────────────────────────┤
│ 1. 💵 Cash                  │
│ 2. 📱 UPI                   │
│ 3. 💳 Card                  │
╰──────────────────────────────╯
```

Invalid choices are rejected until a valid option is selected.

---

# 🆔 Order ID

The current program displays:

```text
🆔 Order ID: ORD1001
```

> 📌 The current implementation uses `1001` as the order ID.

---

# 📦 Order Status

```text
╭──────────────────────────────────────╮
│          📦 ORDER STATUS             │
├──────────────────────────────────────┤
│ ✅ Order Status: Confirmed           │
│ 👨‍🍳 Kitchen Status: Preparing        │
│ 📦 Order Status: Packed              │
│ 🚚 Delivery: Order will be delivered│
│ ⏱️ Estimated Time: 30–40 minutes     │
╰──────────────────────────────────────╯
```

---

# ⭐ Rating

Customers can rate the service from **1 to 5**.

```text
⭐ Rate our service from 1 to 5: 5

😍 Excellent! Thank you!
```

---

# 🔄 Application Flow

```text
🚀 START
   │
   ▼
🔐 LOGIN
   │
   ▼
👤 CUSTOMER DETAILS
   │
   ▼
📂 SELECT CATEGORY
   │
   ▼
🍔 DISPLAY MENU
   │
   ▼
🍕 SELECT FOOD
   │
   ▼
🔢 ENTER QUANTITY
   │
   ▼
📦 CHECK STOCK
   │
   ▼
🧾 CALCULATE SUBTOTAL
   │
   ▼
🔄 ORDER MORE?
   ├──────────────► YES ──► 🍔 MENU AGAIN
   │
   ▼ NO
🛒 VIEW CART
   │
   ▼
❌ REMOVE ITEM
   │
   ▼
🎉 SPECIAL OFFER
   │
   ▼
🎟️ COUPON
   │
   ▼
🎁 DISCOUNT
   │
   ▼
🧾 GST
   │
   ▼
🚚 DELIVERY
   │
   ▼
💳 PAYMENT
   │
   ▼
📦 ORDER STATUS
   │
   ▼
⭐ RATING
   │
   ▼
✅ END
```

---

# 🧩 Functions

```text
select_category()
display_menu()
select_food()
enter_quantity()
available_quantity()
calculate_price()
food_order()
cancel_items()
display_cart()
special_offers()
calculate_discount()
delivery_charge()
apply_coupon()
payment_method()
calculate_bill()
rating()
```

Each function handles a specific task, keeping the program organized and easy to understand.

---

# 🛠️ Technologies & Concepts

### 🐍 Technology

* Python 3.x
* VS Code / PyCharm / IDLE
* Console / Terminal

### 📚 Python Concepts

* Variables
* Strings
* Integers
* Lists
* Dictionaries
* Input / Output
* `if`, `elif`, `else`
* `while` loop
* `for` loop
* Functions
* Parameters
* `return`
* `isdigit()`
* `strip()`
* Basic arithmetic

> 📌 No external Python libraries are required.

---

# 📂 Project Structure

```text
Food-Ordering-System/
│
├── 📄 Food-Ordering-System.py
├── 📄 README.md
└── 📄 LICENSE
```

---

# 🚀 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/techwithmanav/Food-Ordering-System.git
```

### 2️⃣ Open the project

```bash
cd Food-Ordering-System
```

### 3️⃣ Run the program

```bash
python Food-Ordering-System.py
```

---

# 🔑 Demo Login

Use the following credentials to test the application:

```text
📧 Email: manav@gmail.com
🔐 Password: manav123
```

---

# 🖥️ Terminal Preview

```text
╔══════════════════════════════════════════╗
║        🍔 FOOD ORDERING SYSTEM           ║
╠══════════════════════════════════════════╣
║                                          ║
║ 🔐 Login successful!                    ║
║                                          ║
║ 👤 Customer : Manav                     ║
║ 📞 Phone    : 9876543210                ║
║ 🏠 Address  : Delhi                     ║
║                                          ║
║ 📂 Category : Fast Food                 ║
║ 🍔 Burger   : ₹120 × 2 = ₹240           ║
║                                          ║
║ 🛒 Cart Total          : ₹240           ║
║ 🎉 Special Offer      : -₹30            ║
║ 🎟️ Coupon             : ₹0              ║
║ 🧾 GST                : ₹10.50          ║
║ 🚚 Delivery           : ₹40             ║
║ 💳 Payment            : UPI             ║
║                                          ║
║ 💵 Final Amount       : ₹220.50         ║
║ 📦 Status             : Confirmed       ║
║ ⭐ Rating             : 5/5             ║
║                                          ║
╚══════════════════════════════════════════╝
```

---

# 📚 Learning Outcomes

This project provides practical experience with:

* ✅ User input and validation
* ✅ Conditional statements
* ✅ Loops
* ✅ Lists and dictionaries
* ✅ Functions
* ✅ Parameters and return values
* ✅ Arithmetic calculations
* ✅ Stock management
* ✅ Cart management
* ✅ Basic application logic
* ✅ Real-world problem solving

---

# 💡 Why This Project?

### 🧠 Learn

```text
Variables
    +
Conditions
    +
Loops
    +
Lists
    +
Dictionaries
    +
Functions
```

### 🛠️ Build

```text
🔐 Login
📂 Menu
📦 Stock
🛒 Cart
💰 Billing
💳 Payment
📦 Order Status
⭐ Rating
```

### 🚀 Practice

```text
Problem Solving
      +
Program Flow
      +
User Interaction
      +
Basic Data Handling
```

---

# 🚀 Future Roadmap

### 🟢 Phase 1 — Next Features

* 🔍 **Food Search**
* 💳 **UPI/Card Details**
* 🛵 **Delivery Partner Assignment**
* 📍 **Interactive Delivery Tracking**

### 🟡 Phase 2 — Personalization & Storage

* 📜 **Order History**
* ❤️ **Favourite Food**
* 🎁 **Loyalty Points**
* 💾 **File Storage using `.txt` or `.json`**

### 🔴 Phase 3 — Advanced Version

* 🧑‍💼 **Admin Panel**
* 🗃️ **Database Integration**
* 🖥️ **GUI Application**
* 🌐 **Web Application**

---

# 🤝 Contributing

Contributions and improvements are welcome! 🎉

```bash
git clone https://github.com/techwithmanav/Food-Ordering-System.git
git checkout -b feature-name
git add .
git commit -m "Add new feature"
git push origin feature-name
```

Then create a Pull Request.

---

# 📄 License

This project is created for **learning and educational purposes**.

You are free to modify and improve the project for your own learning.

---

<div align="center">

## 🍔 Food Ordering System

### Simple • Beginner-Friendly • Python-Based

<br>

🍔   🍕   🥪   🍟   🥤

<br><br>

**Built with ❤️ using Python 🐍**

<br><br>

<img src="https://img.shields.io/badge/Made%20with-❤️%20%26%20🐍%20Python-3776AB?style=for-the-badge" />
<img src="https://img.shields.io/badge/Beginner--Friendly-2EA44F?style=for-the-badge" />

<br><br>

⭐ **Like this project? Give the repository a star!** ⭐

<br><br>

<a href="https://github.com/techwithmanav/Food-Ordering-System">
  <img src="https://img.shields.io/badge/⭐%20Visit%20Repository-FFD700?style=for-the-badge&logo=github&logoColor=black" />
</a>

<br><br>

**Learn → Build → Improve → Repeat 🚀**

<br>

<sub>Food Ordering System • Python Mini Project</sub>

</div>
```
