import matplotlib.pyplot as plt

months = ['Вересень', 'Жовтень', 'Листопад']
product_1_prices = [50, 55, 53]
product_2_prices = [45, 48, 47]

plt.figure(figsize=(8, 5))
plt.plot(months, product_1_prices, marker='o', label='Товар 1', color='blue')
plt.plot(months, product_2_prices, marker='s', label='Товар 2', color='orange')

plt.title('Порівняння цін двох товарів за останні 3 місяці', fontsize=14)
plt.xlabel('Місяці', fontsize=12)
plt.ylabel('Ціна (у грн)', fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
