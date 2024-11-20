import random

random_float = random.random()
print(f"Випадкове число від 0.0 до 1.0: {random_float}")

random_int = random.randint(400, 500)
print(f"Випадкове ціле число від 400 до 500: {random_int}")

random_float = random.uniform(400.0, 500.0)
print(
    f"Випадкове число з плаваючою крапкою від 400.0 до 500.0: {random_float}")

car_brands = ["Toyota", "Ford", "BMW",
              "Mercedes", "Honda", "Audi", "Chevrolet"]

random_car_brand = random.choice(car_brands)
print(f"Випадкова марка автомобіля: {random_car_brand}")
