# 🧮 Calculatrice en Ligne de Commande

A simple Python command-line calculator that performs basic arithmetic operations in a loop until the user decides to stop.

---

## 📋 Description

This program lets the user perform **basic arithmetic operations** interactively:
- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- 〰️ Modulo (remainder)

The program keeps running as long as the user answers **"oui"**, and exits gracefully when they answer **"non"**.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your machine

### Run the program

```bash
python calculatrice.py
```

---

## 🖥️ Usage Example

```
veut tu calcule (oui-non): oui
entre un nombre: 10
entre un symbole de calcule(+,-,%,*): +
entre un nombre: 5
15
veut tu calcule (oui-non): oui
entre un nombre: 9
entre un symbole de calcule(+,-,%,*): %
entre un nombre: 4
1
veut tu calcule (oui-non): non
Merci d'avoir utilisé la calculatrice !
```

---

## 🔢 Supported Operations

| Symbol | Operation      | Example        |
|--------|----------------|----------------|
| `+`    | Addition       | `5 + 3 = 8`    |
| `-`    | Subtraction    | `9 - 4 = 5`    |
| `*`    | Multiplication | `6 * 7 = 42`   |
| `%`    | Modulo         | `10 % 3 = 1`   |

---

## ⚠️ Error Handling

- Division by zero with `%` is detected and displays a warning message.

---

## 📁 Project Structure

```
📦 calculatrice
 ┗ 📜 calculatrice.py
 ┗ 📜 README.md
```

---

## 🛠️ Possible Improvements

- [ ] Add support for **division** (`/`) and **integer division** (`//`)
- [ ] Handle **non-numeric inputs** gracefully (try/except)
- [ ] Handle **division by zero** for all relevant operators
- [ ] Allow **decimal numbers** (float) as input
- [ ] Add a **history** of all calculations done in the session
- [ ] Build a **GUI** version with Tkinter

---

## 👤 Author

> Made with ❤️ and Python

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
