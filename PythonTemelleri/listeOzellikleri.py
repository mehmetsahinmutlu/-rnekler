# liste1 = [12,23,43]
# liste2 = liste1
# liste2[2] = "Hello"
# print(liste1)

# liste1 = [12,23,43]
# liste2 = liste1.copy()
# liste2[2] = "Hello"
# print(liste2)
# print(liste1)

liste1 = [12,23,43]
liste = [1,2,3,3]

liste1.append(liste)
print(liste1)

liste1.extend(liste)
print(liste1)

# a = 12
# b = a
# b = 6
# print(a)