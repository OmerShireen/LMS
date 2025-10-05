class Person:
    def __init__(self, name, age, email, phone_no):
        self._name = name 
        self._age = age 
        self._email = email
        self._phone_no = phone_no        
     
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new):
        self._name = new

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new):
        self._age = new

    @property
    def email(self):
        return self._email 

    @email.setter
    def email(self, new):
        self._email = new

    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, new):
        self._phone_no = new 

    def __str__(self):
        return f"{self.name}\n{self.age}\nEmail :{self.email}\nPhone_No : {self.phone_no} "                                 