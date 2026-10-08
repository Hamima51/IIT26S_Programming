
print("Program starting.")
print()

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspection = int(input("Insert inspection point: "))

print()

if start >= stop:
    print("Starting point value must be less than the stopping point value.")

if inspection < start or inspection > stop:
    print("Inspection value must be within the range of start and stop.")

if start < stop and start <= inspection <= stop:

    print("First loop - inspection with break:")

    for i in range(start, stop + 1):
        if i == inspection:
            break
        print(i, end=" " if i < inspection - 1 else "")

    print()
    print("Second loop - inspection with continue:")

    for i in range(start, stop + 1):
        if i == inspection:
            continue
        print(i, end=" " if i < stop else "")

    print()

print()
print("Program ending.")