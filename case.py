sayi = int(input("Değer giriniz: "))

match sayi:
    case 1:
        print("Toplama")
    case 2:
        print("Çıkarma")
    case 3:
        print("Çarpma")
    case 4:
        print("Bölme")
    case _:
        print("Geçersiz işlem")