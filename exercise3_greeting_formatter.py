# Exercise 3: Customer Greeting Formatter

def format_greeting(name, title="Customer"):
    name = name.strip()

    if name == "":
        return "Hello, Valued Customer!"

    name = " ".join(name.split())
    name = name.title()

    return f"Hello, {name}!"


name = input("What's your full name? ")

print(format_greeting(name))