#კალკულატორი
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
