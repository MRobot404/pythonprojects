import random

options = ('piedra','papel','tijera')
user_option=str
menu: int = 0
menu = int(input('1. Para seguir 2. para parar '))
while menu != 2:
    if menu == 1:
        

        user_option = input('piedra papel o tijera =>')
        user_option = user_option.lower()

        if not user_option in options:
            print('Esta opcion no es valida')

        computer_options=random.choice(options)

        print('El usuario eligio:' ,   user_option)
        print('La computadora eligio', computer_options)

        if user_option==computer_options:
            print('Empate')
        elif user_option=='piedra':
            if computer_options=='tijera':
                print('Piedra gana a tijera')
                print('Usuario gana')
            else:
                print('Usuario pierde')
        elif user_option=='papel':
            if computer_options=='piedra':
                print('Papel cubre piedra ')
                print('Usuario Gana')
            else:
                print('Usuario pierde')
        else:
            if computer_options=='papel':
                print('Tijera corta papel')
                print('Usuario gana')
            else:
                print('Usuario pierde')
    menu = int(input('1. Para seguir 2. para parar '))