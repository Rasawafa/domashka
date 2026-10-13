text = input("Текст: ").lower()

text1 = ""
for c in text:
    if c.isalnum() or c.isspace():
        text1 += c
words = text1.split()

f = {}
for i in words:
    f[i] = f.get(i, 0) + 1
print("Уникальных слов:", len(f))

while True:
    order = input("Порядок (1 — убыв., 2 — возр.): ").strip()
    if order == "1" or order == "2":
        break
    print("Ошибка: такого порядка нету, введите число из списка (1 — убыв., 2 — возр.).")

if order == "1":
    a = sorted(f, key = f.get, reverse=True)[:5]
else:
    a = sorted(f, key = f.get)[:5]

for i in a:
    print(i, "–", f[i])
