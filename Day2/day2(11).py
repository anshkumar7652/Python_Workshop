print("\n----- Bitwise Operators Menu -----")
print("1. Bitwise AND (&)")
print("2. Bitwise OR (|)")
print("3. Bitwise XOR (^)")
print("4. Bitwise NOT (~)")
print("5. Left Shift (<<)")
print("6. Right Shift (>>)")
print("7. Exit")

choice = int(input("Enter your choice: "))

n1 = int(input("Enter first number: "))

if choice != 4:
    n2 = int(input("Enter second number / shift count: "))

match choice:

        case 1:
            result = n1 & n2
            print(f"{n1} ({bin(n1)}) & {n2} ({bin(n2)}) = {result} ({bin(result)})")

        case 2:
            result = n1 | n2
            print(f"{n1} ({bin(n1)}) | {n2} ({bin(n2)}) = {result} ({bin(result)})")

        case 3:
            result = n1 ^ n2
            print(f"{n1} ({bin(n1)}) ^ {n2} ({bin(n2)}) = {result} ({bin(result)})")

        case 4:
            result = ~n1
            print(f"~{n1} ({bin(n1)}) = {result} ({bin(result)})")

        case 5:
            result = n1 << n2
            print(f"{n1} ({bin(n1)}) << {n2} = {result} ({bin(result)})")

        case 6:
            result = n1 >> n2
            print(f"{n1} ({bin(n1)}) >> {n2} = {result} ({bin(result)})")

        case _:
            print("Invalid Choice")