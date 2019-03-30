# liste = [[2,3,4],[1,2,3],[2,4,5],[7,8,5]]
# print(liste)
# print("_"*8)
# for a,b,c in liste:
#     print("| {},{},{} |".format(a,b,c))
# print("_"*8)

alfabe = "abcçdefgğhıijklmnoöpqrstuvwyz"

# cevrim = {i : alfabe.index(i) for i in alfabe }
# # print(cevrim)
# print(cevrim.items())

# for key,value in cevrim.items():
#     print(key,value)


import random
liste=  [random.randint(0,10000000) for i in range(0,80)]
print(liste)

# liste = []
# for i in range(0,80):
#     liste.append(random.randint(0, 1000))
# print(liste)

