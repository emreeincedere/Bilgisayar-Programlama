#Bir otoparkta ilk 15 saat için saat başına 35 TL, 10 ile 30 saat arasında kalan süre için saat başına 50 TL, 30 saatten sonraki süre için ise saat başına 80 TL ücret alınmaktadır.
#Kullanıcının girdiği park süresine göre toplam otopark ücretini hesaplayan Python kodunu yazınız.


saat=float(input("Otoparkta kaldığınız süreyi giriniz: "))

if saat<=15:
    ucret=saat*30
elif saat<=35:
    ucret=(saat-10)*50+300
else:
    ucret=(saat-30)*80+1200

print(ucret)
