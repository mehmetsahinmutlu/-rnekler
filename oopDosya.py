class KayitIslem:
    dosyaFormat = ".csv"
    def __init__(self,*args,dosyaYolu):
        self.dosyaYolu = dosyaYolu+self.dosyaFormat
        self.kayitListe = list(args)
        # self.Giris()
        self.adim = ""

    def dosyaAc(self):
        import os 
        dosya = None
        if os.path.exists(self.dosyaYolu):
            dosya = open(self.dosyaYolu,"r+")
            self.adim = "dosyaAc_1"
        else:
            dosya = open(self.dosyaYolu,"w+")
            self.adim = "dosyaAc_2"
        return dosya

    def Listeleme(self):
        dosya = None
        try:
            dosya = self.dosyaAc()
            self.adim = "Listeleme_1"
            liste = dosya.readlines()
            self.adim = "Listeleme_2"
            print("-"*30)
            for item in liste:
                print(liste.index(item)+1,item,sep="-")
            print("-"*30)
            self.adim = "Listeleme_3"
        except:
            print("Hata Var",self.adim)
        finally:
            dosya.close()

    def KayitEkle(self):
        try:
            dosya = self.dosyaAc()
            liste = dosya.readlines()  
            kayit = ""
            for item in self.kayitListe:
                kayit += input(item + " Verisini Giriniz") + ";"
            kayit += "\n"
            liste.append(kayit)
            dosya.seek(0)
            dosya.truncate()
            dosya.writelines(liste)
        except:
            print("Hata Var")
        finally:
            dosya.close()

    def KayitGuncelle(self):
        try:
            dosya = self.dosyaAc()
            liste = dosya.readlines()
            print("-"*30)
            for item in liste:
                print(liste.index(item)+1,item,sep="-")
            print("-"*30)
            kayitNum = int(input("Düzenlemek istediğiniz kaydın numarasını giriniz"))
            kayit = ""
            for item in self.kayitListe:
                kayit += input(item + " Verisini Giriniz") + ";"
            kayit += "\n"
            liste[kayitNum-1] = kayit
            dosya.seek(0)
            dosya.truncate()
            dosya.writelines(liste)
        except:
            print("Hata Var")
        finally:
            dosya.close()

    def KayitSil(self):
        try:
            dosya = self.dosyaAc()
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
    def Giris(self):
        while True:
            demet = ("Listeleme","Kayıt Ekleme","Kayıt Düzenleme","Kayıt Silme","Çıkış")
            print("_"*40)
            for i in demet:
                print(demet.index(i)+1,i,end="\n")
            print("_"*40)
            islem = int(input("Yapmak istediğiniz işlemi seçiniz"))
            if islem == 1:
                self.Listeleme()
            elif islem == 2:
                self.KayitEkle()
            elif islem == 3:
                self.KayitGuncelle()
            elif islem == 4:
                self.KayitSil()
            elif islem == 5:
                break
            else:
                print("Hatalı İşlem Seçimi")


