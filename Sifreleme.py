import random

sifreli_alfabe = list()
bit = int(); sifre_harf_str = str(); sifre_harf = int() ; sifreli_metin = str()

alfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZabcçdefgğhıijklmnoöprsştuüvyz "

while True:
    try:
        metin = input('Sifrelenmek Istenen Metni Giriniz: ')
        bit = int(input('Bit Sayisini Giriniz: '))
        break

    except:
        print('Beklenmeyen Bir Hata Olustu...')
        break

for i in alfabe:
    for j in range(bit):
        sifre_harf_str += str(random.randint(0,1))
        sifre_harf = int(sifre_harf_str)
    sifreli_alfabe.append((i,sifre_harf))

for i in metin:
    for j in range(len(alfabe)):
        if i == sifreli_alfabe[j][0]:
            sifreli_metin += str(sifreli_alfabe[j][1])

i = 0; j = 0
while True:
    print(sifreli_metin[i:i+50])
    i += 50
    j += 1
    if bit*len(metin)+1 == j:
        break
print(sifreli_alfabe)