from faker import Faker
from random import choice
import json
import os
import re

# Faker ბიბლიოთეკის შემოტანა ქართული ინიციალებით
fake = Faker("ka_GE")

# თუ "students.json" ფაილი არ არსებობს, ვქმნით და შეგვყავს 100 სტუდენტი
if not os.path.exists("students.json"):
    students = [
        {
            "roll_number": i,
            "name": fake.name(),
            "grade": choice(["A", "B", "C", "D", "E", "F"]),
        }
        for i in range(1, 101)
    ]
    # მონაცემების ჩაწერა json ფაილში
    with open("students.json", "w", encoding="utf-8") as file:
        json.dump(students, file, indent=2, ensure_ascii=False)


# სტუდენტის კლასი (OOP)
class Student:
    # ფუნქცია სადაც განისაზღვრება როგორი ტიპის მონაცემს ელოდება თითოეული ცვლადი
    def __init__(self, name: str, roll_number: int, grade: str):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    # გეთერი სახელის ვალიდაციისთვის
    @property
    def name(self) -> str:
        return self._name

    # სეტერი სახელის ვალიდაციისთვის
    @name.setter
    def name(self, value: str):
        self._name = validate_name(value)

    # გეთერი შეფასების ვალიდაციისთვის
    @property
    def grade(self) -> str:
        return self._grade

    # სეტერი შეფასების ვალიდაციისთვის
    @grade.setter
    def grade(self, value: str):
        valid_grades = ["A", "B", "C", "D", "E", "F"]
        formatted_grade = str(value).strip().upper()

        if formatted_grade not in valid_grades:
            raise ValueError(
                f"არასწორი შეფასება! უნდა იყოს ერთ-ერთი შემდეგიდან: {', '.join(valid_grades)}"
            )

        self._grade = formatted_grade

    # გეთერი სიითი ნომრის ვალიდაციისთვის
    @property
    def roll_number(self) -> int:
        return self._roll_number

    # სეტერი სიითი ნომრის ვალიდაციისთვის
    @roll_number.setter
    def roll_number(self, value: int):
        if not (1 <= value <= 200):
            raise ValueError("გთხოვთ შეიყვანოთ ნომერი 1-დან 200-მდე")
        self._roll_number = value

    # სტუდენტის ობიექტის ტექსტური წარმოდგენა
    def __str__(self):
        return f"სახელი და გვარი: {self.name}, სიითი ნომერი: {self.roll_number}, ნიშანი: {self.grade}"


# სტუდენტების მართვის სისტემის კლასი
class StudentManagement:
    def __init__(self, json_file="students.json"):
        self.json_file = json_file
        self.students = []
        # ობიექტის შექმნისთანავე ტვირთავს მონაცემებს JSON-დან
        self.load_from_json()

    # JSON ფაილიდან მონაცემების წაკითხვა და Student ობიექტებად ქცევა
    def load_from_json(self):

        if not os.path.exists(self.json_file):
            self.students = []
            return

        with open(self.json_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.students = []
            for student in data:
                try:
                    self.students.append(
                        Student(
                            student["name"], student["roll_number"], student["grade"]
                        )
                    )
                except ValueError as e:
                    print(e)
                    continue

    # მიმდინარე სტუდენტების სიის JSON ფაილში შენახვის ფუნქცია
    def save_to_json(self):
        data = []
        for student in self.students:
            data.append(
                {
                    "name": student.name,
                    "roll_number": student.roll_number,
                    "grade": student.grade,
                }
            )
        with open(self.json_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    # ახალი სტუდენტის დამატების ფუნქცია
    def add_student(self, name: str, roll_number: int, grade: str):
        if not (101 <= roll_number <= 200):
            print("შეცდომა: ახალი სტუდენტის ნომერი უნდა იყოს 101-დან 200-მდე.")
            return False

        if self.get_student_by_roll_number(roll_number) is not None:
            print(f"შეცდომა: სტუდენტი სიის ნომრით {roll_number} უკვე არსებობს!")
            return False
        try:
            student = Student(name, roll_number, grade)
            self.students.append(student)
            self.save_to_json()
            print()
            print(f"სტუდენტი {name} წარმატებით დამატებულია")
            return True
        except ValueError as e:
            print(f"შეცდომა: {e}")
            return False

    # ყველა სტუდენტის ცხრილის სახით გამოტანა
    def show_all_students(self):
        if not self.students:
            print("სია ცარიელია!")
            return
        print("*" * 38)
        print(f" {'№':<5}{'სტუდენტი':<20} {'შეფასება'}")
        print("*" * 38)
        for student in self.students:
            print(f" {student.roll_number:<5}{student.name :<25}{student.grade}")

    # სტუდენტის ძებნა სიითი ნომრის მიხედვით
    def get_student_by_roll_number(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student
        return None

    # სტუდენტის ნიშნის განახლების მეთოდი
    def update_student_grade(self, roll_number: int, grade: str):
        student = self.get_student_by_roll_number(roll_number)
        if student:
            formatted_grade = str(grade).strip().upper()

            # შემოწმება: ხომ არ არის ახალი ნიშანი იგივე, რაც მიმდინარეა
            if student.grade == formatted_grade:
                print()
                print(
                    f"შეცდომა: სტუდენტს {student.name} უკვე აქვს შეფასება {formatted_grade}! შეფასება ვერ განახლდება."
                )
                print()
                return False
            try:
                student.grade = formatted_grade
                self.save_to_json()
                print()
                print(
                    f"შეფასება წარმატებით განახლდა, {student.name}ს შეფასება უკვე არის {student.grade}"
                )
                return True
            except ValueError:
                print()
                print(
                    "შეცდომა: გთხოვთ შეიყვანოთ შემდეგი ნიშნებიდან ერთ-ერთი A, B, C, D, E, F"
                )
                print()
                return False

        print("სტუდენტი ვერ მოიძებნა.")
        return False


# დამხმარე ფუნქცია მომხმარებლისგან მთელი რიცხვის უსაფრთხოდ მისაღებად
def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print()
            print("შეიყვანეთ მხოლოდ მთელი რიცხვი")
            print()


# სახელისა და გვარის ფორმატისა და სიმბოლოების ვალიდაცია Regex-ის გამოყენებით
def validate_name(name):
    normalized_name = " ".join(name.strip().split())
    pattern = r"^[ა-ჰ]+(?:\s+[ა-ჰ]+)+$"

    if not re.match(pattern, normalized_name):
        print()
        raise ValueError(
            "გთხოვთ შეიყვანოთ სტუდენტის სახელი და გვარი ქართულად შუაში ერთი გამოტოვებით (მაგ. გიორგი ბერიძე)."
        )

    if not (4 <= len(normalized_name) <= 25):
        raise ValueError("გთხოვთ შეიყვანოთ სწორი სახელი და გვარი")

    return normalized_name


# პროგრამის მთავარი მენიუ
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
        print()

        choice = input("აირჩიეთ ოპერაცია (1-5): ").strip()
        print()

        # ახალი სტუდენტის დამატება
        if choice == "1":
            while True:
                try:
                    name = input("შეიყვანეთ სტუდენტის სახელი და გვარი: ")
                    name = validate_name(name)
                    break
                except ValueError as e:
                    print(f"შეცდომა: {e}")
                    print()

            print()
            while True:
                roll_num = get_valid_int("შეიყვანეთ სიის ნომერი: ")

                if not roll_num:
                    print()
                    print(
                        "ახალი სტუდენტის სიითი ნომერი შეიძლება იყოს 101-დან 200-მდე..."
                    )
                    print()
                    continue

                if not (101 <= roll_num <= 200):
                    print()
                    print(
                        "ახალი სტუდენტის სიითი ნომერი შეიძლება იყოს 101-დან 200-მდე..."
                    )
                    print()
                    continue
                if system.get_student_by_roll_number(roll_num):
                    print()
                    print(
                        f"სტუდენტი სიითი ნომრი {roll_num} უკვე არსებობს, გთხოვთ შეიყვანოთ სიითი ნომერი 101-დან 200-მდე."
                    )
                    print()
                    continue
                break

            print()
            while True:
                grade = (
                    input("შეიყვანეთ ერთ-ერთი შეფასება (A, B, C, D, E, F): ")
                    .strip()
                    .upper()
                )

                if grade not in ["A", "B", "C", "D", "E", "F"]:
                    print()
                    print("გთხოვთ შეიყვანოთ მხოლოდ A, B, C, D, E ან F.")
                    print()
                    continue

                break

            system.add_student(name, roll_num, grade)

        # ყველა სტუდენტის გამოჩენა
        elif choice == "2":
            system.show_all_students()

        # სტუდენტის ძებნა ნომრით
        elif choice == "3":
            roll_num = get_valid_int("შეიყვანეთ საძიებო სტუდენტის სიის ნომერი: ")
            print()
            student = system.get_student_by_roll_number(roll_num)
            if student:
                print("ნაპოვნია სტუდენტი მითითებული სიითი ნომრით:")
                print("-" * 45)
                print()
                print(student)
            else:
                print()
                print(
                    f"სტუდენტი ნომრით {roll_num} ვერ მოიძებნა, გთხოვთ შეიყვანოთ სიითი ნომერი 1-დან 100-მდე."
                )

        # სტუდენტის შეფასების შეცვლა
        elif choice == "4":
            while True:
                roll_num = get_valid_int(
                    "შეიყვანეთ სტუდენტის სიის ნომერი შეფასების შესაცვლელად: "
                )
                student = system.get_student_by_roll_number(roll_num)
                if student:
                    print()
                    print(
                        f"თქვენს მიერ არჩეული სტუდენტია: {student.name} (მიმდინარე შეფასება: {student.grade})"
                    )
                    print()
                    new_grade = input("შეიყვანეთ ახალი შეფასება: ").strip()
                    if system.update_student_grade(roll_num, new_grade):
                        break
                else:
                    print()
                    print(
                        f"სტუდენტი ნომრით {roll_num} ვერ მოიძებნა, გთხოვთ შეიყვანოთ სიითი ნომერი 1-დან 100-მდე."
                    )
                    break

        # გამოსვლა პროგრამიდან
        elif choice == "5":
            print("პროგრამა დასრულებულია. ნახვამდის!")
            break
        else:
            print("თქვენ არასწორად აირჩიეთ. გთხოვთ აირჩიოთ ციფრი 1-დან 5-მდე.")


# პროგრამის გაშვება
main_menu()
