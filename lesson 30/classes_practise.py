# Date : 10-01-2024
# Author: Sunnatjonpy

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
class Professor(Shaxs):
    "Professor class"
    def __init__(self,ism,familiya,passport,tyil,unvon,idd):
        super().__init__(ism, familiya, passport, tyil)
        self.unvon = unvon
        self.idd = idd
        
    def get_unvon(self):
        """Professor unvoni"""
        return self.unvon
    def get_idd(self):
        """Professor id raqami"""
        return self.idd 
    def get_info(self):
        """Professor haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan. "
        info += f"Unvon: {self.unvon}, ID: {self.idd}"
        return info
    def ban_user(self,shaxs):
        """Professor foydalanuvhcini bloklash qismi"""
        return f"Foydalanuvchi :{shaxs.get_name()} bloklandi!"
        
class Professor_yordamchi(Professor):
    """Professor yordamchisi class"""
    def __init__(self,ism,familiya,passport,tyil,unvon,idd,maosh):
        """Voris classga qoshimcha atributelar"""
        super().__init__(ism,familiya,passport,tyil,unvon,idd)
        self.money = maosh
    def get_info(self):
        """Professor yordamchisi haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.tyil}-yilda tug`ilgan. "
        info += f"Unvon: {self.unvon}, ID: {self.idd} maosh: {self.money}"
        return info

class Talaba:
    """Talaba class"""
    def __init__(self,ism,familiya,ota_ism):
        self.ism = ism
        self.familiya = familiya
        self.ota_ism = ota_ism
        self.fanlar = []
		
    def get_name(self):
        """Talaba ismi"""
        return self.ism
    def get_lastname(self):
        """Talaba familiyasi"""
        return self.familiya
    def get_otaism(self):
        """Talaba otasining ismi"""
        return self.ota_ism
    def get_surname(self):
        """Talaba ism-familiyasi"""
        return f"{self.ism} {self.familiya}"
    def get_ismtoliq(self):
        """Talabaning ism-familiya-otasining ismi"""
        return f"{self.ism} {self.familiya} {self.ota_ism}"
    def fanga_yozil(self,nom):
        """Fanga yozilish"""
        self.fanlar.append(nom)
    def remove_fan(self,fan_nom):
        """Fanni o'chirish"""
        if fan_nom in self.fanlar:
            self.fanlar.remove(fan_nom)
        else:
            return f"Siz {fan_nom} faniga yozilmagansiz!"
            
    def get_fanlar(self):
        """Fanlarni ko'rish"""
        subjects = []
        for fan in self.fanlar:
            subjects.append(fan.get_name())
        return subjects
class Fan:
    """Fan class"""
    def __init__(self,name):
        """Fanga tegishli xususiyatlar"""
        self.name = name
        self.talabalar = []
    def get_name(self):
        """Fan nomi"""
        return self.name
talaba1 = Talaba("Shahzod","Omonov","Habibulla o'g'li")
talaba2 = Talaba("Zarnigor","Do'stbekova","Rahmatulla qizi")

fan1 = Fan("Informatika")
fan2 = Fan("Adabiyot")

talaba1.fanga_yozil(fan1)
talaba1.fanga_yozil(fan2)

professor1 = Professor("Sunnatjon", "Arslonov", "AAF234NM", 2007, "Master", "bc12b2-sbf2j3-djjs23")
professor_helper1 = Professor_yordamchi("Sardor","Arslonov","AAF42BDBF",2009,"Manager","23dafdf-2sdse3-fdwwr3","$1000")