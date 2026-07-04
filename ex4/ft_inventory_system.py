import sys


def parser() -> dict[str, int]:
    args: list[str] = sys.argv[1:]
    inventory: dict[str, int] = {}

    for arg in args:
        try:
            key, value = arg.split(':')
        except ValueError:
            print(f"Error - invalid parameter ’{arg}’")
            continue
        if (key not in inventory):
            try:
                inventory[key] = int(value)
            except ValueError as e:
                print(f"Quantity error for ’{key}’: {e}")
        else:
            print(f"Redundant item ’{key}’ - discarding")
    return inventory


print("=== Inventory System Analysis ===")

inventory: dict[str, int] = parser()
items: list[str] = list(inventory.keys())
quantity: int = len(items)
values: int = sum(inventory.values())
greater: int = 0
greater_key: str = ""
lower: int
lower_key: str = ""
new_item: dict[str, int] = {"magic_item": 1}

print(inventory)
for k in inventory:
    percentage: float = inventory[k] / values * 100
    print(f"Item {k} represents {round(percentage, 1)}%")
for k in inventory:
    if inventory[k] > greater:
        greater = inventory[k]
        greater_key = k
lower = greater
for k in inventory:
    if inventory[k] < lower:
        lower = inventory[k]
        lower_key = k

print(f"Item most abundant: {greater_key} with quantity {greater}")
print(f"Item least abundant: {lower_key} with quantity {lower}")

inventory.update(new_item)
print(inventory)
