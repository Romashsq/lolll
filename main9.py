import math

my_list = [42, "Python", 3.14, "Programming", -7, "Code"]

for item in my_list:
    if isinstance(item, (int, float)):
        result = math.sin(item)
        print(f"Number: {item}, sine: {result}")

for item in my_list:
    if isinstance(item, str):
        length = len(item)
        print(f"String: '{item}', length: {length}")

list_length = len(my_list)
print(f"Length of the list: {list_length}")
