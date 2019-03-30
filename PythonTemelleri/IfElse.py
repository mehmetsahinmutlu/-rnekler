# a = int(input("Sayıyı Giriniz"))

if not a%2==0 :
    print("Sayı Tektir")
else:
    print("Sayı Çifttir")

vize1 = int(input("I. Vize Notunuzu Giriniz"))
vize2 = int(input("II. Vize Notunuzu Giriniz"))
final = int(input("Final Notunuzu Giriniz"))
Notu = round((vize1*0.3)+(vize2*0.3)+(final*0.4))
print(85*0.30)
print(75*0.30)
print((85+75)/2*0.60)
Sonuc = ""
if Notu < 25 and Notu >=0:
    Sonuc="FF"
elif Notu < 45 and Notu >=25:
    Sonuc="FD"
elif Notu < 55 and Notu >=45:
    Sonuc="DD"
elif Notu < 60 and Notu >=55:
    Sonuc="DC"
elif Notu < 70 and Notu >=60:
    Sonuc="CC"
elif Notu < 80 and Notu >=70:
    Sonuc="CB"
elif Notu < 85 and Notu >=80:
    Sonuc="BB"
elif Notu < 90 and Notu >=85:
    Sonuc="BA"
elif Notu <= 100 and Notu >=90:
    Sonuc="AA"
else:
    Sonuc = "Not Hesaplanamadı"
print("Notunuz {},{}  İyi Günler Dileriz".format(Sonuc,Notu))
input()    


