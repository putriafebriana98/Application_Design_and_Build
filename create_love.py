n = 6  # Controls the size of the heart
for i in range(n // 2, n):  # Upper part - two semi-circles
    print(" " * (n - i - 1) + "*" * (2 * i + 1) + " " * (n - i) + "*" * (2 * i + 1))

for i in range(n, -1, -1):  # Lower part - downward triangle
    print(" " * (n - i) + "*" * (2 * i + 1))
