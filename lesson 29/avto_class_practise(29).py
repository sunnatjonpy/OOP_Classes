class Avto:
    """Avtomabil klasi"""
    def __init__(self,model,rang,yil,karobka,km,narx):
        """Avtomabilning xususiyatlari"""
        self.model = model
        self.rang = rang
        self.yil = yil
        self.karobka = karobka
        self.km = km
        self.narx = narx
    def get_info(self):
        """Avtomabil haqida ma'lumot qaytaradi"""
        info = f"{self.rang} {self.model} {self.karobka} karobka. "
        info+= f"km: {self.km}, yil: {self.yil}, narxi: {self.narx}"
        return info
    def update_km(self,kilometr):
        """Avtomabil kmni o'zgartiradi"""
        self.km+=kilometr

class Avto_Manzil:
    """AVtosalon manzili uchun klas"""
    def __init__(self,viloyat,tuman,mahalla,kocha,uy):
        """Manzil xususiyatlari"""
        self.vil = viloyat
        self.tum = tuman
        self.mah = mahalla
        self.koch = kocha
        self.uy = uy
    def get_manzil(self):
        """Avtomabil manzilini qaytaradi"""
        info = f"{self.vil} viloyati, {self.tum} tumani "
        info += f"{self.mah} mahallasi, {self.koch} ko'chasi, {self.uy}-uy"
        return info
class Avtosalon:
    """Avtosalon klas"""
    def __init__(self,name,manzil,sotuvda):
        """Avtosalon xususiyatlari"""
        self.name = name
        self.manzil = manzil
        self.sotuv = sotuvda
        self.avtolar = []
    def add_avto(self,avto):
        """Avtosalonga avtomabillar qoshish"""
        self.avtolar.append(avto)
    def see_avto(self):
        """Qo'shilgan avtomabillarni ko'rish"""
        royxat = []
        for avto in self.avtolar:
            royxat.append(avto.get_info())
        return royxat
    def get_manzil(self):
        """Avtosalon manizlini korish"""
        return self.manzil.get_manzil()
    
avto1 = Avto("Malibu","Qora",2007,"avtomat",1000,"$20000") #1-obyekt
avto2 = Avto("Gentra","Oq",2010,"avtomat",1020,"$10000") #2-obyekt
avto1_manzil = Avto_Manzil("Sirdaryo","Oqoltin","Yangiyer","Yangiyo'l",5) #Avtosalon klasiga manzil olish uchun yangi obyekt
avtosalon = Avtosalon("UzAutoMotors",avto1_manzil,"Mavjud emas") #Avtosalon obyekti