var1 = "Ben bir ceviz ağacıyım Gülhane Parkında\a "
var1 += "Ne sen bunun farkındasın nede polis farkında"



print(var1[:])


var1 = "ali;veli;12345678910;"
var1 += "veli;can;85274196321"

# var1 = "123456789"

print(var1.split(";"))


var1 = "www.vektorelbilisim.com"

print(var1.replace('.com','.net'))
print(var1.split("."))
print(dir(var1))

var1 = "Teşekkürler Süpermen"
print(var1.replace("e","i").replace("ü","i").split())


adi = input("Adınız:")
soyadi = input("Soyadiniz")
sonuc = adi.capitalize() + " " + soyadi.upper()
print(sonuc)

print(input("Adınız:"),input("Soyadınız:").upper())



var1 = "İbrahim EDİZ"
print(var1.splitlines())
print(var1.swapcase())
print(var1.zfill(25))

d1 = "ali.jpg"
d2 = "manzara.png"
d3 = "hayalet sevgilim.ogg"
for i in d1,d2,d3:
    if i.endswith("ogg"):
        print(i)