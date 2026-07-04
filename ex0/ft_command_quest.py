import sys

args: list[str] = sys.argv
len: int = len(args)
print("=== Command Quest ===")
print(f"Program name: {args[0]}")
if (len == 1):
    print("No arguments provided!")
else:
    print(f"Arguments received: {len - 1}")
    for i in range(len - 1):
        print(f"Arguments {i + 1}: {args[i + 1]}")
print(f"Total arguments: {len}")
