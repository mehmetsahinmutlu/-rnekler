# say = input("Kontrol etmek istediğiniz sayıyı giriniz")
# toplam = 0
# for i in say:
#     toplam += int(i)**(len(say))

# if toplam == int(say):
#     print("Armstrong Sayısı")


# def sayiKontrol(*args):
#     toplam = 0
#     sayi = ""
#     for i in args:
#         toplam += int(i)**(len(args))
#         sayi+=i
#     if toplam == int(sayi):
#         return True
#     else:
#         return False

# if sayiKontrol(*input("Kontrol etmek istediğiniz sayıyı giriniz")):
#     print("Budur")



# N = int(input("Bir Pozitif Tam Sayı Giriniz"))
# x=2
# while x<=N:
#     i = 2
#     while i*i<=x:
#         if x%i==0:
#             break
#         i += 1
#     else:
#         print(x)
#     x+=1

# def deneme(**kwargs):
#     for key,value in kwargs.items():
#         if key == "Isim":
#             if value == "Soner":
#                 print("Sen gonuşma Sonner")
#                 break

# def calc_factorial(x):
#     """This is a recursive function
#     to find the factorial of an integer"""

#     if x == 1:
#         return 1
#     else:
#         return (x * calc_factorial(x-1))

# num = 4
# print("The factorial of", num, "is", calc_factorial(num))	



# def f1(param):
#     if len(param) >= 1:
#        f1(param[0:len(param)-1])
#        print(param)

# f1("Tripanazomigambiyetsiz")
# input("değişken tanımla")
# exec(input("değişken tanımla"))
# print(eval("25+30"))
# print(a)