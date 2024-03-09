from libs import welcome_massage, exit_program
from games import dilpy
from tools import kalkulator

def menu():
    user_option = int(input(f'Menu program di DILPY:\n1. Games DILPY\n2. Kalkulator DilMath\n3. Face Detection DilFace AI\n4. Exit Program\n\nSilahkan pilih [1 /2 /3 /4]: '))

    while user_option > 4:
        user_option = int(input('Mohon pilih sesuai menu: '))

    if user_option == 1:
        dilpy.start()
    elif user_option == 2:
        kalkulator.start()
    elif user_option == 3:
        print('maaf program sedang diperbaiki silahkan pilih menu lain!')
        main()
    elif user_option == 4:
        exit_program()

def main():
    welcome_massage()
    menu()
    
if __name__ == '__main__':
    main()
