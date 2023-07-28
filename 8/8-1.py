sabit = 12500
sdeneyim = 100
scocuk = 250
smesai = 50

print("""
PersioN Hastanesi Maaş Hesaplama Programı 

""")

mesai =int(input("Lütfen bu ay yaptığınız mesai saatini giriniz: "))
deneyim = int(input("Lütfen işinizdeki deneyiminizi yıl olarak giriniz: "))
cocuk = int(input("Lütfen çocuğunuz var ise kaç çocuğunuz olduğunu giriniz(Yok ise 0 yazınız): "))

hesapmaas = sdeneyim*deneyim + scocuk*cocuk + smesai*mesai + sabit
print(f"Bu ay maaşınız {hesapmaas} TL olarak hesaplanmıştır.")