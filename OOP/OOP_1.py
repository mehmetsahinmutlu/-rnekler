class Kedi:
    familya = "felis"
    def __init__(self,ad="",tuy="",goz="",renk=""):
        self.tuy = tuy
        self.goz = goz
        self.ad = ad
        self.renk = renk
    def beslenme(self):
        self.miyavla()
        print(self.ad,"Beslendi")
    def miyavla(self):
        print(self.ad,"Miyavladı")




Duman = Kedi(ad="Duman",tuy="Kısa",goz="yesil",renk="Gri")
print(Duman.goz)
Duman.beslenme()
Melek = Kedi()
Melek.ad = "Melek"
Melek.beslenme()