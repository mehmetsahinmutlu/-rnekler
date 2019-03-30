sozluk = {"book":"kitap","apple":"elma"}

print(sozluk["book"])


alfabe = "abcçdefgğhıijklmnoöpqrstuvwyz"

cevrim = {i : alfabe.index(i) for i in alfabe }
print(cevrim)
print(cevrim.keys())
print(cevrim.values())
print(cevrim.items())

# isimlistesi = ["a","ı","b","ı","ç","o","ö"]
# sozluk = {}
# sozluk.
# sozluk = sozluk.fromkeys(isimlistesi)
# sozluk.clear()



# print(cevrim.get("o"))

# isimlistesi = ["ahmet","ışıl","berkecan","ışınsu","çisem","orçun","ömer"]
# isimlistesi.sort()
# print(isimlistesi)

# print(sorted(isimlistesi,key = lambda x : cevrim[x[0]]))