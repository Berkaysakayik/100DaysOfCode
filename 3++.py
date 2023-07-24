ParkeEn  = 20
ParkeBoy = 110

SalonEn  = 600
SalonBoy = 300

OOEn     = 400
OOBoy    = 300

COEn     = 200
COBoy    = 300

YOEn     = 400
YOBoy    = 300

def parke_hesapla(en,boy):
    parkesayisi = (en*boy) // (ParkeEn*ParkeBoy)
    return parkesayisi

S = parke_hesapla(SalonEn,SalonBoy)
O = parke_hesapla(OOEn,OOBoy)
C = parke_hesapla(COEn,COBoy)
Y = parke_hesapla(YOEn,YOBoy)

total=S+O+C+Y
print(f"Yatak Odası : {Y}\nOturma Odası : {O}\nÇocuk Odası : {C}\nSalon: {S}\ntotalde {total} adet parke gerekli")