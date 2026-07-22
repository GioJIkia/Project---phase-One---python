from faker import Faker
from random import choice
import json
import os
import re 

fake = Faker("ka_GE")


if not os.path.exists("students.json"):
    students = [
        {
            "roll_number": i,
            "name": fake.name(),
            "grade": choice(["A", "B", "C", "D", "E", "F"])
        }
        for i in range(1, 101)
    ]

    with open("students.json", "w", encoding="utf-8") as file:
        json.dump(students, file, indent=2, ensure_ascii=False)

class Student:
    def __init__(self, name: str, roll_number: int, grade: str):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        normalized_name = " ".join(value.strip().split())
        pattern = r"^[ა-ჰ]+(?:\s+[ა-ჰ]+)+$"
        
        if not re.match(pattern, normalized_name):
            raise ValueError("გთხოვთ შეიყვანოთ სტუდენტის სახელი და გვარი ქართულად ზედმეტი სიმბოლოების გარეშე, შუაშუ სფეისით (მაგ. სახელი გვარი)")
        if not (4 <= len(normalized_name) <= 25):
            raise ValueError("გთხოვთ შეიყვანოთ სწორი სახელი და გვარი")

        self._name = normalized_name

    @property
    def grade(self) -> str:
        return self._grade

    @grade.setter
    def grade(self, value: str):
        valid_grades = ["A", "B", "C", "D", "E", "F"]
        formatted_grade = str(value).strip().upper()
        
        if formatted_grade not in valid_grades:
            raise ValueError(f"არასწორი შეფასება! უნდა იყოს ერთ-ერთი შემდეგიდან: {', '.join(valid_grades)}")
            
        self._grade = formatted_grade
        
        
    def __str__(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, Grade: {self.grade}"

class StudentManagement:
    def __init__(self, json_file="students.json"):
        self.json_file = json_file
        self.students = []
        self.load_from_json()

    def load_from_json(self):
        with open(self.json_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.students = []
            for student in data:
                try:
                    self.students.append(
                    Student(
                        student["name"],
                        student["roll_number"],
                        student["grade"]
                    )
                    )
                except ValueError:
                    continue
                    
    def save_to_json(self):
        data = []
        for student in self.students:
            data.append({
                "name": student.name,
                "roll_number": student.roll_number,
                "grade": student.grade
            })
        with open(self.json_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def add_student(self, name: str, roll_number: int, grade: str):
        if self.get_student_by_roll_number(roll_number) is None:
            try:
                student = Student(name, roll_number, grade)
                self.students.append(student)
                self.save_to_json()
                print (f"სტუდენტი {name} წარმატებით დამატებულია")
                return True
            except ValueError:
                return False
        else:
            print(f"❌ შეცდომა: სტუდენტი სიის ნომრით {roll_number} უკვე არსებობს!")
            return False

    def show_all_students(self):
        print("*" * 38)
        print(f" {'№':<5}{'სტუდენტი':<20} {'შეფასება'}")
        print("*" * 38)
        for student in self.students:
            print(f" {student.roll_number:<5}{student.name :<25}{student.grade}")
    
    def get_student_by_roll_number(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student
        return None

    def update_student_grade(self, roll_number: int, grade: str):
        student = self.get_student_by_roll_number(roll_number)
        if student:
            try:
                student.grade = grade
                self.save_to_json()
                print(f"შეფასება წარმატებით განახლდა, {student.name}ს შეფასება უკვე არის {grade}")
                return True
            except ValueError:
                return False

        print("სტუდენტი ვერ მოიძებნა.")
        return False

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ შეიყვანეთ მხოლოდ რიცხვი.")


def main_menu():
    system = StudentManagement()

    while True:
        print("\n" + "=" * 35)
        print("სტუდენტების მართვის სისტემა")
        print("=" * 35)
        print("1. ახალი სტუდენტის დამატება")
        print("2. ყველა სტუდენტის ნახვა")
        print("3. სტუდენტის ძებნა ნომრის მიხედვით")
        print("4. სტუდენტის შეფასების განახლება")
        print("5. გასვლა")

        choice = input("აირჩიეთ ოპერაცია (1-5): ").strip()

        if choice == "1":
            name = input("შეიყვანეთ სტუდენტის სახელი და გვარი: ").strip()
            roll_num = get_valid_int("შეიყვანეთ სიის ნომერი: ")
            grade = input("შეიყვანეთ შეფასება (A, B, C, D, E, F): ").strip()

            system.add_student(name, roll_num, grade)

        elif choice == "2":
            system.show_all_students()

        elif choice == "3":
            roll_num = get_valid_int("შეიყვანეთ საძიებო სტუდენტის სიის ნომერი: ")
            student = system.get_student_by_roll_number(roll_num)
            if student:
                print("\nნაპოვნია სტუდენტი:")
                print(student)
            else:
                print(f"❌ სტუდენტი ნომრით {roll_num} ვერ მოიძებნა.")

        elif choice == "4":
            roll_num = get_valid_int("შეიყვანეთ სტუდენტის სიის ნომერი შეფასების შესაცვლელად: ")
            student = system.get_student_by_roll_number(roll_num)
            if student:
                print(f"არჩეული სტუდენტი: {student.name} (მიმდინარე შეფასება: {student.grade})")
                new_grade = input("შეიყვანეთ ახალი შეფასება: ").strip()
                system.update_student_grade(roll_num, new_grade)
            else:
                print(f"❌ სტუდენტი ნომრით {roll_num} ვერ მოიძებნა.")

        elif choice == "5":
            print("პროგრამა დასრულებულია. ნახვამდის!")
            break
        else:
            print("❌ არასწორი არჩევანი. გთხოვთ აირჩიოთ 1-დან 5-მდე.")

main_menu()
