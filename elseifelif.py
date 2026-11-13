
koli = int(input("Koli sayısını giriniz: "))
agirlik = float(input("Toplam ağırlığı giriniz: "))

ortalama = agirlik / koli
kapasite = 1500

if agirlik > kapasite:
    print("Kamyon yükü taşıyamaz")
else:
    print("Kamyon yükü taşıyabilir")
