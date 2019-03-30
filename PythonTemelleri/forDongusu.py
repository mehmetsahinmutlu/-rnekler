# liste = [25,85,74,96,35,14,25,65,74]
# sayac = 0
# for i in range(0,len(liste)):
#     if liste[i] > 50:
#         sayac += 1
# print(sayac)
# sayac = 0
# for item in liste:
#     if item > 50:
#         sayac+=1
# print(sayac)
# sayac = 0
# metin = "Fıstıkçı Şahap"
# alfabe = "abcdefghijklmnopqrstuvwxyz"
# for kar in metin:
#     # if not (kar.lower() in alfabe):
#     #     sayac += 1
#     if kar.lower() in alfabe:
#         pass
#     else:
#         sayac += 1
# print(sayac)

# sayac = 0
# metin = "Fıstıkçı Şahap"
# alfabe = "abcdefghijklmnopqrstuvwxyz"
# for kar in metin:
#     # sayac += 1
#     if not (kar.lower() in alfabe):
#         print(" {} adımda for durdu".format(sayac))
#         break
#     sayac += 1

# print(sayac)
# sayac=0
# while True:
#     sayac+=1
#     print(sayac)

import random

sayi = random.randint(0, 100)
print(sayi)
for i in range(1, 7):
    tahmin = int(input("Sayıyı Tahmin Et"))
    if tahmin > sayi:
        print("Aşağıkalan hak {}".format(6 - i))
    elif tahmin < sayi:
        print("Yukarı kalan hak {}".format(6 - i))
    elif tahmin == sayi:
        print("Tebrikler {} tahminde buldun".format(i))
        break
    if i == 6:
        print("Hakkınız Bitti")


