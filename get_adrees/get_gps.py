from PIL import Image
import PIL.ExifTags as ExifTags

def get_gps(fname):
    # 画像ファイルを開く --- (*1)
    im = Image.open(fname)
    # EXIF情報を辞書型で得る
    exif = {
        ExifTags.TAGS[k]: v
        for k, v in im._getexif().items()
        if k in ExifTags.TAGS
    }
    # GPS情報を得る --- (*2)
    gps_tags = exif["GPSInfo"]
    gps = {
        ExifTags.GPSTAGS.get(t, t): gps_tags[t]
        for t in gps_tags
    }
    # 緯度経度情報を得る --- (*3)
    def conv_deg(v):
        # 分数を度に変換
        d = v[0]
        m = v[1]
        s = v[2]
        return d + (m / 60.000) + (s / 3600.000)
    lat = conv_deg(gps["GPSLatitude"])
    lat_ref = gps["GPSLatitudeRef"]
    if lat_ref != "N": lat = 0 - lat
    lon = conv_deg(gps["GPSLongitude"])
    lon_ref = gps["GPSLongitudeRef"]
    if lon_ref != "E": lon = 0 - lon
    return lat, lon

if __name__ == "__main__":
    lat, lon = get_gps("IMG_0311.jpg")
    print(lat, lon)