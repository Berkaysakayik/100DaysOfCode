import random

tkm = ["taş", "kağıt", "makas"]

Taş = tkm[0]
Kağıt = tkm[1]
Makas = tkm[2]

kullanici_skor = 0
bilgisayar_skor = 0

while True:
    girdi = input("taş, kağıt, makas, birini giriniz (Çıkmak için 'q' yazabilirsiniz): ")

    if girdi.lower() in ["q"]:
        break

    pc = random.choice(tkm)
    print(f"Rakibiniz {pc} seçti.")

    
    if girdi == Taş:
        
        if pc == Taş:
            print("Berabere!")
        elif pc == Kağıt:
            print("Kaybettiniz!")
            bilgisayar_skor += 1
        elif pc == Makas:
            print("Kazandınız!")
            kullanici_skor += 1
    
    elif girdi == Kağıt:
        if pc == Taş:
            print("Kazandınız!")
            kullanici_skor += 1
        elif pc == Kağıt:
            print("Berabere!")
        elif pc == Makas:
            print("Kaybettiniz!")
            bilgisayar_skor += 1
    
    elif girdi == Makas:
        if pc == Taş:
            print("Kaybettiniz!")
            bilgisayar_skor += 1
        elif pc == Kağıt:
            print("Kazandınız!")
            kullanici_skor += 1
        elif pc == Makas:
            print("Berabere!")

    print(f"Siz:  {kullanici_skor} - Bilgisayar: {bilgisayar_skor}")

    if kullanici_skor == 2:
        print("Oyun bitti! Kazanan Sizsiniz :)")
        break
    elif bilgisayar_skor == 2:
        print("Oyun bitti! Kazanan Bilgisayar :)")
        break