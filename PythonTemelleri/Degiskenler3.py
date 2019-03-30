liste = [1,2.3,1+3j,"asdsa",[123,23],(23,3),{"ali":"Abi"}]
print(liste)
liste[3] = "www.ibrahimediz.com"
liste[3] = [12,32,12]
print(liste)

matris2 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
matris3  = [[[1,2,3],[4,5,6],[7,8,9],[10,11,12]],[[13,14,15],[16,17,18],[19,20,21],[22,23,24]],]

a,b,c = matris2[0]
print(len(matris3[0][1]))
liste = [1]
liste.append("ali")
# append eleman ekler 
liste.insert(1,"deneme")
# indis numarasına göre eleman ekler
liste.append("8 den sonra mı öncemi ")
print(liste.pop(2))
print(liste.index("deneme"))
print(liste)

liste2 = [2]

liste2 += liste
# + birleştirir
print(liste2)


