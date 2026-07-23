import random

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
