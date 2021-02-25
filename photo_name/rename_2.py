import glob, os
files = glob.glob("*.jpg")
for i, old_name in enumerate(files): # --- (*1)
    # ファイル名を決定する --- (*2)
    new_name = "kujira-{0:03d}.jpg".format(i + 1)
    # 改名する
    os.rename(old_name, new_name)
    # 状況を報告
    print(old_name + "→" + new_name)