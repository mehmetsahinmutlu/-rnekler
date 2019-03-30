# import sqlite3 as sql
# db = sql.connect(r"D:\İbrahim EDİZ\23022019\Örnekler\IEDB.db")
# cursor = db.cursor()
# cursor.execute("SELECT * FROM V_HESAP")

def SozlukGetir(tabloid):
    import sqlite3 as sql
    db = sql.connect(r"D:\İbrahim EDİZ\23022019\Örnekler\IEDB.db")
    cursor = db.cursor()
    cursor.execute("SELECT sozluk_id,sozluk_adi FROM HSP_SOZLUK WHERE tablo_ID = {}".format(tabloid))
    liste = cursor.fetchall()
    return liste

def VeriEkle(sorgu):
    try:
        import sqlite3 as sql
        db = sql.connect(r"D:\İbrahim EDİZ\23022019\Örnekler\IEDB.db")
        cursor = db.cursor()
        cursor.execute(sorgu)
        db.commit()
        print("Kaydedildi")
    except:
        print("Hata var")
    finally:
        db.close()



for item,ay in SozlukGetir(2):
    print(item,"-",ay)
ayGiris = input("Ay Verisini Giriniz")
for item,ay in SozlukGetir(1):
    print(item,"-",ay)
KalemGiris = input("Kalem Verisini Giriniz")
TutarGiris = input("Tutarı Giriniz")


sorgu = """INSERT INTO HSP_BILGI (hsp_blg_kalem,hsp_blg_tutar,hsp_ay) 
values ({},{},{})""".format(KalemGiris,TutarGiris,ayGiris)
VeriEkle(sorgu)

