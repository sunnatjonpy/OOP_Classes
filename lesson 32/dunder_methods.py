# Date 13-01-2024
# Author: Sunnatjonpy


from uuid import uuid4
class Talaba:
    """Talaba class"""
    __talaba_soni = 0
    def __init__(self,ism,familiya,ota_ism,tyil,bosqich):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.ota_ism = ota_ism
        self.t_yil = tyil
        self.bosqich = bosqich
        self.__id = uuid4()
        Talaba.__talaba_soni +=1
        
    def __repr__(self):
        return f"{self.familiya} {self.ism}"
    def __lt__(self,object2):
        qiymat = self.bosqich<object2.bosqich
        if qiymat==True:
            return f"{self.ism}ning kursi {object2.ism}nikidan kichik ({self.bosqich}<{object2.bosqich})"
        else:
            return f"{self.ism}ning kursi {object2.ism}nikidan katta.({self.bosqich}>{object2.bosqich})"
    def __eq__(self,object2):
        qiymat = self.bosqich==object2.bosqich
        if qiymat==True:
            return f"{self.ism}ning kursi {object2.ism}ning kursi bilan teng ({self.bosqich}=={object2.bosqich})"
        else:
            return f"{self.ism}ning kursi {object2.ism}ning kursi bilan teng emas ({self.bosqich}!={object2.bosqich})"
        
    def get_name(self):
        """Talaba ismi"""
        return self.ism
    def get_lastname(self):
        """Talaba familiyasi"""
        return self.familiya
    def get_otaism(self):
        """Talaba otasining ismi"""
        return self.ota_ism
    def get_id(self):
        """Talaba ID raqami (inkapsulyatsiya)"""
    def get_bosqich(self):
        return self.bosqich
        return self.__id
    def get_surname(self):
        """Talaba ism-familiyasi"""
        return f"{self.ism} {self.familiya}"
    def get_ismtoliq(self):
        """Talaba ismi-familiyasi-otasining_ismi"""
        return f"{self.ism} {self.familiya} {self.ota_ism}"
    def get_toliq(self):
        """Talaba haqida to'liq ma'lumot"""
        return f"{self.ism} {self.familiya} {self.ota_ism} {self.t_yil}-yilda tug'ilgan va u hozir {2024-self.t_yil} yoshda."
    def set_bosqich(self):
        if self.bosqich+1>4:
            return "Qaytadan uruning!, Talaba kursini 4 dan oshirib bo'lmaydi"
        else:
            self.bosqich+=1
    
    @classmethod
    def get_talabasoni(cls):
        """Avto classi xususiyati"""
        return cls.__talaba_soni
    
    
talaba1 = Talaba("Shahzod","Omonov","Habibulla o'g'li",1998,2)
talaba2 = Talaba("Zarnigor","Do'stbekova","Rahmatulla qizi",2007,3)

class Fan:
    """Fan class"""
    def __init__(self,name):
        """Fanga tegishli xususiyatlar"""
        self.name = name
        self.talabalar = []
    def get_name(self):
        """Fan nomi"""
        return self.name
    def add_student(self,*students):
        for student in students:
            if isinstance(student,Talaba): 
                self.talabalar.append(student)
            else:
                print("Obyekt boshqa classga tegishli")   
    def __getitem__(self,index):
        return self.talabalar[index]
    
    def __setitem__(self,index,value):
        if isinstance(value,Talaba):
            self.talabalar[index]=value
    def __len__(self):
        return len(self.talabalar)
    
fan1 = Fan("Informartika")
fan1.add_student(talaba1,talaba2)
class Shaxs:
    """Shaxslar haqida ma'lumot"""
    __shaxs_soni = 0
    def __init__(self,ism,familiya,passport,tyil,):
        """Shaxs class xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.__passport = passport
        self.tyil = tyil
        self.__id = uuid4()
        Shaxs.__shaxs_soni+=1

    def get_pasport(self):
        """Shaxs passporti"""
        return self.__passport
    def get_id(self):
        """Shaxs ID raqami"""
        return self.__id
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
    @classmethod
    def get_shaxssoni(cls):
        """Shaxs class xususiyati"""
        return cls.__shaxs_soni
shaxs1 = Shaxs("Sardor","Arslonov","AAF783BHDA",2006)
shaxs2 = Shaxs("G'ayrat","Husanov","AAGHSU345B",2009)