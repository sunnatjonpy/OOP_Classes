# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 21:40:32 2024

@author: Sunnatjonpy

class Talaba:
    """Talaba class"""
    def __init__(self,ism,familiya,ota_ism,tyil):
         self.ism = ism
         self.familiya = familiya
         self.ota_ism = ota_ism
         self.t_yil = tyil
         self.bosqich = 1
  
    def get_name(self):
        return self.ism
    def get_lastname(self):
        return self.familiya
    def get_otaism(self):
        return self.ota_ism
    def get_surname(self):
        return f"{self.ism} {self.familiya}"
    def get_ismtoliq(self):
        return f"{self.ism} {self.familiya} {self.ota_ism}"
    def get_toliq(self):
        return f"{self.ism} {self.familiya} {self.ota_ism} {self.t_yil}-yilda tug'ilgan va u hozir {2024-self.t_yil} yoshda."


class Fan:
    def __init__(self,nom):
        self.nom = nom
        self.talabalar = []
        self.talabalar_soni = 0
    def get_name(self):
        return f"Fan nomi : {self.nom}"
    def add_student(self,talaba):
        if talaba not in self.talabalar:
            self.talabalar.append(talaba)
            self.talabalar_soni +=1        
    def get_student(self):
        royxat = []
        for talaba in self.talabalar:
            royxat.append(talaba.get_ismtoliq())
        return royxat
    #return [talaba.get_ismtoliq() for talaba in self.talabalar]
    def get_talabasoni(self):
        return f"Talabalar soni: {self.talabalar_soni} ta"
fan1 = Fan("Ingliz-tili")
talaba1 = Talaba("Shahzod","Omonov","Habibulla o'g'li",1998)
talaba2 = Talaba("Zarnigor","Do'stbekova","Rahmatulla qizi",2007)
def see_methods(klas_nomi):
    """Kiritgan Classga tegishli metod va xususiyatlarni chiqaruvchi funksiya"""
    funk = []
    for method in dir(klas_nomi):
        if "__" not in method:
            funk.append(method)
    return funk
    #nomalum [if "__" not in method for method in dir(klas_nomi)]
"""

class Avto:
    def __init__(self,model,rang,karobka,yil,narx,km=0):
        self.model = model
        self.color = rang
        self.box = karobka
        self.year = yil
        self.cost = narx
        self.km = km
    def avto_info(self):
        info = f"{self.color} {self.model} {self.box} karobka"
        info+= f"{self.year}-yil narxi: {self.cost} km: {self.km}"
        return info
avto1 = Avto("Malibu","Qora","Mexanika",2020,"15000$",15000)