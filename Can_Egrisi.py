import math

alfabe="abcçdefgğhıijklmnoöprsştuüvyz ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

okullist = list(); vizefinal = list(); ortalama = list(); notlar = list()
kisisayisi = int(); toplam = int(); aritmetikort = int() ; kalan_ogren = 0
sapmatoplam = int(); sapma = int(); sinif = int(); gecen_ogren = 0


#Toplam Sinif Mevcudu
while True:
    try:
        kisisayisi = int(input('Sinif Mevcudunu Giriniz: '))
        if kisisayisi < 1:
            print('Doğru Bir Değer Girilmedi.')
            continue    #kisi sayisi 1 den az olamayacagina gore tekrar deger istiyoruz.
        break

    except ValueError:  #yanlis deger hatasi buraya dusuyor
        print('Tam Sayi Giriniz.')
        continue


#Ogrenci Bilgileri
sinif = 0
while True:
    try:
        kontrol = False
        adsoyad = input("Öğrenci Adını ve Soyadını Giriniz: ")
        for a in adsoyad:
            if a not in (alfabe): #girilen ad ve soyadi alfabe de izin verilen harfler ile karsilastiriyoruz.
                kontrol = True #eger yanlis bir karakter varsa kontrolumuz true oluyor ve if bloguna duserek hata verip tekrar deger istiyor.
        if kontrol == True:
            print("Ad Soyad Sayısal Karakter İçeremez...")
            continue

        ogrencino = int(input("Öğrenci Numarasını Giriniz 3 Hane: "))
        if ogrencino > 999 or ogrencino < 100: #ogrenci numarasini 3 hane olarak aliyoruz. aksi halde tekrar deger istiyoruz.
            print("Doğru Bir Numara Girilmedi...")
            continue

    except: #olasi farkli hatalari engellemek icin
        print("Beklemeyen Bir Hata Oluştu!")
        continue

    okullist.append((adsoyad, ogrencino))   #okuldaki ogrencilerin adi, soyad ve numaralarini bir listeye atiyoruz.

    sinif += 1
    if kisisayisi == sinif:  #kisisayisi tamamlandiginda donguden cikiyoruz.
        break


#Vize ve Final Notu Alma
sinif = 0   #tekrar kisisayisi ile karsilastirma yapabilmek icin 0 liyoruz. aksi halde dongu eksik kalir.
while True:
    try:
        print('Ogrenci Adi Soyadi / Numarasi: ',okullist[sinif]) #hangi ogrencinin notunu girecegimizi belirten bir cikti veriyoruz.
        vize = int(input("Ögrenci Vize Notu: "))
        if vize < 0 or vize > 100:      #girilen degerin 0-100 arasi oldugunu onaylatiyoruz aksi halde tekrar istiyoruz.
            print("0-100 Arasında Bir Sayi Giriniz...")
            continue
        final = int(input("Öğrenci Final Notu: "))
        if final < 0 or final > 100:    #benzer sekilde final notunu da hesapliyoruz ve ayni kontrolleri uyguluyoruz.
            print("0-100 Arasında Bir Sayi Giriniz...")
            continue

    except ValueError:  #try except ile deger hatasinin onune geciyoruz.
        print("Yanlış Bir Değer Girildi!")
        continue
    vizefinal.append((vize, final)) #ogrenci notlarini ayri bir listeye aliyoruz.

    sinif += 1
    if kisisayisi == sinif: #kisisayisi ile tekrar karsilastirma yapiyoruz ve herkesin notlari girildikten sonra dongu sonlaniyor.
        break


#Standart Sapma ve Ortalama Hesaplama
for i, j in vizefinal:
    ortalama.append(i*40/100 + j*60/100) #her ogrencinin vize ve final ortalamasini alip ayri bir listeye atiyoruz. islemlerimizi kolaylastirmak icin.

for i in ortalama:  #ogrencilerin not ortalamalarini topluyoruz.
    toplam += i

aritmetikort = toplam/kisisayisi  #aritmatik ortalamayi bulmak icin ortalama toplamini kisi sayisina boluyoruz.

for i in ortalama:
    sapmatoplam += ((i - aritmetikort)*(i - aritmetikort))  #sapma formulu geregi, ortalamalari tek tek artimatik ortalamadan cikartip karesini alip toplamini buluyoruz.

sapma = math.sqrt(sapmatoplam/(kisisayisi-1))  #sapmaortalamasini kisi sayisinin 1 eksigine bolup karekokunu aliyoruz.

if sapma > 10:  #eger sapma yuksek cikarsa bir ust limit koyuyoruz. bu ogrencilere yapilabilecek max torpil degeri olarak belirledik.
    sapma = 10

#Gecme Notu Harf Hesaplamasi ve Kalan / Gecen Ogrenci Sayisi
for i in ortalama:
    if i > aritmetikort + (4*sapma): #ogrenci ortalamalarina (vize/final) sinif ortalamasi ve sapmayi ekleyerek uygun notlari veriyoruz.
        notlar.append('AA')
        gecen_ogren += 1
    elif i > aritmetikort + (3*sapma):
        notlar.append('BA')
        gecen_ogren += 1
    elif i > aritmetikort + (2*sapma):
        notlar.append('BB')
        gecen_ogren += 1
    elif i > aritmetikort + (1*sapma):
        notlar.append('CB')
        gecen_ogren += 1
    elif i > aritmetikort:
        notlar.append('CC')
        gecen_ogren += 1
    elif i > aritmetikort - (1*sapma):
        notlar.append('DC')
        gecen_ogren += 1
    elif i > aritmetikort - (2*sapma):
        notlar.append('DD')
        gecen_ogren += 1
    else:
        notlar.append('FD')
        kalan_ogren += 1


#Sinifin Genel Durumu
print('''*******************************    
          -- Meraklisi icin Detaylar --
Ogrenci Sayisi: {0}
Kalan Orenci Sayisi: {1}
Gecen Ogrenci Sayisi: {2}
Can Egrisi & Standart Sapma: {3} --- {4}

*******************************
'''.format(kisisayisi,kalan_ogren,gecen_ogren,aritmetikort,sapma)) #Genel bilgileri yazdiriyoruz. sinif ile ilgili istatistikler.


#Siniftaki Ogrencilerin Dokumu
sec = input('Sinif Listesini Goruntulemek Istiyor Musunuz [`E`/`H`] ? ') #istege bagli olarak tum sinifin detayli bir dokumunu cikartiyoruz.
if sec == 'e' or sec == 'E':
    for i in range(kisisayisi):
        print('''--------------------------------------------------------------------------------
        Ogrenci Adi Soyadi: {0}  /  Numarasi: {1}  /  Ortalamasi: {2}  /   Harf Karsiligi: {3}
        '''.format((okullist[i][0]), (okullist[i][1]), ortalama[i], notlar[i]))









