from oopDosya import KayitIslem

kayit = KayitIslem("Banka","Tutar","Gun",dosyaYolu=r"D:\Hesap")
kayit2 = KayitIslem("Musteri","Tutar",dosyaYolu=r"D:\Takip")
kayit.KayitEkle()
kayit2.KayitEkle()