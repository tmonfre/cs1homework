def f(a):
    global x
    x = 2 * a
    y = 3 * x
    return y - x -1

x = 2
y = 3
print(str(x) + ", " + str(y))
print(f(y))
print(str(x) + ", " + str(y))