# Exercise 3: Customer Greeting Formatter

def format_greeting(name, title="Customer"):
    name = name.strip()

    if name == "":
        return "Hello, Valued Customer!"

    name = name.title()
    first_name = name.split()[0]

    return f"Hello, {first_name} ({title})!"


name = input("What's your full name? ")

print(format_greeting(name))