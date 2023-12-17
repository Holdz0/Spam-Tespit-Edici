def spamtespit():
    with open("spamm.txt","r+",encoding="utf-8") as spamtes:       
        icerik = spamtes.read()
        satırlar = icerik.split("\n")       
        return satırlar
def girisyazma():
    with open("girisler.txt","a",encoding="utf-8")as girisleryaz:
        girisleryaz.write(giris+"\n")
def girisliste():
     with open("girisler.txt","r+",encoding="utf-8")as girisleryaz:
        icerik = girisleryaz.read()
        satırlar = icerik.split("\n")
        return satırlar
def spammesajlar():
    with open("spam_mesajlar.txt","a",encoding="utf-8")as spammesaj:
        spammesaj.write(giris+"\n")

while True:
   
    giris = input("Yazı Girin : ")
    uzunluk = len(spamtespit())
    print(uzunluk)
    sayac2 = 0
    for i in range(0,uzunluk):  
        yazi = spamtespit()[i]
        sayac = giris.count(yazi)
        sayac2 += 1
        if sayac == 1:
            print("spam")
            spammesajlar()
            break
    if sayac2 == uzunluk:
        girisyazma()
    
        


      

    
                  


    
    
