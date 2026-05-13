# 1
class Student:
    school_name = "Najot Ta'lim"
    country = "Uzbekistan"

    def __init__(self, fullname, age, course, grade):
        self.fullname = fullname
        self.age = age
        self.course = course
        self.grade = grade

    def show_info(self):
        print(f"Ism: {self.fullname}")
        print(f"Yosh: {self.age}")
        print(f"Kurs: {self.course}")
        print(f"Bahosi: {self.grade}")
        print(f"Maktab: {Student.school_name}")
        print(f"Mamlakat: {Student.country}")

    def change_grade(self, new_grade):
        print(f"{self.fullname} bahosi o'zgardi: {self.grade} -> {new_grade}")
        self.grade = new_grade


s1 = Student("Azamat", 21, "Backend", "B")
s2 = Student("Ali", 19, "Frontend", "C")
s3 = Student("Vali", 22, "Design", "A")

s1.show_info()
print("------------")
s2.show_info()
print("------------")
s3.show_info()

print("\n===== O'ZGARISHDAN KEYIN =====\n")


s1.change_grade("A")
s2.change_grade("B+")


print("\n--- YANGILANGAN MA'LUMOTLAR ---\n")
s1.show_info()
print("------------")
s2.show_info()

# 2
class Car:
    wheels = 4
    country = "Germany"

    def __init__(self, brand, color, price, speed):
        self.brand = brand
        self.color = color
        self.price = price
        self.speed = speed

    def show_car(self):
        print(f"brand: {self.brand}, color: {self.color}, price: {self.price}, speed: {self.speed}")

    def change_color(self, new_color):
        print(f"{self.color} va {self.speed} ozgardi")
        self.color = new_color


c1 = Car("BMW", "black", 23000, 200)
c2 = Car("Mers", "Pink", 30000, 280)

c1.show_car()
c2.show_car()

c1.change_color("Yellow")
