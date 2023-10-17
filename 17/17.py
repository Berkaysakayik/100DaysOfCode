import tkinter as tk
from PIL import Image, ImageTk
import random
import os

# Fotoğraf dosyalarının isimleri ve değerleri
foto_isimleri = {'1.png': 1, '2.png': 2, '3.png': 3, '4.png': 4, '5.png': 5, '6.png': 6}

# Dosya yolunu kontrol eden fonksiyon
def kontrol_et(foto_ad):
    dosya_yolu = os.path.join(os.path.dirname(__file__), foto_ad)
    if os.path.exists(dosya_yolu):
        return dosya_yolu
    else:
        return None

# Bilgisayardan rastgele tahmin alma fonksiyonu
def bilgisayar_tahmini():
    return random.randint(1, 6)

# Rastgele bir fotoğraf dosyası seçme fonksiyonu
def rastgele_fotograf_sec():
    return random.choice(list(foto_isimleri.keys()))

# Kullanıcı ve bilgisayar tahminlerine göre oyunun kazananını belirleme fonksiyonu
def kazanan_belirle(kullanici_tahmini, bilgisayar_tahmini):
    en_yakin_kullanici = en_yakin_fotograf(kullanici_tahmini)
    en_yakin_bilgisayar = en_yakin_fotograf(bilgisayar_tahmini)

    if en_yakin_kullanici == en_yakin_bilgisayar:
        return "Berabere"
    elif abs(foto_isimleri[en_yakin_kullanici] - kullanici_tahmini) < abs(foto_isimleri[en_yakin_bilgisayar] - bilgisayar_tahmini):
        return "Kullanıcı"
    else:
        return "Bilgisayar"

# Kullanıcının tahminine en yakın fotoğrafı bulma fonksiyonu
def en_yakin_fotograf(tahmin):
    en_yakin_foto = min(foto_isimleri, key=lambda x: abs(foto_isimleri[x] - tahmin))
    return en_yakin_foto

# Oyunu başlatma fonksiyonu
def oyun():
    kullanici_tahmini = int(entry.get())
    bilgisayar_tahmin = bilgisayar_tahmini()

    secilen_foto_ad = rastgele_fotograf_sec()  # Sadece dosya adını alın, dosya yolu değil
    secilen_foto_yolu = kontrol_et(secilen_foto_ad)

    if not secilen_foto_yolu:
        print(f"Dosya yolu bulunamadı: {secilen_foto_ad}")
        return

    bilgisayar_tahmin_label.config(text=f"Bilgisayarın tahmini: {bilgisayar_tahmin}")
    secilen_foto = ImageTk.PhotoImage(Image.open(secilen_foto_yolu))
    secilen_foto_label.config(image=secilen_foto)
    secilen_foto_label.image = secilen_foto

    kazanan = kazanan_belirle(kullanici_tahmini, bilgisayar_tahmin)
    sonuc_label.config(text=f"Kazanan: {kazanan}")

# Arayüz oluşturma
root = tk.Tk()
root.title("Fotoğraf Tahmin Oyunu")

label = tk.Label(root, text="1 ile 6 arasında bir tahmin yapın (1 ve 6 dahil):")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Tahmin Et", command=oyun)
button.pack(pady=10)

bilgisayar_tahmin_label = tk.Label(root, text="")
bilgisayar_tahmin_label.pack(pady=5)

secilen_foto_label = tk.Label(root)
secilen_foto_label.pack(pady=10)

sonuc_label = tk.Label(root, text="")
sonuc_label.pack(pady=5)

root.mainloop()
