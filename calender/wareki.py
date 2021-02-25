# 西暦と和暦の対応テーブル --- (*1)
wareki_table = [
    {"name": "明治", "start": 1868, "end": 1912},
    {"name": "大正", "start": 1912, "end": 1926},
    {"name": "昭和", "start": 1926, "end": 1989},
    {"name": "平成", "start": 1989, "end": 2019},
    {"name": "令和", "start": 2019, "end": 9999}
]

# 西暦から和暦へ変換する関数を定義 --- (*2)
def seireki_wareki(year):
    for w in wareki_table:
        if w["start"] <= year < w["end"]:
            y = str(year - w["start"] + 1) + "年"
            if y == "1年": y = "元年"
            return w["name"] + y
    return "不明"

# 関数のテスト --- (*3)
if __name__ == "__main__":
    print(2018, "=", seireki_wareki(2018))
    print(2019, "=", seireki_wareki(2019))
    print(2020, "=", seireki_wareki(2020))