"""
1400 yıl önce savaşmayı çok seven Krala SATRANÇ öğreten Yüce Bilge şunu talep eder;

"Kralım sizden çok fazla şey istemem buğday verseniz yeter. bakın bu satranç
tahtası 64 kare. Birinci kareye bir buğday ikincisine 2, üçüncü kareye 4, 
dördüncü kareye 8 ve sonra hep böyle iki misli olacak 
şekilde her kareyi doldurmaya yetecek kadar buğday yeter" demiş.

SORU:

64 karenin hepsinin dolumu sonunda ne kadar buğday gerekli?

"""


karesayisi = 64
toplam = 0

for i in range(karesayisi):
    karedegeri = 2 ** i
    toplam += karedegeri

print(f"Bütün buğdayların toplamı: {toplam}")
