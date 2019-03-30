class MarvelHero():
    tanimli = []
    def __init__(self,ad=""):
        self.yetenekleri = []
        self.unvani = ""
        self.gezegen = ""
        self.tanimli.append(ad)

thor = MarvelHero("thor")
capamerica = MarvelHero("Kaptan Amerika")
capamerica.unvani = "Kaptan"
capamerica.yetenekleri.append("Kalkan")
thor.yetenekleri.append("Çekiç")
print(thor.yetenekleri)
print(capamerica.tanimli)
print(thor.tanimli)