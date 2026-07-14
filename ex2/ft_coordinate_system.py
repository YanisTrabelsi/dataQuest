import math


def ask() -> list[str]:
    args: list[str] = input("Enter new coordinates as \
floats in format ’x,y,z’: ").split(",")
    if (len(args) != 3):
        print("Invalid syntax")
    return args


def get_player_pos() -> tuple[float, ...]:
    args: list[str] = []
    fargs: list[float] = []

    while (len(fargs) != 3):
        fargs.clear()
        args = ask()
        if (len(args) == 3):
            for arg in args:
                try:
                    fargs.append(float(arg))
                except ValueError as e:
                    print(f"Error on parameter '{arg}': {e}")
    pos: tuple[float, ...] = tuple(fargs)
    return pos


print("=== Game Coordinate System ===")
print("Get a first set of coordinates")
set1: tuple[float, ...] = get_player_pos()
x1: float = set1[0]
y1: float = set1[1]
z1: float = set1[2]
distance_from_center: float = math.sqrt(x1**2 + y1**2 + z1**2)
print(f"Got a first tuple: {set1}")
print(f"It includes: X={x1}, Y={y1}, Z={z1}")
print(f"Distance to center: {round(distance_from_center, 4)}\n")
print("Get a second set of coordinates")
set2: tuple[float, ...] = get_player_pos()
x2: float = set2[0]
y2: float = set2[1]
z2: float = set2[2]
distance: float = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")
