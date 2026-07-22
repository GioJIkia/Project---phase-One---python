import os
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
        file.write("მომხმარებელი,ელ-ფოსტა,პაროლი,ბალანსი(ლარი)\n")

        # მეორე ხაზი - ტირეები
        file.write("---------------------------------------------------\n")

        # შემდეგი ხაზები - შენახული ინფორმაცია
        for username in accounts:
            email = accounts[username]["email"]
            password = accounts[username]["password"]
            balance = accounts[username]["balance"]

            file.write(f"{username},{email},{password},{balance}\n" )

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
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
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
    password_regex = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z\d]).{8,}$")

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
                print("\n------ მენიუ ------")
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
