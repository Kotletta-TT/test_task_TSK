import random
import matplotlib.pyplot as plt

def generate_massive():
    return [random.uniform(-1, 1) for i in range(100)]

def convert_commulative(massive):
    new_massive = []
    previous_value = 0
    for i in massive:
        new_value = i + previous_value
        new_massive.append(new_value)
        previous_value = new_value
    return new_massive

def check_intersection(massive1, massive2):
    coordinate_intersection = []

    for i in range(len(massive1)-1):
        x1_1 = i
        x2_1 = i
        x1_2 = i + 1
        x2_2 = i + 1
        y1_1 = massive1[i]
        y1_2 = massive1[i+1]
        y2_1 = massive2[i]
        y2_2 = massive2[i+1]
        A1 = y1_1 - y1_2
        B1 = x1_2 - x1_1
        C1 = x1_1 * y1_2 - x1_2 * y1_1
        A2 = y2_1 - y2_2
        B2 = x2_2 - x2_1
        C2 = x2_1 * y2_2 - x2_2 * y2_1

        if B1 * A2 - B2 * A1 and A1:
            y = (C2 * A1 - C1 * A2) / (B1 * A2 - B2 * A1)
            x = (-C1 - B1 * y) / A1
            if min(x1_1, x1_2) <= x <= max(x1_1, x1_2):
                coordinate_intersection.append([x, y])

        elif B1 * A2 - B2 * A1 and A2:
            y = (C2 * A1 - C1 * A2) / (B1 * A2 - B2 * A1)
            x = (-C2 - B2 * y) / A2
            if min(x1_1, x1_2) <= x <= max(x1_1, x1_2):
                coordinate_intersection.append([x, y])

    return coordinate_intersection

def create_graphics(massive, second_massive):
    range(len(massive))
    plt.plot(range(len(massive)), massive, "-")
    plt.plot(range(len(second_massive)), second_massive, "-")
    intersections = check_intersection(massive, second_massive)
    print("Intersection points:", end='')
    for intersection in intersections:
        plt.plot(intersection[0], intersection[1], 'ro')
        print(f"({intersection[0]} : {intersection[1]})", end=" ")
    plt.show()





first_init_massive = generate_massive()
second_init_massive = generate_massive()
first_cumulative_massive = convert_commulative(first_init_massive)
second_cumulative_massive = convert_commulative(second_init_massive)
create_graphics(first_cumulative_massive, second_cumulative_massive)
