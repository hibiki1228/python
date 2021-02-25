# Janomeを使うための宣言 
from janome.tokenizer import Tokenizer

# 「こころ」を読み込む --- (*1)
fp = open("kokoro.txt", "rt", encoding="sjis")
text = fp.read()

# Janomeの準備 --- (*2)
tok = Tokenizer()
tokens = tok.tokenize(text)

# 形態素をカウント --- (*3)
counter = {}
for t in tokens:
    bf = t.base_form
    if not bf in counter: counter[bf] = 0
    counter[bf] += 1

# カウントの多い順に並び替える --- (*4)
sc = sorted(counter.items(), key=lambda x: x[1], reverse=True)
# 並び替えたものを表示 --- (*5)
for i, t in enumerate(sc):
    if i >= 100: break
    key, cnt = t
    print((i + 1), ".", key, "=", cnt)