# დავალება 1 - კალკულატორი
# კალკულატორის ფუნქცია მომხმარებლებს საშუალებას აძლევს შეასრულონ ძირითადი
# არითმეტიკული მოქმედებები (+, -, *, /). მომხმარებლებს შეუძლიათ შეიყვანონ ორი რიცხვი და
# შემდეგ აირჩიონ ოპერაცია შედეგის მისაღებად. კალკულატორი ასევე შეიცავს შეყვანის
# ვალიდაციას არასწორი შეყვანების დასამუშავებლად.

import os

# საქაღალდის და ფაილის შექმნა
folder = "project_1"
file = "calculator.py"

os.makedirs(folder, exist_ok=True)
file_name = os.path.join(folder, file)

calculator_code = """#კალკულატორი
def calculator(num1, num2, operator):

    # 0-ზე გაყოფის ვალიდაცია
    if operator in ["/", "%"] and num2 == 0:
        print()
        return "შეცდომა, 0-ზე გაყოფა შეუძლებელია!"

    # ფუნქციის მათემატიკური მოქმედებები
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    elif operator == "**":
        return num1 ** num2


# მომხმარებლის მიერ შესაყვანი ინფორმაციის ფუნქცია
def main():
    print("=========== კალკულატორი ===========")
    
    num1 = None  # ინახავს წინა შედეგს, თუ მომხმარებელს მისი გამოყენება სურს

    while True:
        #პირველი რიცხვის შეყვანა და ვალიდაცია
        if num1 is None:
            while True:
                try:
                    print ()
                    num1_input = input("შეიყვანეთ პირველი რიცხვი: ").strip()

                    num1 = float(num1_input)
                    break
                except ValueError:
                    print ()
                    print("შეცდომა, გთხოვთ შეიყვანოთ მხოლოდ ციფრები!")

        #ოპერატორის შეყვანა და ვალიდაცია
        while True:
            print ()
            operator = input("აირჩიეთ სასურველი ოპერაცია (+, -, *, /, %, **): ").strip()
            if operator in ["+", "-", "*", "/", "%", "**"]:
                break
            print ()
            print("შეცდომა, თქვენს მიერ შეყვანილია არასწორი ოპერატორი! გთხოვთ სცადოთ ხელახლა.")

        #მეორე რიცხვის შეყვანა და ვალიდაცია
        while True:
            try:
                print ()
                num2_input = input("შეიყვანეთ მეორე რიცხვი: ").strip()
                num2 = float(num2_input)
                break
            except ValueError:
                print ()
                print("შეცდომა, გთხოვთ შეიყვანოთ მხოლოდ ციფრები!")

        # გამოთვლა
        result = calculator(num1, num2, operator)

        #თუ კალკულატორმა ტექსტური შეცდომა დააბრუნა (მაგ. 0-ზე გაყოფა)
        if isinstance(result, str):
            print(result)
            # შეცდომისას თავიდან ვიწყებთ
            num1 = None 
            continue

        # მთელი რიცხვების ლამაზად გამოჩენა (ათწილადის გარეშე)
        display_num1 = int(num1) if num1 == int(num1) else num1
        display_num2 = int(num2) if num2 == int(num2) else num2
        display_result = int(result) if result == int(result) else result

        # ეკრანზე საბოლოო ტოლობის გამოტანა
        print()
        print(f"შედეგი: {display_num1} {operator} {display_num2} = {display_result}")

        # შეკითხვა მომხმარებელს
        print()
        choice = input(f"გსურთ მიღებული შედეგის ({display_result}) გამოყენება შემდეგი გამოთვლისთვის? (yes/no/exit): ").strip().lower()

        if choice in ["yes", "y", "კი", "ki"]:
            num1 = result  # შედეგი გადადის პირველ რიცხვად
        elif choice in ["exit", "გამოსვლა"]:
            print()
            print("გმადლობთ კალკულატორით სარგებლობისთვის!")
            break
        else:
            num1 = None  # თავიდან იწყება ახალი ტოლობა

# პროგრამის გაშვება
main()
"""

# calculator.py ფაილში ჩაწერა
with open(file_name, "w", encoding="utf-8") as file:
    file.write(calculator_code)
###===============================================================================================================###

# დავალება 2 - თამაში 1 (გამოიცანით რიცხვი)

# ამ თამაშში პროგრამა აგენერირებს შემთხვევით რიცხვს მითითებული დიაპაზონიდან.
# მომხმარებლებს სთხოვენ გამოიცნონ რიცხვი. არასწორი რიცხვის შემთხვევაში პროგრამა
# მომხმარებელს აძლევს მინიშნებას (უფრო მაღალი/უფრო დაბალი). თამაში აკონტროლებს
# მცდელობების რაოდენობას და აჩვენებს შედეგს, როდესაც მომხმარებელი გამოიცნობს სწორ
# რიცხვს.

from random import randint
import os

# საქაღალდის და ფაილის შექმნა
folder = "project_2"
file = "guess_the_number.py"

os.makedirs(folder, exist_ok=True)
file_name = os.path.join(folder, file)

guess_the_number_code = """from random import randint

# სამომხმარებლო ფუნქცია ვალიდაციისთვის
def guess_the_number(step, remaining_guesses, history):
    while True:
        try:
            # მომხმარებლის მიერ მონაცემების შემოტანა ტექსტურ ფორმატში
            user_input = (input(f"ცდა {step}, დარჩენილი გაქვთ {remaining_guesses} მცდელობა, გამოიცანი ჩაფიქრებული მთელი რიცხვი 1-დან 100-მდე: "))
            print ("===========================================================================================")
            print ()

            # ვამოწმებთ, ხომ არ არის შეყვანილი ველი ცარიელი
            if not user_input.strip():
                print ("შეცდომა, ველი ცარიელია, გთხოვთ შეიყვანოთ მთელი რიცხვი 1-დან 100-მდე!")
                print ()
                continue

            # მომხმარებლის მიერ შემოტანილი მონაცემის ტიპის გარდაქმნა ტექსტიდან მთელ რიცხვში
            number_value = int(user_input)

            # ვამოწმებთ, ხომ არ მეორდება რიცხვი ისტორიაში
            if number_value in history:
                print(f"შეცდომა, რიცხვი {number_value} უკვე შეიყვანეთ ადრე! იყავით ყურადღებით! მცდელობა არ დაგაკლდებათ!")
                print ()
                continue

            # ვამოწმებთ, ხომ არ სცილდება რიცხვი დასაშვებ დიაპაზონს
            if 1 <= number_value <= 100:
                return number_value
            else:
                print("შეცდომა, გთხოვთ შეიყვანოთ მთელი რიცხვი 1-დან 100-მდე!")
                print ()

        except ValueError:
            # თუ მომხმარებელი რიცხვის ნაცვლად შეიყვანს ტექსტს შეცდომის გამოტანა
            print("შეცდომა, გთხოვთ შეიყვანოთ მხოლოდ ციფრები!")
            print ()

# თამაშის მართვის ფუნქცია
def play_game():

    # კომპიუტერის მიერ ჩაფიქრებული შემთხვევითი რიცხვი
    secret_number = randint(1, 100)

    # მცდელობების მაქსიმალური რაოდენობა
    total_guesses = 8

    # მიმდინარე მცდელობის რაოდენობა
    i = 1

    # შეყვანილი რიცხვების ისტორია
    user_input_history = []

    print("თამაში დაიწყო! ჩაფიქრებულია რიცხვი 1-დან 100-მდე, აბა გამოიცანით...")
    print ()
    print(f"თქვენ გაქვთ სულ {total_guesses} მცდელობა!")
    print ()

    # ციკლის ოპერატორი
    while i <= total_guesses:

        # დარჩენილი მცდელობების გამოთვლა
        remaining_guesses = total_guesses - i

        # ვალიდაციის ფუნქციის გამოძახება
        guess = guess_the_number(i, remaining_guesses, user_input_history)

        # მიღებული მნიშვნელობის დამატება ისტორიაში
        user_input_history.append(guess)

        # პირობითი ოპერატორები
        if guess == secret_number:
            print(f"გილოცავთ,თქვენ გამოიცანით რიცხვი! ჩაფიქრებული რიცხვი იყო {secret_number}!")
            print ()

            # ციკლის შეწყვეტა მოგების შემთხვევაში
            break
        elif guess > secret_number:
            print("თქვენს მიერ შეყვანილი რიცხვი მეტია ჩაფიქრებულ რიცხვზე, გთხოვთ შეიყვანოთ უფრო ნაკლები რიცხვი!")
            print ()
        else:
            print ("თქვენს მიერ შეყვანილი რიცხვი ნაკლებია ჩაფიქრებულ რიცხვზე, გთხოვთ შეიყვანოთ უფრო მეტი რიცხვი")
            print ()

        # მთვლელის გაზრდა
        i += 1

    else:
        # დასრულება ციკლის, როდესაც ციკლი ამოიწურება და break არ მოხდება

        print(f"სამწუხაროდ თქვენ დამარცხდით, ჩაფიქრებული რიცხვი იყო {secret_number}!")
        print ()

# თამაშის ფუნქციის გამოძახება
play_game()"""


# ფაილში ჩაწერა მთელი იმ კოდის, რაც მოთავსებულია სამმაგ ბრჭყალებში
with open(file_name, "w", encoding="utf-8") as file:
    file.write(guess_the_number_code)

###===============================================================================================================###

# დავალება 3 - თამაში 2 (Hangman)

# Hangman არის სიტყვების გამოცნობის თამაში. პროგრამა ირჩევს შემთხვევით სიტყვას
# წინასწარ განსაზღვრული სიიდან და აჩვენებს მას ქვედა ტირეების გამოყენებით (რამდენი
# ასოცაა სიტყვაში, იმდენი ქვედა ტირე), რომელიც წარმოადგენს ფარულ ასოებს.
# მომხმარებლებს სთხოვენ გამოიცნონ ასო და პროგრამა ამოწმებს არის თუ არა ასო სიტყვაში.
# ვლინდება სწორად გამოცნობილი ასოები და თამაში გრძელდება მანამ, სანამ მომხმარებელი
# არ გამოიცნობს სიტყვას ან არ ამოიწურება მცდელობები.

import random

# საქაღალდის და ფაილის შექმნა
folder = "project_3"
file = "hangman.py"

os.makedirs(folder, exist_ok=True)
file_name = os.path.join(folder, file)

hangman_code = r'''import random

#თამაშის ეტაპების გრაფიკული გამოსახულება
stages = [
    r"""
------
  |  |
     |
     |
     |
     |
------
""",
    r"""
------
  |  |
  O  |
     |
     |
     |
------
""",
    r"""
------
  |  |
  O  |
  |  |
     |
     |
------
""",
    r"""
------
  |  |
  O  |
 /|  |
     |
     |
------
""",
    r"""
------
  |  |
  O  |
 /|\ |
     |
     |
------
""",
    r"""
------
  |  |
  O  |
 /|\ |
 /   |
     |
-------
""",
    r"""
------
  |  |
  O  |
 /|\ |
 / \ |
     |
------
""",
]

# გამოსაცნობი სიტყვების სია
word_bank = [
    "tomato",
    "potato",
    "carrot",
    "onion",
    "cucumber",
    "cabbage",
    "broccoli",
    "cauliflower",
    "spinach",
    "lettuce",
    "pepper",
    "eggplant",
    "zucchini",
    "pumpkin",
    "radish",
    "beetroot",
    "garlic",
    "ginger",
    "peas",
    "corn",
    "celery",
    "asparagus",
    "mushroom",
]


# სიტყვის ეკრანზე ჩვენების ფუნქცია
def get_display_word(word, guessed_letters):
    result = []
    for letter in word:
        # თუ მომხმარებელმა ასო გამოიცნო ვამატებთ მას
        if letter in guessed_letters:
            result.append(letter)
        # თუ ასო ჯერ ვერ გამოიცნო ვწერთ ქვედა ტირეს
        else:
            result.append("_")
    return " ".join(result)

# მომხმარებლის მიერ შეყვანილი ასოს ვალიდაციის ფუნქცია
def get_valid_input (guessed_letters):
    while True:
        guess = input("გამოიცანი ლათინური ასო: ").lower().strip()

        # ამოწმებს, რომ მომხმარებლის მიერ შეყვანილი იყოს 1 ასო
        if len(guess) != 1:
            print ()
            print("შევდომა, გთხოვთ შეიყვანოთ 1 ლათინური ასო.")
            print ()
            continue
        # ამოწმებს, რომ შეყვანილი იყოს ლათინური ანბანის ასო
        if not (guess.isalpha() and guess.isascii()):
            print ()
            print("შეცდომა, გთხოვთ შეიყვანოთ ლათინური ასო (a-z).")
            print ()
            continue
        # ამოწმებს, ხომ არ არის ასო უკვე გამოყენებული
        if guess in guessed_letters:
            print ()
            print(f"თქვენ უკვე შეიყვანეთ ასო {guess}.")
            print ()
            continue
      
        return guess

# თამაშის ფუნქცია
def hangman():
    # შემთხვევითობის პრინციპით კომპიუტერი ირჩევს საიდუმლო სიტყვას
    random_word = random.choice(word_bank)

    # მასივი, სადაც შევა მომხმარებლის მიერ შეყვანილი ლათინური ასო
    guessed_letters = []

    # მცდელობების რაოდენობა
    attempts = 6

    print ("==============================")
    print("მოგესალმებით თამაშ Hangman-ში!")
    print ("==============================")
    print ()
    print("თქვენ გაქვთ 6 მცდელობა რომ გამოიცნოთ ბოსტნეულის ლათინური სახელწოდება...")

    while attempts > 0:
    
        # ვბეჭდავთ დარჩენილი მცდელობების რაოდენობას
        print()
        print(f"მცდელობა დარჩა: {attempts}")

        # ვბეჭდავთ შესაბამის გრაფიკულ გამოსახულებას მცდელობების მიხედვით
        print(stages[6 - attempts])
        print ()

        # ვაჩვენებთ მომხმარებელს უკვე გამოყენებული ასოების ისტორიას
        print ()
        print(f"შეყვანილი ასოების ისტორია: {', '.join(guessed_letters) if guessed_letters else 'ცარიელია'}")
        print ()
        
        # ველოდებით ვალიდურ ასოს მომხმარებლისგან
        guess = get_valid_input(guessed_letters)

        # შეყვანილ ასოს ვამატებთ უკვე შეყვანილი ასოების ისტორიის მასივში
        guessed_letters.append(guess)

        # შემოწმება არის თუ არა ასო საიდუმლო სიტყვაში
        if guess not in random_word:
            print ()
            attempts -= 1
            print(f"{guess} არ არის ჩაფიქრებულ სიტყვაში. შენ გაქვს {attempts} მცდელობა დარჩენილი.")
            print ()
        else:
            print ()
            print(f"ყოჩაღ! {guess} არის ჩაფიქრებულ სიტყვაში.")
            print ()

        # ვბეჭდავთ სიტყვის მიმდინარე მდგომარეობას ტირეებით ან გამოცნობილი ასოებით
        current_display = get_display_word(random_word, guessed_letters)
        print (f"სიტყვაში გამოცნობილი ასოების არსებული მდგომარეობა: {current_display}")
        print ()

        # კითხვა მომხმარებლისთვის სურს თუ არა მთელი სიტყვის გამოცნობა
        while True:
            choice_hangman = input("გსურთ მთელი სიტყვის დასახელება? (კი ან არა): ").strip().lower()
            print()

            if choice_hangman == "კი":

                while True:
                    word_guess = input("შეიყვანეთ ბოსტნეულის ლათინური სახელწოდების მთლიანი სიტყვა: ").strip().lower()

                    # ვალიდაცია, ცარიელი სიტყვის გამორიცხვა
                    if not word_guess:
                        print()
                        print("შეცდომა, სიტყვა არ შეიძლება იყოს ცარიელი.")
                        print()
                        continue

                    # ვალიდაცია, მხოლოდ ლათინური ასოების დაშვება
                    if not (word_guess.isalpha() and word_guess.isascii()):
                        print()
                        print("შეცდომა, გთხოვთ შეიყვანოთ მხოლოდ ლათინური ასოებით დაწერილი სიტყვა.")
                        print()
                        continue

                    break

                # თუ სწორია სიტყვა
                if word_guess == random_word:
                    print()
                    print("--------------------------------------------------------------")
                    print(f"გილოცავთ! თქვენ მოიგეთ! ჩაფიქრებული სიტყვა იყო {random_word}")
                    print("--------------------------------------------------------------")
                else:
                    print()
                    print("-------------------------------------------------------------------")
                    print(f"სამწუხაროდ თქვენ დამარცხდით! ჩაფიქრებული სიტყვა იყო {random_word}")
                    print("-------------------------------------------------------------------")

                return

            elif choice_hangman == "არა":
                break

            else:
                print("არასწორი არჩევანი, გთხოვთ აირჩიოთ მხოლოდ 'კი' ან 'არა'.")
                print()

        # ამოწმებს, მოიგო თუ არა მოთამაშემ, თუ აღარ დარჩა ქვედა ტირეები მოგებულად აცხადებს
        if "_" not in get_display_word(random_word, guessed_letters):
            print (stages [6 - attempts])
            print ()

            print ("--------------------------------------------------------------")
            print(f"გილოცავთ! თქვენ მოიგეთ! ჩაფიქრებული სიტყვა იყო {random_word}")
            print ("--------------------------------------------------------------")
            print ()
            break
            
    # თუ ციკლის ისე დასრულდა, რომ ვერ გამოიცნო მომხმარებელმა სიტყვა აგდებს წაგების შეტყობინებას
    else:
        print(stages[6])
        print ()

        print ("-------------------------------------------------------------------")
        print(f"სამწუხაროდ თქვენ დამარცხდით! ჩაფიქრებული სიტყვა იყო {random_word}")
        print ("-------------------------------------------------------------------")

# თამაშის ფუნქციის გამოძახება
hangman()
'''

# ფაილში ჩაწერა მთელი იმ კოდის, რაც მოთავსებულია სამმაგ ბრჭყალებში
with open(file_name, "w", encoding="utf-8") as file:
    file.write(hangman_code)

###===============================================================================================================###

# დავალება 4 - ბანკომატი
# ბანკომატის აპლიკაცია საშუალებას აძლევს მომხმარებელს განახორციელოს ბანკომატის
# ძირითადი ოპერაციების სიმულაცია. მომხმარებელს შეუძლია შეასრულოს ისეთი ქმედებები,
# როგორიცაა ბალანსის შემოწმება, თანხის შეტანა და თანხის გატანა. მომხმარებლის
# მონაცემები ინახება ტექსტურ ფაილში მომხმარებლის ანგარიშის ინფორმაციის
# შესანარჩუნებლად.

# საქაღალდის და ფაილის შექმნა
folder = "project_4"
file = "cashpoint.py"

os.makedirs(folder, exist_ok=True)
file_name = os.path.join(folder, file)

cashpoint_code = """import os
import sys
import re

# ცვლადი, სადაც მომხმარებლების მონაცემები ინახება
file_name = "accounts.txt"

# ფაილიდან მონაცემების წაკითხვის და ლექსიკონში შენახვის ფუნქცია
def load_accounts():
    accounts = {}

    # თუ ფაილი ჯერ საერთოდ არ არსებობს, ვაბრუნებთ ცარიელ ლექსიკონს
    if not os.path.exists(file_name):
        return accounts

    # ფაილის გახსნა წასაკითხად
    with open(file_name, "r", encoding="utf-8") as file:
        
        # პირველი ორი ხაზის (სათაური, ტირეები) გამოტოვება
        next (file)
        next (file)

        for line in file:
            # თითოეული ხაზის დაყოფა მძიმით
            username, email, password, balance = line.strip().split(",")

            # მომხმარებლის დამატება
            accounts[username] = {
                "email": email,
                "password": password,
                "balance": float(balance)
                }

    return accounts

# ლექსიკონში არსებული მონაცემების ტექსტურ ფაილში შენახვა
def save_accounts(accounts):
    with open(file_name, "w", encoding="utf-8") as file:
        
        # პირველი ხაზი - სვეტების სახელები
        file.write("მომხმარებელი,ელ-ფოსტა,პაროლი,ბალანსი(ლარი)\\n")

        # მეორე ხაზი - ტირეები
        file.write("---------------------------------------------------\\n")

        # შემდეგი ხაზები - შენახული ინფორმაცია
        for username in accounts:
            email = accounts[username]["email"]
            password = accounts[username]["password"]
            balance = accounts[username]["balance"]

            file.write(f"{username},{email},{password},{balance}\\n" )

# ახალი მომხმარებლის რეგისტრაცია
def register(accounts):
    print("--- რეგისტრაცია ---")
    print ()
    # მომხმარებლის სახელის შეყვანა
    username = input("შეიყვანეთ მომხმარებლის სახელი: ").strip()
    print ()
    # ვალიდაცია, ცარიელი მომხმარებლის სახელის გამორიცხვა
    if not username:
        print("მომხმარებლის სახელი არ შეიძლება იყოს ცარიელი.")
        print ()
        return

    # ვალიდაცია, მომხმარებლის სახელის შემადგენელი ნაწილის განსაზღვრა
    if not re.match("^[a-zA-Z0-9]+$", username):
        print("მომხმარებლის სახელი უნდა შეიცავდეს მხოლოდ ლათინურ ასოებს და ციფრებს.")
        print ()
        return

    # ვალიდაცია, არსებული მომხმარებლის თავიდან რეგისტრაციის გამორიცხვა
    if username in accounts:
        print("მომხმარებელი უკვე არსებობს!")
        print ()
        return
    
    # ვალიდაცია, მომხმარებლის სახელის სიმბოლოების მინიმალური რაოდენობის განსაზღვრა
    if len(username) < 6:
        print("მომხმარებლის სახელი უნდა შეიცავდეს მინიმუმ 6 სიმბოლოს.")
        print ()
        return

    # მეილის შეყვანა და regex ვალიდაცია
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
    
    while True:
        email = input("შეიყვანეთ ელ-ფოსტა: ").strip()
        print ()
        
        # ვალიდაცია, მომხმარებლის ცარიელი ელ-ფოსტის გამორიცხვა
        if not email:
            print("ელ-ფოსტა არ შეიძლება იყოს ცარიელი.")
            print ()
            continue
            
        # ვალიდაცია, შემოწმება ემთხვევა თუ არა შეყვანილი ტექსტი სტანდარტული მეილის ფორმატს
        if not re.match(email_regex, email):
            print("არასწორი ელ-ფოსტის ფორმატი! გთხოვთ შეიყვანოთ შემდეგი ფორმატით (მაგ: example@domain.com)")
            print ()
            continue
        
        # ვალიდაცია, უკვე რეგისტრირებული ელ-ფოსტის შემოწმება
        email_exists = False
        for account_info in accounts.values():
            if account_info["email"] == email:
                email_exists = True
                break
        
        if email_exists:
            print("ეს ელ-ფოსტა უკვე დარეგისტრირებულია სხვა მომხმარებელზე!")
            print ()
            continue
            
        break

    # პაროლის შეყვანა და რეჯექს (Regex) ვალიდაცია
    password_regex = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[^a-zA-Z\\d]).{8,}$")

    while True:
        password = input("შეიყვანეთ პაროლი (მინიმუმ 8 სიმბოლო, 1 დიდი ასო, 1 პატარა და 1 ციფრი): ").strip()
        print ()
        
        # ვალიდაცია, მომხმარებლის ცარიელი პაროლის გამორიცხვა
        if not password:
            print("პაროლი არ შეიძლება იყოს ცარიელი.")
            print ()
            continue

        # ვალიდაცია, regex-ის
        if password_regex.match(password):
            print ("პაროლი წარმატებით დადასტურდა.")
            print ()
            break
        else:
            print ("პაროლი არასწორია. გთხოვთ შეიყვანოთ შემდეგი პაროლის ფორმატით (მაგ: Abc123!)")
            print ()
    
    #საწყისი ბალანსის შეყვანა
    while True:
        try:
            balance = float(input("შეიყვანეთ თქვენი საწყისი ბალანსი ლარში: "))
            print ()

            # ვალიდაცია, უარყოფითი ბალანსის გამორიცხვა
            if balance < 0:
                print("ბალანსი უარყოფითი არ შეიძლება იყოს.")
                continue
                
            break
            
        # ასოების შეყვანის გამორიცხვა
        except ValueError:
            print()
            print("შეიყვანეთ მხოლოდ რიცხვი.")
            print()

    # ახალი მომხმარებლის დამატება        
    accounts[username] = {"email": email, "password": password, "balance": balance}
    
    # მონაცემების შენახვა
    save_accounts(accounts)

    print("რეგისტრაცია წარმატებით დასრულდა.")
    print ()

# ავტორიზაციის ფუნქცია
def login(accounts):
    print("--- ავტორიზაცია ---")
    print ()
    username = input("მომხმარებელი: ").strip()
    print ()
    password = input("პაროლი: ")
    print ()

    # მომხმარებლის შემოწმება
    if username in accounts and accounts[username]["password"] == password:
        print(f"შესვლა წარმატებით განხორციელდა {username}")
        return username

    print("თქვენს მიერ მითითებული მონაცემები არასწორია.")
    print ()
    return None

# ბალანსის შემოწმების ფუნქცია
def check_balance(accounts, username):
    print(f"ბალანსი: {accounts[username]['balance']} ლარი")

# თანხის შეტანის ფუნქცია
def deposit(accounts, username):
    try:
        amount = float(input("შეიტანეთ ლარის რაოდენობა, რომლის შეტანაც გინდათ: "))
        print ()

        # ვალიდაცია, უარყოფითი თანხის გამორიცხვა
        if amount <= 0:
            print("თანხა უნდა იყოს დადებითი რიცხვი.")
            return
        
        # არსებული ბალანსის გაზრდა
        accounts[username]["balance"] += amount

        # მონაცემების შენახვა
        save_accounts(accounts)

        print(f"თქვენს მიერ შეტანილი {amount} ლარი წარმატებით დაემატა თქვენს ბალანს.")
        print ()
        print (f"თქვენი ბალანსი შეადგენს: {accounts[username]['balance']} ლარს")

    except ValueError:
        print("არასწორი მონაცემი.")

# თანხის გატანის ფუნქცია
def withdraw(accounts, username):

    # ვალუტის კურსები
    rates = {
        "1": 1,
        "2": 2.6327,
        "3": 3.01
    }
    while True:
        print ()
        print("გასატანი თანხის სასურველი ვალუტა")
        print ("--------------------------------")
        print ()
        print("1. ლარი")
        print("2. დოლარი")
        print("3. ევრო")
        print ()

        currency = input("აირჩიეთ სასურველი ვალუტის შესაბამისი ციფრი: ").strip()
        print ()

        if currency not in rates:
            print("გთხოვთ აირჩიეთ სასურველი ვალუტის შესაბამისი ციფრი.")
            print()
            continue
        else:
            break
    

    try:
        amount = float(input("შეიტანეთ თანხის რაოდენობა, რომლის გატანაც გინდათ: "))
        print ()

        # ვალიდაცია, უარყოფითი თანხის გამორიცხვა
        if amount <= 0:
            print("თანხა უნდა იყოს დადებითი რიცხვი.")
            return

        # თანხის ლარში გადაყვანა
        gel_amount = amount * rates[currency]

        # ვალიდაცია, ზედმეტი თანხის გამოტანის გამორიცხვა
        if gel_amount > accounts[username]["balance"]:
            print("ბალანსზე არ გაქვთ ოპერაციის შესრულებისთვის საკმარისი თანხა.")
            return
        
        # არსებული ბალანსის შემცირება
        accounts[username]["balance"] -= gel_amount

        # მონაცემების შენახვა
        save_accounts(accounts)

        print("მითითებული თანხა წარმატებით გაიტანეთ.")
        print ()
        if currency == "1":
            print(f"გატანილია {amount} ლარი.")
            print ()
        elif currency == "2":
            print(f"გატანილია {amount} დოლარი ({gel_amount:.2f} ლარი).")
            print ()
        else:
            print(f"გატანილია {amount} ევრო ({gel_amount:.2f} ლარი).")
            print ()
            
        print (f"თქვენი ბალანსი შეადგენს: {accounts[username]['balance']} ლარს")

    except ValueError:
        print("მითითებული მონაცემები არასწორია")

# მთავარ მენიუში დაბრუნების ფუნქცია
def back_to_menu():
    while True:
        print()
        print("1. მთავარ მენიუში დაბრუნება")
        print("2. სისტემიდან გამოსვლა")
        print()

        choice = input("გთხოვთ აირჩიეთ სასურველი ოპერაციის შესაბამისი ციფრი: ")

        if choice == "1":
            return
        elif choice == "2":
            print()
            print("თქვენ გამოხვედით პროგრამიდან. ნახვამდის!")
            sys.exit()
        else:
            print()
            print("არასწორი არჩევანი. გთხოვთ აირჩიეთ 1 ან 2")

# ფაილიდან მონაცემების ჩატვირთვა
accounts = load_accounts()

# ბანკომატის მთავარი მენიუ
while True:
    print("=======================")
    print("====== ბანკომატი ======")
    print("=======================")
    print()
    print("1. რეგისტრაცია")
    print()
    print("2. ავტორიზაცია")
    print()
    print("3. გამოსვლა")
    print()

    # მომხმარებლის არჩევანის ჩაწერა
    choice = input("აირჩიეთ შესაბამისი ციფრი: ")

    # რეგისტრაციის გამოტანა
    if choice == "1":
        print()
        register(accounts)
    
    # ავტორიზაციის გამოტანა
    elif choice == "2":
        print()
        current_user = login(accounts)
        if current_user:
            while True:
                print("\\n------ მენიუ ------")
                print("1. ბალანსი")
                print("2. თანხის შეტანა")
                print("3. თანხის გატანა")
                print("4. გამოსვლა")

                # მომხმარებლის არჩევანის ჩაწერა
                print()
                option = input("აირჩიეთ შესაბამისი ციფრი: ")

                # ბალანსის გამოტანა
                print ()
                if option == "1":
                    check_balance(accounts, current_user)
                    back_to_menu()

                # თანხის შეტანის გამოტანა
                elif option == "2":
                    deposit(accounts, current_user)
                    back_to_menu()
                
                # თანხის გატანის გამოტანა
                elif option == "3":
                    withdraw(accounts, current_user)
                    back_to_menu()
                
                # პროგრამიდან გამოსვლა
                elif option == "4":
                    print()
                    print("თქვენ გამოხვედით პროგრამიდან,ნახვამდის!")
                    sys.exit()
                else:
                    print()
                    print("არასწორი არჩევანი, გთხოვთ აირჩიეთ 1-დან 4-მდე.")
    
    # პროგრამიდან გამოსვლა
    elif choice == "3":
        print()
        print("თქვენ გამოხვედით პროგრამიდან, ნახვამდის!")
        break
    
    else:
        print ()
        print("არასწორი არჩევანი, გთხოვთ აირჩიეთ 1-დან 3-მდე.")
        print ()
"""

# ფაილში ჩაწერა მთელი იმ კოდის, რაც მოთავსებულია სამმაგ ბრჭყალებში
with open(file_name, "w", encoding="utf-8") as file:
    file.write(cashpoint_code)

###===============================================================================================================###

# დავალება 5 - სტუდენტების მართვის სისტემა

# შექმენით კონსოლის აპლიკაცია რომელიც წარმოადგენს სტუდენტის მართვის
# მარტივ სისტემას ობიექტზე ორიენტირებული პროგრამირების პრინციპების გამოყენებით.
# სისტემამ მომხმარებელს უნდა მისცეს საშუალება განახორციელოს ძირითადი ოპერაციები,
# რომლებიც დაკავშირებულია სტუდენტის ინფორმაციასთან. თითოეულ სტუდენტს უნდა
# ჰქონდეს ისეთი ატრიბუტები, როგორიცაა სახელი, სიის ნომერი და შეფასება.

# 1. სტუდენტური კლასი:
# • შექმენით სტუდენტური კლასი შემდეგი ატრიბუტებით:
#     o Name Name (string) - სახელი
#     o Roll Number (int) - სიის ნომერი
#     o Grade (char) - შეფასება.

# 2. კონსოლის აპლიკაცია:
# • კონსოლის აპლიკაციის შემუშავება რომელიც მომხმარებელს მისცემს საშუალებას იურთიერთოს სტუდენტთა მართვის სისტემასთან.

# 3. მენიუს სისტემა:
# • მენიუს ჩვენება შემდეგი პარამეტრებით:
#     o ახალი სტუდენტის დამატება
#     o ყველა სტუდენტის ნახვა
#     o სტუდენტის ძებნა ნომრის მიხედვით
#     o მოსწავლის შეფასების განახლება
#     o გასვლა

# 4. ფუნქციონალობა:
# • ახალი სტუდენტის დამატება:
#     o სთხოვეთ მომხმარებელს შეიყვანოს მოსწავლის სახელი, სიის ნომერი და
#     შეფასება.
#     o შექმენით ახალი სტუდენტური ობიექტი და დაამატეთ ის სტუდენტების
#     სიაში.
# • ყველა სტუდენტის ნახვა:
#     o სისტემაში ყველა სტუდენტის დეტალების ჩვენება.
# • მოძებნეთ სტუდენტი ნომრის მიხედვით:
#     o შესთავაზეთ მომხმარებელს შეიყვანოს სიის ნომერი.
#     o მოძებნეთ სტუდენტი მითითებული ნომრით და აჩვენეთ მათი დეტალები.
# • განაახლეთ მოსწავლის შეფასება:
#     o შესთავაზეთ მომხმარებელს შეიყვანოს იმ სტუდენტის სიის ნომერი, რომლის
#     შეფასებაც განახლებას საჭიროებს.
#     o ნება მიეცით მომხმარებელს განაახლოს შეფასება მითითებული
#     სტუდენტისთვის.
# • გასვლა:
#     o შეწყვიტე პროგრამა.

# 5. ობიექტზე ორიენტირებული პრინციპები:
# • საჭიროების შემთხვევაში გამოიყენეთ ინკაფსულაცია, მემკვიდრეობა და პოლიმორფიზმი.

# 6. ვალიდაცია
# • განახორციელეთ შეყვანის ვალიდაცია, რათა დარწმუნდეთ, რომ მომხმარებელი
# შეიყვანს ვალიდურ ინფორმაციას.

# 7. პროექტში გამოყენებული უნდა იყოს სხვადასხვა ტიპის ცვლადები, პროექტში გამოყენებული უნდა იყოს პირობითი და ციკლის ოპერატორები
# პროექტში გამოყენებული უნდა იყოს მასივები, პროექტში სტუდენტს შექმნილი უნდა ჰქონდეს სამომხმარებლო ფუნქციები, კოდის ყველა მოდული დაკომენტარებული უნდა იყოს.
import os

# საქაღალდის და ფაილის შექმნა
folder = "project_5"
file = "student_management.py"

os.makedirs(folder, exist_ok=True)
file_name = os.path.join(folder, file)

# ახალ ფაილში გადასატანი Python კოდის ტექსტი Raw String ფორმატში
student_management_code = r"""from faker import Faker
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
            "grade": choice(["A", "B", "C", "D", "E", "F"])
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
        self._name = validate_name (value)

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
            raise ValueError(f"არასწორი შეფასება! უნდა იყოს ერთ-ერთი შემდეგიდან: {', '.join(valid_grades)}")
            
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
        #ობიექტის შექმნისთანავე ტვირთავს მონაცემებს JSON-დან
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
                        student["name"],
                        student["roll_number"],
                        student["grade"]
                    )
                    )
                except ValueError as e:
                    print(e)
                    continue
                    
    # მიმდინარე სტუდენტების სიის JSON ფაილში შენახვის ფუნქცია 
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

    #ახალი სტუდენტის დამატების ფუნქცია     
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
            print (f"სტუდენტი {name} წარმატებით დამატებულია")
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
                print ()
                print(f"შეცდომა: სტუდენტს {student.name} უკვე აქვს შეფასება {formatted_grade}! შეფასება ვერ განახლდება.")
                print ()
                return False
            try:
                student.grade = formatted_grade
                self.save_to_json()
                print()
                print(f"შეფასება წარმატებით განახლდა, {student.name}ს შეფასება უკვე არის {student.grade}")
                return True
            except ValueError:
                print()
                print("შეცდომა: გთხოვთ შეიყვანოთ შემდეგი ნიშნებიდან ერთ-ერთი A, B, C, D, E, F")
                print()
                return False

        print("სტუდენტი ვერ მოიძებნა.")
        return False

# დამხმარე ფუნქცია მომხმარებლისგან მთელი რიცხვის უსაფრთხოდ მისაღებად
def get_valid_int(prompt):
    while True:
        try:
            value = int (input(prompt))
            return value
        except ValueError:
            print()
            print("შეიყვანეთ მხოლოდ მთელი რიცხვი 1-დან 100-მდე")
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
        raise ValueError(
            "გთხოვთ შეიყვანოთ სწორი სახელი და გვარი"
        )

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
            roll_num = get_valid_int("შეიყვანეთ სიის ნომერი: ")
            
            print()
            while True:
                grade = input("შეიყვანეთ ერთ-ერთი შეფასება (A, B, C, D, E, F): ").strip().upper()

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

        #სტუდენტის ძებნა ნომრით
        elif choice == "3":
            roll_num = get_valid_int("შეიყვანეთ საძიებო სტუდენტის სიის ნომერი: ")
            print ()
            student = system.get_student_by_roll_number(roll_num)
            if student:
                print("ნაპოვნია სტუდენტი მითითებული სიითი ნომრით:")
                print("-" * 45)
                print()
                print(student)
            else:
                print(f"სტუდენტი ნომრით {roll_num} ვერ მოიძებნა, გთხოვთ შეიყვანოთ სიითი ნომერი 1-დან 100-მდე.")

        # სტუდენტის შეფასების შეცვლა
        elif choice == "4":
            while True:
                roll_num = get_valid_int("შეიყვანეთ სტუდენტის სიის ნომერი შეფასების შესაცვლელად: ")
                student = system.get_student_by_roll_number(roll_num)
                if student:
                    print()
                    print(f"თქვენს მიერ არჩეული სტუდენტია: {student.name} (მიმდინარე შეფასება: {student.grade})")
                    print()
                    new_grade = input("შეიყვანეთ ახალი შეფასება: ").strip()
                    if system.update_student_grade(roll_num, new_grade):
                        break
                else:
                    print(f"სტუდენტი ნომრით {roll_num} ვერ მოიძებნა, გთხოვთ შეიყვანოთ სიითი ნომერი 1-დან 100-მდე.")
                    break
        
        # გამოსვლა პროგრამიდან
        elif choice == "5":
            print("პროგრამა დასრულებულია. ნახვამდის!")
            break
        else:
            print("თქვენ არასწორად აირჩიეთ. გთხოვთ აირჩიოთ ციფრი 1-დან 5-მდე.")

# პროგრამის გაშვება
main_menu()
"""
# კოდის ჩაწერა შესაბამის ფაილში
with open(file_name, "w", encoding="utf-8") as file:
    file.write(student_management_code)
