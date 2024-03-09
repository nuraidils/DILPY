import socket
from time import sleep

PC_NAME = socket.gethostname()

def welcome_massage():
    style = "*" * (len(PC_NAME) + 8)
    
    print(f'\n{style}')
    print(f"*** {PC_NAME} ***")
    print(style)
    print('''by : nuraidilss\n''')
    
def exit_program():
    print('\nProgram akan dihentikan terimakasih')
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('Program berhasil dihentikan')
    
if __name__ == '__main__':
    welcome_massage()
    exit_program()