adim = ""

try:
    a = input("1. Sayı:")
    adim = "A.D.M.-1A"
    if a == "Soner":
        raise ZeroDivisionError
    b = int(input("2. Sayı:"))
    adim = "A.D.M.-1B"
except:
    print("Hata var Hata Mesajı",adim)
else:
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Sıfıra bölünme hatası")
finally:

