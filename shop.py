import os

def shop(player_name, player_hp, player_money, player_potions):
    while True:
        os.system("cls")
        print(f"{player_name} приехал в лавку алхимика.")
        print(f"здоровье: {player_hp}")
        print(f"деньги: {player_money}")
        print(f"зелья: {player_potions}")
        print("1 - Купить зелье за 200 монет")
        print("2 - Поехать к камню")

        answer = input("Введите номер варианта и нажмите ENTER: ")

        if answer == "1":
            if player_money >= 200:
                player_money -= 200
                player_potions += 1
                print(f"{player_name} купил зелье")
            else:
                print("У вас нет столько монет!")
                input("ENTER - дальше")
        elif answer == "2":
            print("Уехал к камню")
            break