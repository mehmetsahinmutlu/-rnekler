def fonksiyon():
    print("Merhaba")
fonksiyon()

def carp(sayi=1,b=0):
    print(sayi*sayi)

# def topla(**kwargs):
#     a = 0
#     b= 0
#     c =0
#     for key,value in kwargs.items():
#         if key == "a":
#             a = value
#         if key == "b":
#             b = value
#         if key == "c":
#             c = value
#     print("{} + {} + {} = {}".format(a,b,c,a+b+c))


# topla(a=3,b=34)
liste = [20,85,74,51]

def ortalama(*args,katsayi=0):
    toplam = 0
    sonuc = ""
    for item in args:
        toplam += item
    return toplam/len(args)*katsayi,sonuc

print(ortalama(20,50,40,45,0,katsayi=4)[0]*5)





















