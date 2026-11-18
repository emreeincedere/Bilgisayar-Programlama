ortalama=float(input("Ortalamanızı giriniz"))
gelir=float(input("Aile gelirinizi giriniz:"))
if ortalama>=90 and gelir<=20000:
   print("Tam burs")
elif ortalama>=75 and gelir<=30000:
   print("Yarım burs")
else:
   print("Burs yok")