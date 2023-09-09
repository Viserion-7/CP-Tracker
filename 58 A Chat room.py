compareStr ='hello'
str = input()
pointer = 0

for letter in str:
    if letter == compareStr[pointer]:
        pointer += 1
    if pointer == 5:
        break

if pointer == 5:
    print("YES")
else:
    print("NO")