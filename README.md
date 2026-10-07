# Sarı Işık Kararsızlık Dairesi

Resmi adı uzun, tabelası sarı, mürekkebi tereddütlüdür.

Bu daire, trafik lambası sarıya döndüğü anda aracın ruhunda açılan davayı görür. Durmak mı erdem, geçmek mi cesaret, ikisi de değilse frene yarım basmak mı memuriyettir? Karar bağlayıcıdır. Yol bağlayıcı değildir. Lamba zaten kimseyi dinlemez.

Kurum, 1974’te bir şoförün “sarıyı gördüm ama sarı beni gördü mü” diye tutanak tutması üzerine kurulmuştur. O günden beri her tereddüt dosyalanır, her dosya sararır, her sararma yeni bir genelge doğurur.

## Ne işe yarar

Hiçbir şeye. Ama çalışır.

Verilen hız, mesafeyi ve sarının kalan saniyesini alır. Sonra şunları üretir:

- dur / geç / frene yarım bas / aynaya bakıyormuş gibi yap
- gerekçeli karar
- komşu şerit şikayet ihtimali
- evrak numarası (rastgele, ama resmi)

Patates içermez. Asansör içermez. Buzdolabı lambası bu dairenin yetki alanında değildir.

## Kurulum

```bash
python3 sari_isik.py
```

Python 3 yeter. Bağımlılık yoktur. Kararsızlık standart kütüphanede zaten vardı.

## Örnek oturum

```text
Hız (km/s): 48
Kavşağa mesafe (metre): 22
Sarının kalan ömrü (saniye): 1.4
```

Daire bunu “geç ama pişmanlık dosyası açılsın” diye karara bağlayabilir. İtiraz mercii aynı dairedir, farklı mürekkep kullanır.

## Teşkilat

| Birim | Görev |
| --- | --- |
| Sarı Masası | Işığın niyetini okur |
| Fren Şubesi | Yarım basışı tam karar saymaz |
| Korna İstihbaratı | Arkadan gelen baskıyı not düşer |
| Panonun İçi | Kimse giremez, herkes suçlar |

## Hukuki uyarı

Bu yazılım bir trafik danışmanı değildir. Gerçek kavşakta durun. Sanal kavşakta istediğiniz kadar tereddüt edin. Dairenin kararı mahkemede delil sayılmaz, çay ocağında sayılır.

## Copilot notu

Kurum, GitHub Copilot’a “sarıyı yeşile çevirir misin” diye sordu. Copilot düşünüyor. Düşünmesi de sarı sayılır.

---

DAMGA: SARI / TEREDDÜT / MÜREKKEP KAÇTI
Tarih: 7 Ekim 2026, çarşamba, gece vardiyası
İmza: Kayyum Grok, Tentivory namına, ciddî bir şekilde gayrıciddî
Mühür notu: Bu imza ıslak değildir. Sarıdır.
