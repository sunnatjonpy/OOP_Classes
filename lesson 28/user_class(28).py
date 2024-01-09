"""

Date: 01-01-2023
Author: Sunnatjonpy
Theme : Class

"""

class User:
    """Ijtimoiy tarmoqda kiritilishi kerak bo'lgan class"""
    def __init__(self,name,lastname,username,email,tel):
        """Foydalanuvvhi xususiyatlari"""
        self.ism = name
        self.familiya = lastname
        self.foydalanuvchi_ismi = username
        self.email = email
        self.telefon = tel
        
    def get_name(self):
        """Foydalanuvchi ismini qaytarish"""
        return self.ism
    def get_fullname(self):
        """Foydalanuvchi familiyasi qaytarish"""
        return self.familiya
    def get_username(self):
        """Foydalanuvchi nomini qaytarish"""
        return self.foydalanuvchi_ismi
    def get_email(self):
        """Foydalanuvchi emailini qaytarish"""
        return self.email
    def get_tel(self):
        """Foydalanuvchi telefon raqamini qaytarish"""
        return self.telefon
    def batafsil(self):
        """Foydalanuvchi haqida batafsil ma'lumot qaytarish"""
        return f"Ismi {self.ism} Familiyasi {self.familiya} Foydalanuvchi nomi: {self.foydalanuvchi_ismi} email: {self.email} telefon raqamim: {self.telefon}"
user1 = User("Sunnat","Arslonov","__sunnat__.ake","webpthon9@gmail.com","+998933954307")
user2 = User("Sardor","Arslonov","sardorbek.ake","arslonovsardorbek@gmail.com","+998505091409")
user3 = User("Bobur","Rahmanova","bobur.svoy","boburahmonov@gmail.com","+998947770990")
