class Student:
    name="Agness"
    school= "Akirachix"
    code = 79
    age=20

class New_student:
    school="Akirachix"
    def __init__(self, first_name,last_name,age,country,code):
        self.first_name= first_name
        self.last_name= last_name
        self.age=age
        self.country=country
        self.code=code
    def greet_student(self):
        greeting= f" Hello {self.first_name}, welcome to {self.school},your code is {self.code}"
        return greeting
    def year_of_birth(self):
        return f"Hello {self.first_name} you were born in year {2024-self.age}"
    def full_names(self):
        full_name=self.first_name+" "+self.last_name
        return full_name
    def show_initials(self):
        initials= self.first_name[0]+self.last_name[0]
        return initials
    def check_minor(self):
        # if self.age<=18
        return f"you are a minor"
    # def enroll_student(self):


    
