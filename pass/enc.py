#!/usr/bin/env python3
# コマンドラインから渡されたファイルを得る --- (*1)
import sys
if len(sys.argv) < 3:
    print("USAGES:")
    print("env.py targetfile keyfile")
    exit
target_file = sys.argv[1]
key_file = sys.argv[2]
out_file = target_file.replace('.txt', '') + ".out.txt"

# ファイルをバイナリモードで開く --- (*2)
out_fd = open(out_file, "wb")
target = open(target_file, "rb").read()
key = open(key_file, "rb").read()

# 独自の乱数生成関数 --- (*3)
rx, ry, rz, rw = (15424343, 949583, 991234, 11223344)
def randint(n):
    global rx, ry, rz, rw
    t = (rx ^ (rx << 11))
    rx, ry, rz = ry, rz, rw
    rw = rw = (rw ^ (rw >> 19)) ^ (t ^ (t >> 8))
    return rw % n

# 一バイトずつXOR処理 --- (*4)
res = bytearray()
for i, a in enumerate(target):
    b = key[i % len(key)]
    r = randint(256)
    c = a ^ b ^ r
    res.append(c)

# 結果を書き込む --- (*5)
out_fd.write(res)