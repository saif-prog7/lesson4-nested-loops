string = input("Enter your string: ")
char = input("Enter the character to count: ")
i = 0
count = 0
while i < len(string):
    if string[i] == char:
        count += 1
    i +=1
print(f"the character {char} occurs {count} time in the string {string}")
        