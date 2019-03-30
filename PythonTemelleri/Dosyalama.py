try:
    dosya = open(r"D:\deneme.txt","r+")
    print("1.",dosya.read())
    print(dosya.tell())
    print("2.",dosya.read())
    dosya.seek(0)
    dosya.truncate()
    print("3.",dosya.read())
    dosya.write("Hüsnün senin ey dilberi nadide kamermi")
except:
    pass
finally:
    dosya.close()

input()


