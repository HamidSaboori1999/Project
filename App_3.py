i = int(input("To what number should I continue the Fibonacci sequence ? "))

x, y = 0, 1
while y <= i:
    print(y)
    x, y = y, x + y
