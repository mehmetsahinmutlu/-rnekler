tcno = "12345678910"
adi = "Ali"
soyadi = "Veli"
adres = "ANKARA"

var1 = """\t\tT.C.\t\t\n \tGAZİ ÜNİVERSİTESİ\t \n
    Kimlik Numarası :{3}\n
    Adı Soyadı : {1} {2} 
    Adres : {0}   """.format(adres,adi,soyadi,tcno)
print(var1)


var1 = "ttri pana zomi gambi yetsi zz"
print(var1.strip("t").strip("z"))

print(var1.find(" "))