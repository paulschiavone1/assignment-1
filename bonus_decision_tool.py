# Bonus Challenge: Integrated Decision Tool

def is_profitable(revenue, cost):
    return revenue > cost


def main():
    revenue = float(input("Enter business revenue: "))
    cost = float(input("Enter business cost: "))
    category = input("Enter business category: ").strip().lower()

    match category:
        case "high margin":
            suggestion = "Reinvest"
        case "medium margin":
            suggestion = "Expand"
        case "low margin":
            suggestion = "Reduce Costs"
        case _:
            suggestion = "Review Business"


    if is_profitable(revenue, cost):
        profit = revenue - cost
        print(f"Profit: ${profit:.2f}")
        print(f"Suggestion: {suggestion}")
    else:
        print("The business is not profitable.")


main()