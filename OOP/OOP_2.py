class HarfSayaci:

    def __init__(self):
        self.sesli_harf = "aeiıoüuö"
        self.sessiz_harf = "qwrtypğsdfghjklşzxcvbnmç"
        self.turkce = "üğışçö"
        self.sesli_sayac = 0
        self.sessiz_sayac = 0
        self.turkce_sayac = 0
        self.kelime = ""

    def kelime_sor(self):
        return input("Bir kelime Girin")

    def seslidir(self,harf):
        return harf in self.sesli_harf

    def sessizdir(self,harf):
        return harf in self.sessiz_harf

    def turkcedir(self,harf):
        return harf in self.turkce

    def arttır(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sesli_sayac += 1
            if self.sessizdir(harf):
                self.sessiz_sayac += 1
            if self.turkcedir(harf):
                self.turkce_sayac += 1
        return (self.sessiz_sayac,self.sesli_sayac,self.turkce_sayac)

    def ekrana_bas(self):
        sayim = self.arttır()
        mesaj = "{} kelimesinde {} sesli harf ve {} sessiz harf, {} türkçe karakter vardır."
        print(mesaj.format(self.kelime,sayim[1],sayim[0],sayim[2]))

    def çalıştır(self):
        self.kelime = self.kelime_sor()
        self.ekrana_bas()

if __name__ == '__main__':
    sayac = HarfSayaci()
    sayac.çalıştır()
