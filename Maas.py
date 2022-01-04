# coding:utf8

# Puantaj tablosu


OCAK = MART = MAYIS = TEMMUZ = AĞUSTOS = EKİM = ARALIK = 31
NİSAN = HAZİRAN = EYLÜL = KASIM = 30
ŞUBAT = 28

hakedis = 0
agi = 152.21

p = []

# Personel bilgileri..
while True:
    try:
        pers = input('Personel Adı Soyadı : ')

        # isalpha() -> alfabe
        # isspace() -> boşluk
        if (not pers or (not all(c.isalpha() or c.isspace() for c in pers))):
            print('Personel adı soyadını boş geçemez ve içerisinde sayısal karakter kullanamazsınız!')
            continue

        break;

    except ValueError:
        print('Tip hatası oluştu lütfen değerleri kontrol ediniz!')
    except:
        print("Beklenmeyen bir hata oluştu!")

    # Doğum tarihi bilgileri..
while True:
    try:
        dyil = int(input('Doğum Tarihi : '))

        if (len(str(dyil)) != 4):
            print('Doğum tarihini 4 karakter olacak şekilde girmelisiniz!')
            continue
        else:

            if (dyil > 2018):
                print('Doğum tarihi 2018 yılından küçük olmalıdır!')
                continue

            dyil = (2018 - dyil)
            break

    except ValueError:
        print('Doğum tarihini sayısal bir değer şeklinde giriniz!')
    except:
        print("Beklenmeyen bir hata oluştu!")

# Medeni durumu ve cocuk sayısı bilgileri
while True:
    try:

        cocukdurum = 0
        medenidurum = input('Medeni Durumu (E/B) : ')

        if (medenidurum.lower() not in ('e', 'b')):
            print('Medeniz durumunu E veya B şeklinde giriniz!')
            continue
        else:
            if (medenidurum.lower() == 'e'):

                esdurum = input('Eşi çalışıyormu ? (E/H) : ')

                if (esdurum.lower() not in ('e', 'h')):
                    print('Eş çalışma durumunu E veya H şeklinde giriniz!')
                    continue
                else:
                    cocukdurum = int(input('Çocuk Sayısı : '))
                    if (cocukdurum == None): cocukdurum = 0
                    break
            else:
                break

    except ValueError:
        print('Tip hatası oluştu lütfen değerleri kontrol ediniz!')
    except:
        print("Beklenmeyen bir hata oluştu!")

    # İşe başlama tarihi bilgileri..
while True:
    try:
        isyil = int(input('İşe Başlama Tarihi : '))

        if (len(str(isyil)) != 4):
            print('İşe başlama tarihini 4 karakter olacak şekilde girmelisiniz!')
            continue

        isyil = (2018 - isyil)
        break

    except ValueError:
        print('İşe başlama tarihini sayısal bir değer şeklinde giriniz!')
    except:
        print("Beklenmeyen bir hata oluştu!")

# Net maaş bilgileri
while True:
    try:
        netmaas = float(input('Net maaş : '))

        if (netmaas < 1603.09):
            print('Asgari ücretten yüksek maaş girmelisiniz!')
            continue

        break

    except ValueError:
        print('Tip hatası oluştu lütfen değerleri kontrol ediniz!')
    except:
        print("Beklenmeyen bir hata oluştu!")

    # Yol ücreti ve yemek ücreti
while True:
    try:
        yol = float(input('Yol ücreti : '))
        yemek = float(input('Yemek ücreti : '))
        break

    except ValueError:
        print('Tip hatası oluştu lütfen değerleri kontrol ediniz!')
    except:
        print("Beklenmeyen bir hata oluştu!")

    # Yıllık izin hakkı
if (dyil < 50):

    if (isyil >= 1 <= 5):
        yiknt = 2
    elif (isyil >= 6 <= 14):
        yiknt = 4
    elif (isyil >= 15):
        yiknt = 6
    else:
        yiknt = 0

elif (dyil >= 50 <= 18):

    if (isyil >= 1 <= 5):
        yiknt = 4
    elif (isyil >= 6 <= 14):
        yiknt = 6
    elif (isyil >= 15):
        yiknt = 8
    else:
        yiknt = 0

# AGI
if (medenidurum == 'E'):

    if (esdurum == 'H'):
        if (cocukdurum == 0):
            agi = 182.66
        elif (cocukdurum == 1):
            agi = 205.49
        elif (cocukdurum >= 2):
            agi = 228.32

    else:
        if (cocukdurum == 1):
            agi = 175.04
        elif (cocukdurum >= 2):
            agi = 197.88

# Puantaj bilgileri
while True:
    try:

        i = 1
        yi = g = ht = ui = 0

        ay = eval("input('Hakediş puantaj ayını giriniz : ')")

        while i <= eval(ay):
            gun = input(str(i) + '. günü giriniz : ')

            if (gun not in ('G', 'HT', 'YI', 'UI')):
                print('Puantajı G, HT, YI, UI şeklinde girmelisiniz!')
                continue

            if (gun == 'G'):
                g += 1
            elif (gun == 'HT'):
                ht += 1
            elif (gun == 'UI'):
                ui += 1
            elif (gun == 'YI'):

                if (yi >= yiknt):
                    print('Personelin yıllık izin hakkı bitmiştir! Personelin yıllık izin hakkı {0} gündür..'.format(
                        str(yiknt)))
                    continue
                yi += 1

            p.insert(i, gun)
            i += 1

        break

    except ValueError:
        print('Tip hatası oluştu lütfen değerleri kontrol ediniz!')
    except:
        print("Beklenmeyen bir hata oluştu!")

_yol = float(yol * g)
_yemek = float(yemek * g)
_kesinti = ui * (netmaas / eval(ay))

print('\n\n{0} {1} ayı hakediş bilgileri..'.format(pers, ay))

print(50 * '-')
print('Maaş : {0} TL'.format(round(netmaas, 2)))
print('AGI : {0} TL'.format(round(agi, 2)))
print('Yol : {0} TL'.format(round(_yol, 2)))
print('Yemek : {0} TL'.format(round(_yemek, 2)))
hakedis = (netmaas + agi + _yol + _yemek) - _kesinti
print('Hakediş : {0} TL'.format(round(hakedis, 2)))
print(50 * '-')

print('\nG : Toplam {0} gün'.format(g))
print('HT : Toplam {0} gün'.format(ht))
print('YI : Toplam {0} gün yıllık izin kullanıldı.. Kalan yıllık izin {1} gün'.format(yi, yiknt - yi))
print('UI : Toplam {0} gün ücretsiz izin kullanıldı.. Kesinti tutarı {1} TL'.format(ui, round(_kesinti, 2)))

# Puantaj tablosu
print('\n\n')
x = PrettyTable([j for j in range(1, len(p) + 1)])
x.add_row(p)
print(x)