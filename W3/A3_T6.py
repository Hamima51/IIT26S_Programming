print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")

print()
print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")

choice = int(input("Your choice: "))

if choice == 1:
    print()
    print("Length options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")

    length_choice = int(input("Your choice: "))

    if length_choice == 1:
        meters = float(input("Insert meters: "))
        kilometers = meters * 0.001
        print(f"{meters:.1f} m is {kilometers:.1f} km")
    elif length_choice == 2:
        kilometers = float(input("Insert kilometers: "))
        meters = kilometers * 1000
        print(f"{kilometers:.1f} km is {meters:.1f} m")
    elif length_choice == 0:
        print("Exiting...")
    else:
        print("Unknown option.")