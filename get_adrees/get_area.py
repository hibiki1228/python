import get_gps, reverse_geocoder as rg

# 画像ファイルから緯度経度情報を得る
(lat, lon) = get_gps.get_gps("IMG_0311.jpg")
# 都市名を調べる
results = rg.search([(lat, lon)])
# 分かりやすく表示
area = {t: results[0][t] for t in results[0]}
print(area['cc'], area['admin1'], area['name'])