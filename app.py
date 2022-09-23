
import time
print("Bienvenido al Hòroscopo")
print("#######################")

def read_file(app):
    file = open("signs/"+ app,"r", encoding="UTF-8")
    for line in file:
        print(line)

def menu():
    print("seleccionada cual es tu signo")
    print("1","Acuario")
    print("2","Aries")
    print("3","Cancer")
    print("4","Capricornio")
    print("5","Geminis")
    print("6","Leo")
    print("7","Libra")
    print("8","Piscis")
    print("9","Sagitarios")
    print("10","Escorpiòn")
    print("11","Tauro")
    print("12","Virgo")
    print("13","Color de la Suerte")
    print("0","salir")
    print("##################")

user_input =""


while user_input !="exit":
    menu()

    user_input = input()
    if user_input == "1":
        read_file = ("aguarius.txt")
    elif user_input == "2":
        read_file = ("aries.txt")
    elif user_input == "3":
        read_file = ("cancer.txt")
    elif user_input =="4":
        read_file = ("capricornus.txt")
    elif user_input == "5":
        read_file = ("Geminis.txt")   
    elif user_input == "6":
        read_file = ("leo.txt")
    elif user_input == "7":
        read_file = ("libra.txt")   
    elif user_input == "8":
        read_file = ("pisces.txt")
    elif user_input == "9":
        read_file = ("sagittarius.txt")   
    elif user_input == "10":
        read_file = ("scorpio.txt")  
    elif user_input == "11":
        read_file = ("taurus.txt")   
    elif user_input == "12":
        read_file = ("virgo.txt")
    else:
        time.sleep(0.3)
        print("opciòn incorrecta")


