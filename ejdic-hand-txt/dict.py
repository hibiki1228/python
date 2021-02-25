word = input("write words: ")

fp = open("ejdict-hand-utf8.txt", "r", encoding="utf-8")

for line in fp:
    if line.startswith(word):
        print(line)
fp.close()