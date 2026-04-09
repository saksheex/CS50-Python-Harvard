# 🎓 CS50P — Introduction to Programming with Python

> My complete solutions to all problem sets from Harvard's [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/2022/).

---

## 📋 Table of Contents

- [About](#about)
- [Week 0 — Functions & Variables](#week-0--functions--variables)
- [Week 1 — Conditionals](#week-1--conditionals)
- [Week 2 — Loops](#week-2--loops)
- [Week 3 — Exceptions](#week-3--exceptions)
- [Week 4 — Libraries](#week-4--libraries)
- [Week 6 — File I/O](#week-6--file-io)
- [Week 7 — Regular Expressions](#week-7--regular-expressions)
- [Week 8 — Object-Oriented Programming](#week-8--object-oriented-programming)
- [Technologies Used](#technologies-used)
- [How to Run](#how-to-run)

---

## About

This repository contains my complete solutions to **CS50P**, Harvard University's free online course on Python programming. Each problem is solved in its own `.py` file following the course specifications.

---

## Week 0 — Functions & Variables

---

### 🔤 Indoor Voice [`indoor.py`](./indoor.py)

> *"WRITING IN ALL CAPS IS LIKE YELLING."*

Prompts the user for input and outputs it entirely in **lowercase**. Punctuation and whitespace remain unchanged.

**Example:**
```
Input:  HELLO, WORLD
Output: hello, world
```

---

### 😊 Making Faces [`faces.py`](./faces.py)

Converts old-school **emoticons** to modern emoji using a `convert` function!

| Emoticon | Emoji |
|----------|-------|
| `:)`     | 🙂    |
| `:(`     | 🙁    |

**Example:**
```
Input:  Hello :)
Output: Hello 🙂
```

---

### 💰 Tip Calculator [`tip.py`](./tip.py)

Completes two missing functions in a tip calculator:

- `dollars_to_float(d)` — strips `$` and returns a `float`
- `percent_to_float(p)` — strips `%` and returns a `float`

**Example:**
```
How much was the meal? $50.00
What percentage would you like to tip? 15%
Leave $7.50
```

---

## Week 1 — Conditionals

---

### 🏦 Home Federal Savings Bank [`bank.py`](./bank.py)

Inspired by *Seinfeld* — checks how a greeting starts and outputs a dollar amount. Case-insensitive, ignores leading whitespace.

| Greeting starts with | Output |
|----------------------|--------|
| `"hello"`            | `$0`   |
| `"h"` (not hello)    | `$20`  |
| Anything else        | `$100` |

**Example:**
```
Input:  How you doing?
Output: $20
```

---

### 🍽️ Meal Time [`meal.py`](./meal.py)

Tells you what meal time it is based on 24-hour input. Implements a `convert(time)` function.

| Time Range    | Meal      |
|---------------|-----------|
| 7:00 – 8:00   | Breakfast |
| 12:00 – 13:00 | Lunch     |
| 18:00 – 19:00 | Dinner    |

**Example:**
```
Input:  7:30
Output: breakfast time
```

---

### 🐪 camelCase [`camel.py`](./camel.py)

Converts **camelCase** variable names to Python's preferred **snake_case**.

**Example:**
```
Input:  preferredFirstName
Output: preferred_first_name
```

---

## Week 2 — Loops

---

### 🥤 Coke Machine [`coke.py`](./coke.py)

Simulates a Coke machine selling bottles for **50 cents**, accepting only 25¢, 10¢, and 5¢ coins. Keeps prompting until paid, then shows change owed.

**Example:**
```
Amount Due: 50
Insert Coin: 25
Amount Due: 25
Insert Coin: 25
Change Owed: 0
```

---

### 🐦 Just setting up my twttr [`twttr.py`](./twttr.py)

Removes all **vowels** (A, E, I, O, U — upper and lowercase) from user input.

**Example:**
```
Input:  What's your name?
Output: Wht's yr nm?
```

---

### 🚗 Vanity Plates [`plates.py`](./plates.py)

Validates Massachusetts vanity license plates. Rules:
- Must start with at least 2 letters
- 2–6 characters total
- Numbers only at the end; first number cannot be `0`
- No periods, spaces, or punctuation

**Example:**
```
Input:  CS50
Output: Valid

Input:  CS05
Output: Invalid
```

---

### ⛽ Fuel Gauge [`fuel.py`](./fuel.py)

Takes a fraction `X/Y` and outputs fuel as a percentage. Outputs `E` if ≤ 1% and `F` if ≥ 99%. Handles `ValueError` and `ZeroDivisionError`.

**Example:**
```
Input:  1/4
Output: 25%
```

---

## Week 3 — Exceptions

---

### 🛒 Grocery List [`grocery.py`](./grocery.py)

Takes grocery items one per line (ended with `Ctrl+D`), then outputs them sorted alphabetically in **UPPERCASE** with item counts.

**Example:**
```
Input: apple, banana, apple

Output:
2 APPLE
1 BANANA
```

---

### 📅 Outdated [`outdated.py`](./outdated.py)

Converts US-format dates to **ISO 8601** (`YYYY-MM-DD`). Accepts both `9/8/1636` and `September 8, 1636` formats.

**Example:**
```
Input:  September 8, 1636
Output: 1636-09-08
```

---

## Week 4 — Libraries

---

### 😂 Emojize [`emoji.py`](./emoji.py)

> *Originally named `emojize.py` in the problem set.*

Converts emoji **codes and aliases** in user input to actual emoji using the `emoji` library.

**Example:**
```
Input:  I love CS50 :thumbs_up:
Output: I love CS50 👍
```

---

### 🔤 Frank, Ian and Glen's Letters [`file.py`](./file.py)

> *Originally named `figlet.py` in the problem set.*

Uses **pyfiglet** to render text in large ASCII art fonts. Accepts 0 or 2 command-line arguments (`-f` or `--font`). With no arguments, picks a **random font**.

**Example:**
```bash
$ python file.py -f slant
Input: Hello
```
```
   __  __     ____
  / / / /__  / / /___
 / /_/ / _ \/ / / __ \
/_____/\___/_/_/\____/
```

---

### 🍕 Pinocchio's Pizza [`pizza.py`](./pizza.py)

Reads a CSV file of Pinocchio's pizza menu and outputs it as a formatted **ASCII art table** using the `tabulate` library with `grid` format.

**Example output:**
```
+------------------+---------+---------+
| Sicilian Pizza   | Small   | Large   |
+==================+=========+=========+
| Cheese           | $25.50  | $39.95  |
+------------------+---------+---------+
| 1 item           | $27.50  | $41.95  |
+------------------+---------+---------+
```

**Usage:**
```bash
python pizza.py sicilian.csv
```

---

## Week 6 — File I/O

---

### 📊 Lines of Code [`lines.py`](./lines.py)

Counts **lines of code** (LOC) in a `.py` file, excluding blank lines and comments. Exits via `sys.exit` if the argument is invalid or the file doesn't exist.

**Usage:**
```bash
python lines.py hello.py
```

---

### 🧙 Scourgify [`scourgify.py`](./scourgify.py)

Cleans up a CSV of Hogwarts student names. Takes a CSV with `name, house` columns (name as `"Last, First"`) and outputs a new CSV with `first, last, house` columns.

**Example:**
```
Input:  "Potter, Harry",Gryffindor
Output: Harry,Potter,Gryffindor
```

---

### 👕 CS50 Shirt [`shirt.py`](./shirt.py)

Overlays the CS50 `shirt.png` onto a user-provided photo using **Pillow**. Resizes and crops the input to match shirt size, then saves the result.

**Usage:**
```bash
python shirt.py before.jpg after.jpg
```

---

## Week 7 — Regular Expressions

---

### 🔢 NUMB3RS [`numb3rs.py`](./numb3rs.py)

Implements a `validate` function using **regex** to check if a string is a valid **IPv4 address** (each octet between 0–255).

**Example:**
```
Input:  275.3.6.28
Output: False

Input:  192.168.1.1
Output: True
```

---

### 📺 Watch on YouTube [`watch.py`](./watch.py)

Implements a `parse` function that extracts a YouTube video ID from an HTML `<iframe>` and returns the short `youtu.be` shareable link.

**Example:**
```
Input:  <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
Output: https://youtu.be/xvFZjo5PgG0
```

---

### ✉️ Response Validation [`response.py`](./response.py)

Prompts the user for an email address and validates it using the `validators` library. Outputs `Valid` or `Invalid`.

**Example:**
```
Input:  hello@example.com
Output: Valid
```

---

## Week 8 — Object-Oriented Programming

---

### ⏳ Seasons of Love [`seasons.py`](./seasons.py)

Prompts for a date of birth (`YYYY-MM-DD`) and prints age in **minutes**, written out in English words like the song from *Rent*.

**Example:**
```
Input:  1999-01-01
Output: thirteen million, two hundred twenty-five thousand, six hundred minutes
```

---

### 🍪 Cookie Jar [`jar.py`](./jar.py)

Implements a `Jar` class with `deposit`, `withdraw`, `capacity`, and `size` methods. `__str__` returns 🍪 × number of cookies.

**Example:**
```python
jar = Jar(10)
jar.deposit(3)
print(jar)  # 🍪🍪🍪
```

---

### 👕 CS50 Shirtificate [`shirtificate.py`](./shirtificate.py)

Generates a personalized **CS50 Shirtificate PDF** using `fpdf2`!

**Specifications:**
- Portrait A4 PDF (210mm × 297mm)
- "CS50 Shirtificate" heading centered at the top
- The CS50 t-shirt image centered on the page
- User's name printed in **white text** over the shirt

**To run:**
```bash
pip install fpdf2
python shirtificate.py
Name: Sakshee Singh
```

**Output:**

![CS50 Shirtificate — Sakshee Singh took CS50](./shirtificate_output.png)

---

### ☕ Felipe's Taqueria [`cafe.py`](./cafe.py)

> *Originally named `taqueria.py` in the problem set.*

Interactive ordering system for Felipe's Taqueria. Users add items one per line; running total updates after each addition. Handles `EOFError` on `Ctrl+D`.

**Menu:** Baja Taco, Burrito, Bowl, Nachos, Quesadilla, Super Burrito, Super Quesadilla, Taco, Tortilla Salad.

**Example:**
```
Item: Taco
Total: $3.00
Item: Burrito
Total: $10.50
```

---

### 🔢 Guessing Game [`game.py`](./game.py)

User sets a level `n`, program picks a random number between 1 and `n`, and gives hints until the user guesses correctly.

**Example:**
```
Level: 10
Guess: 5
Too small!
Guess: 8
Too large!
Guess: 7
Just right!
```

---

### 🧮 Little Professor [`professor.py`](./professor.py)

Simulates the **Little Professor** toy — 10 random addition problems, up to 3 tries each. Shows `EEE` on wrong answers, reveals the correct answer after 3 failures. Reports final score out of 10.

---

### ₿ Bitcoin Price Index [`bitcoin.py`](./bitcoin.py)

Fetches the **live Bitcoin price** from the CoinCap v3 API and calculates cost for `n` Bitcoins in USD to 4 decimal places.

**Usage:**
```bash
python bitcoin.py 2
```
**Output:**
```
$246,813.5780
```

---

## Technologies Used

| Tool / Library | Purpose |
|----------------|---------|
| Python 3 | Core language |
| fpdf2 | PDF generation (Shirtificate) |
| pyfiglet | ASCII art fonts (FIGlet) |
| emoji | Emoji code conversion |
| requests | HTTP API calls (Bitcoin) |
| tabulate | ASCII table formatting (Pizza) |
| Pillow | Image manipulation (Shirt) |
| validators | Email validation |
| pytest | Unit testing |
| re | Regular expressions |
| datetime | Date calculations (Seasons) |

---

## How to Run

**1. Clone the repository:**
```bash
git clone https://github.com/your-username/cs50p.git
cd cs50p
```

**2. Install all dependencies:**
```bash
pip install fpdf2 pyfiglet emoji requests tabulate Pillow validators pytest
```

**3. Run any problem:**
```bash
python indoor.py
python shirtificate.py
python game.py
python bitcoin.py 1
```

---

> *This is CS50P* 🎓
