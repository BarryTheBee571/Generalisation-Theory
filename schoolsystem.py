class Person:
    def __init__(self, full_name, DOB, gender):
        self.full_name = full_name
        self.DOB = DOB
        self.gender = gender

    def display_details(self):
        print(f"Full Name: {self.full_name}, , Dob: {self.DOB}, Gender: {self.gender}")

class Parent(Person):
    def __init__(self, full_name, DOB, gender, job):
        super().__init__(full_name, DOB, gender)
        self.job = job

    def get_stats(self):
        print(f"Name: {self.full_name}")
        print(f"Date Of Birth: {self.DOB}")
        print(f"Gender: {self.gender}")
        print(f"Job: {self.job}")

class Teacher(Person):
    def __init__(self, full_name, DOB, gender, subject):
        super().__init__(full_name, DOB, gender)
        self.subject = subject

    def get_stats(self):
        print(f"Name: {self.full_name}")
        print(f"Date Of Birth: {self.DOB}")
        print(f"Gender: {self.gender}")
        print(f"Subjects: {self.subject}")

class Student(Person):
    def __init__(self, full_name, DOB, gender, year):
        super().__init__(full_name, DOB, gender)
        self.year=year

    def get_stats(self):
        print(f"Name: {self.full_name}")
        print(f"Date Of Birth: {self.DOB}")
        print(f"Gender: {self.gender}")
        print(f"Year: {self.year}")

parent =Parent("Tim John", "30th of Febuary 1640", "Male",  "Window Cleaner")
teacher =Teacher("Ted Mustard", "10th of September 2001", "Male", "Cooking")
student= Student("Stephen Wirianata", "6th of April 2010", "Male", 10)

parent.get_stats()
teacher.get_stats()
student.get_stats()