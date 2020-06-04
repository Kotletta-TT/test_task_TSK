import random

def one():
    return [random.uniform(-1, 1) for i in range(100)]

def two(massive):
    new_massive = []
    previous_value = 0
    for i in massive:
        new_value = i + previous_value
        new_massive.append(new_value)
        previous_value = new_value
    return new_massive

def three(massive):
    import matplotlib.pyplot as plt
    x = range(1, 101)
    y = massive
    plt.plot(x, y)
    plt.show()

massive = one()
new_massive = two(massive)
print(two(massive))
three(new_massive)