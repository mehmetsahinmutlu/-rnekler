# from oopDosya import KayitIslem
# kayit = KayitIslem("Adı",dosyaYolu=r"D:\Varsayilan")

class MarvelHero():
    tanimli = []
    def __init__(self,ad=""):
        self.yetenekleri = []
        self.unvani = ""
        self.gezegen = ""
        self.saglik = 100
        self.guc = 10
        self.ad = ad
        self.tanimli.append(ad)
        self.Selamlama()
    
    def Darbe(self):
        self.saglik -= 10
        print(self.saglik)
    
    def Vurus(self):
        print(self.guc,"kadar vurdu")
    
    def Selamlama(self):
        print("Merhaba benim adım ",self.ad)

    @classmethod
    def Liste(cls):
        print(cls.tanimli)

    @staticmethod
    def Pi():
        return 22/7


class DeadPool(MarvelHero):
    def __init__(self):
        super().__init__("Deadpool")
        self.yetenekleri.append("Çabuk İyileşme")

class CaptainMarvel(MarvelHero):
    def __init__(self):
        super().__init__("CaptainMarvel")
        self.yetenekleri.append("Silaha İhtiyacı Yok")
    
class CaptainAmerica(MarvelHero):
    def __init__(self):
        super().__init__("CaptainAmerica")
        self.yetenekleri.append("Kalkan")

    def Darbe(self):
        self.saglik -= 5
        print(self.saglik)

    
# oyuncu1 = DeadPool()
# oyuncu1.Darbe()
# oyuncu2 = CaptainAmerica()
# oyuncu2.Darbe()
# print(oyuncu1.tanimli)

print(MarvelHero.Pi())