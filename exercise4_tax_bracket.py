# Exercise 4: Tax Bracket Determiner

def get_tax_bracket(income):
    if income < 0:
        return "Invalid income."
    elif income < 50000:
        return "Low (10%)"
    elif income < 100000:
        return "Medium (20%)"
    else:
        return "High (30%)"


income = float(input("Enter your income: "))

bracket = get_tax_bracket(income)

if income < 0:
    print("Your bracket: Invalid income.")
else:
    if income < 50000:
        rate = 0.10
    elif income < 100000:
        rate = 0.20
    else:
        rate = 0.30

    tax = income * rate
    print(f"Your bracket: {bracket}. Estimated tax: ${tax:.2f}")