class hgs():
    def __init__(self,hgs_no,ad_soyad,sinif,bakiye):
        self.hgs_no = hgs_no
        self.ad_soyad = ad_soyad
        self.sinif = sinif
        self.bakiye = bakiye

    def hgsno(self):
        print('''Hgs No: {0}
        Surucu Adi / Soyadi: {1}
        Arac Sinifi: {2}
        Bakiye Bilgisi: {3}      
        ''').format(self.hgs_no,self.ad_soyad,self.sinif,self.bakiye)


class gise(hgs):
    def __init__(self,hgs_no,ad_soyad,sinif,bakiye,tarih,giris,cikis):
        hgs.__init__(self,hgs_no,ad_soyad,sinif,bakiye)
        self.tarih = tarih
        self.giris = giris
        self.cikis = cikis

    def kilometre(self,giris,cikis):
        location = {'seferihisar':0,'urla':9.4,'karaburun':18.2,'zeytinler':30.6,'alacati':47.5,'cesme':56.3}
        distance = abs(location[giris] - location[cikis])
        return distance

    def odeme(self,sinif,kilometre):
        if sinif == 'sinif1':
            return kilometre*0.25
        elif sinif == 'sinif2':
            return kilometre*0.30
        elif sinif == 'sinif3':
            return kilometre*0.40



class sinif1(hgs):
    def __init__(self,hgs_no,ad_soyad,sinifi,bakiye):
        hgs.__init__(self,hgs_no,ad_soyad,sinifi,bakiye)

    def hesaplama(self):
        yol = gise.kilometre(gise.giris,gise.cikis)
        return yol*0.25


class sinif2(hgs):
    def __init__(self,hgs_no,ad_soyad,sinifi,bakiye):
        hgs.__init__(self,hgs_no,ad_soyad,sinifi,bakiye)

    def hesaplama(self):
        yol = gise.kilometre(self,gise.giris,gise.cikis)
        return yol*0.30


class sinif3(hgs):
    def __init__(self,hgs_no,ad_soyad,sinifi,bakiye):
        hgs.__init__(self,hgs_no,ad_soyad,sinifi,bakiye)

    def hesaplama(self):
        yol = gise.kilometre(self,gise.giris,gise.cikis)
        return yol*0.40


a = gise(1,'Emre','1.sinif',45,'10.3.2018','seferisar','urla')

print(a.kilometre('karaburun','zeytinler'))