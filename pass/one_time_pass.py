a = 'test
'  #データ
b = '1234'  #乱数表
#暗号化
c = []
for aa, bb in zip(a, b):
    cc = chr(ord(aa) ^ ord(bb))
    c += [cc]
print("".join(c))