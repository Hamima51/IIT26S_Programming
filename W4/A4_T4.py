
print("Program starting.")
print()

words = 0
characters = 0

word = input("Insert word (empty stops): ")

while word != "":
    words = words + 1
    characters = characters + len(word)
    word = input("Insert word (empty stops): ")

print()
print("You inserted:")
print("- " + str(words) + " words")
print("- " + str(characters) + " characters")

print()
print("Program ending.")