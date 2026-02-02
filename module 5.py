import random

n = int(input("How many dice to roll? "))

total = 0

for i in range(n):
    roll = random.randint(1, 6)
    total += roll

print("Sum of dice:", total)

numbers = []

while True:
    user_input = input("Enter a number (empty to quit): ")

    if user_input == "":
        break

    numbers.append(float(user_input))

numbers.sort(reverse=True)

print("Five greatest numbers:")

for num in numbers[:5]:
    print(num)

n = int(input("Enter an integer: "))

if n < 2:
    print(n, "is not a prime number.")
else:
    is_prime = True

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")

cities = []

for i in range(5):
    city = input("Enter city name: ")
    cities.append(city)

print("Cities you entered:")

for city in cities:
    print(city)
