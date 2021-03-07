import random as rand #import randint
import sys
import os
os.system("cls" if os.name == "nt" else "clear")
while True:
    print("Mint 1.1|Публичная Бета Версия.")
    print("Напишите 'помощь' чтобы посмотреть список команд.")
    print("Чтобы команда выполнилась, нажмите Enter.")
    print("-----------------------")
    print("1-Низкий уровень.")
    print("2-Средний уровень.")
    print("3-Высокий уровень.")
    print("у-д-Умножение/деление.")
    print("Какой уровень?")
    s=input()
    if s =="выйти":
        sys.exit()
    elif s =="обновление":
        print("Этот патч исправил ошибки в меню и выпустил программу под лицензией GNU GPLv3.")
        print("Нажмите Enter для выхода в меню.")
        input()
        os.system("cls" if os.name == "nt" else "clear")
    elif s =="лицензия":
        print("(Это свободная программа: вы можете перераспространять ее и/или изменять ее на условиях Стандартной общественной лицензии GNU в том виде, в каком она была опубликована Фондом свободного программного обеспечения; либо версии 3 лицензии, либо (по вашему выбору) любой более поздней версии. Эта программа распространяется в надежде, что она будет полезной, но БЕЗО ВСЯКИХ ГАРАНТИЙ; даже без неявной гарантии ТОВАРНОГО ВИДА или ПРИГОДНОСТИ ДЛЯ ОПРЕДЕЛЕННЫХ ЦЕЛЕЙ. Подробнее см. в Стандартной общественной лицензии GNU. Вы должны были получить копию Стандартной общественной лицензии GNU вместе с этой программой. Если это не так, см. <https://www.gnu.org/licenses/>.")
        print("Нажмите Enter для выхода в меню.")
        input()
        os.system("cls" if os.name == "nt" else "clear")
    elif s =="помощь":
        print("-----------------------------")
        print("Команды:")
        print("1-Низкий уровень.")
        print("2-Средний уровень.")
        print("3-Высокий уровень.")
        print("у-д-Умножение/деление.")
        print("инфо-Информация о программе.")
        print("выйти-Закрыть программу.")
        print("назад-Назад в меню.")
        print("обновление-Новое в этой версии.")
        print("лицензия-уведомление о лицензии")
        print("")
        print("Нажмите Enter для выхода в меню.")
        input()
    elif s =="инфо":
        print("Программа написана Михаилом Пушкином (GlowSprute) и опубликована под лицензией GNU GPLv3(смотрите подробнее о лицензии по команде лицензия).")
        print("Моя почта: mike152010@outlook.com")
        print("Нажмите Enter для выхода в меню.")
        input()
        os.system("cls" if os.name == "nt" else "clear")
    elif s =="1":      # Первый уровень.
        while True:
            a=rand.randint(1,50)
            b=rand.randint(1,50)
            if a > b:
                r=rand.choice(('+','-'))
            else:
                r="+"
            if r =="+":               
                print(f"Сложи {a} и {b}")
                c=a + b
            elif r =="-":
                print(f"Вычти {a} и {b}")
                c=a - b
            s1=input("= ")
            if s1.isnumeric():
                s1=int(s1)
                if c == s1:      # Проверка
                    print("Молодец!")
                else:
                    print("Неправильно!")
            elif s1 =="выйти":
                sys.exit()
            elif s1 =="назад":
                os.system("cls" if os.name == "nt" else "clear")
                break
            else:
                print("Это не цифра!")
    elif s =="2":
        while True:
            a=rand.randint(1,500)
            b=rand.randint(1,500)
            if a > b:
                r=rand.choice(('+','-'))
            else:
                r="+"
            if r =="+":               
                print(f"Сложи {a} и {b}")
                c=a + b
            elif r =="-":
                print(f"Вычти {a} и {b}")
                c=a - b
            s1=input("= ")
            if s1.isnumeric():
                s1=int(s1)
                if c == s1:      # Проверка
                    print("Молодец!")
                else:
                    print("Неправильно!")
            elif s1 =="выйти":
                sys.exit()
            elif s1 =="назад":
                os.system("cls" if os.name == "nt" else "clear")
                break
            else:
                print("Это не цифра!")
    elif s =="3":
        while True:
            a=rand.randint(1,1000)
            b=rand.randint(1,1000)
            if a > b:
                r=rand.choice(('+','-'))
            else:
                r="+"
            if r =="+":               
                print(f"Сложи {a} и {b}")
                c=a + b
            elif r =="-":
                print(f"Вычти {a} и {b}")
                c=a - b
            s1=input("= ")
            if s1.isnumeric():
                s1=int(s1)
                if c == s1:      # Проверка
                    print("Молодец!")
                else:
                    print("Неправильно!")
            elif s1 =="выйти":
                sys.exit()
            elif s1 =="назад":
                os.system("cls" if os.name == "nt" else "clear")
                break
            else:
                print("Это не цифра!")
    elif s =="у-д":
        while True:
            a=rand.randint(1,90)
            b=rand.randint(1,10)
            if a > b:
                r=rand.choice(('*','/'))
            else:
                r="*"
            if r =="*":               
                print(f"Умножь {a} и {b}")
                c=a * b
            elif r =="/":
                print(f"Раздели {a} и {b}")
                c=a / b
            s1=input("= ")
            if s1.isnumeric():
                s1=int(s1)
                if c == s1:      # Проверка
                    print("Молодец!")
                else:
                    print("Неправильно!")
            elif s1 =="выйти":
                sys.exit()
            elif s1 =="назад":
                os.system("cls" if os.name == "nt" else "clear")
                break
            else:
                print("Это не цифра!")
    else:
        print("Такой команды нет.")
        print("Нажмите Enter для выхода в меню.")
        input()
        os.system("cls" if os.name == "nt" else "clear")