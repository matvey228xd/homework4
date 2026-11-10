number = int(input("Введіть ціле число: "))

mask = 1 << 3
bit = (number & mask) != 0

result = number << 3

print(f"3-й біт увімкнений: {bit}, Число * 8: {result}")