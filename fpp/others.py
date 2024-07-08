import random

numbers = [1, 6, 1, 6, 3, 7, 12, 6, 2, 6, 4, 8, 100, 5]
bigger = numbers[0]

for number in numbers:
    if number > bigger:
        bigger = number
print(f"Bigger Number =: [{bigger}]")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element)

customer = {
    "name": "vish",
}

print(customer.get("name"))

print(random.randint(10, 20))
members = ["Lenan", "John", "Emma", "Senna", "Bia"]
print(random.choice(members))
