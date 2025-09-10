for i in range(5):
    print(i)

for i in range(5):
    print("Who is tegar?")

print(50 * "=")

for i in range(1, 5, 2):
    print("Tegar is a student")

word = "Tegar is a good boy"
for letter in word:
    print(letter)

for m, n in enumerate(word):
    print(f"Index {m}. {n}")

for i in range(5, 1, -1):
    print("Tegar likes movies")

for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)

count = 0
while count < 4:
    print("Tegar love games")
    count += 1
