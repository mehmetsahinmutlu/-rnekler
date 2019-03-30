
def dosyaAc(dosyayolu):
    import os 
    dosya = None
    if os.path.exists(dosyayolu):
        dosya = open(dosyayolu,"r+")
    else:
        dosya = open(dosyayolu,"w+")
    return dosya

def KayitEkle(dosyayolu):
    try:
        dosya = dosyaAc(dosyayolu)
        liste = dosya.readlines()      
        ad = input("Adı Giriniz:")
        soyad = input("Soyadı Giriniz")
        tel = input("Telefon Giriniz")
        kayit = ad + ";" + soyad + ";" + tel + "\n"
        liste.append(kayit)
        dosya.seek(0)
        dosya.truncate()
        dosya.writelines(liste)
    except:
        print("Hata Var")
    finally:
        dosya.close()

def KayitGuncelle(dosyayolu):
    try:
        dosya = dosyaAc(dosyayolu)
        liste = dosya.readlines()
        print("-"*30)
        for item in liste:
            print(liste.index(item)+1,item,sep="-")
        print("-"*30)
        kayitNum = int(input("Düzenlemek istediğiniz kaydın numarasını giriniz"))
        ad = input("Adı Giriniz:")
        soyad = input("Soyadı Giriniz")
        tel = input("Telefon Giriniz")
        liste[kayitNum-1] = ad + ";" + soyad + ";" + tel + "\n"
        dosya.seek(0)
        dosya.truncate()
        dosya.writelines(liste)
    except:
        print("Hata Var")
    finally:
        dosya.close()

def KayitSil(dosyayolu):
    try:
        dosya = dosyaAc(dosyayolu)
        liste = dosya.readlines()
        print("-"*30)
        for item in liste:
            print(liste.index(item)+1,item,sep="-")
        print("-"*30)
        kayitNum = int(input("Silmek istediğiniz kaydın numarasını giriniz"))
        liste.pop(kayitNum-1)
        dosya.seek(0)
        dosya.truncate()
        dosya.writelines(liste)
    except:
        print("Hata Var")
    finally:
        dosya.close()

def Listeleme(dosyayolu):
    try:
        dosya = dosyaAc(dosyayolu)
        liste = dosya.readlines()
        print("-"*30)
        for item in liste:
            print(liste.index(item)+1,item,sep="-")
        print("-"*30)
    except:
        print("Hata Var")
    finally:
        dosya.close()

dosyayolu = r"D:\efter.csv"
while True:
    demet = ("Listeleme","Kayıt Ekleme","Kayıt Düzenleme","Kayıt Silme","Çıkış")
    print("_"*40)
    for i in demet:
        print(demet.index(i)+1,i,end="\n")
    print("_"*40)
    islem = int(input("Yapmak istediğiniz işlemi seçiniz"))
    if islem == 1:
        Listeleme(dosyayolu)
    elif islem == 2:
        KayitEkle(dosyayolu)
    elif islem == 3:
        KayitGuncelle(dosyayolu)
    elif islem == 4:
        KayitSil(dosyayolu)
    elif islem == 5:
        break
    else:
        print("Hatalı İşlem Seçimi")
    
