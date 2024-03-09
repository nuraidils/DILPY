import random
import main
from libs import welcome_massage

def start():
    while True:
        bentuk_bak = "|_|"
        bak_kosong = [bentuk_bak] * 4

        dilpy_position = random.randint(1, 4)
        
        bak = bak_kosong.copy()
        bak[dilpy_position - 1] = "|^_^|"

        bak_kosong = ' '.join(bak_kosong)
        bak = ' '.join(bak)
        
        welcome_massage()
        
        print('Selamat Datang di Games DILPY\n')
        
        print(f'Coba perhatikan bak dibawah ini\n\n{bak_kosong}\n')

        pilihan_user = int(input(f"Menurutmu berada di bak nomor berapakah DILPY berada?? [1 /2 /3 /4]: "))

        while pilihan_user > 4:
            pilihan_user = int(input("Mohon maaf pilihan hanya sampai 4. Silahkan masukkan ulang pilihan: "))

        if pilihan_user == dilpy_position:
            print(f"\n{bak}\n\nSelamat kamu menang🥳🥳, DILPY berada di bak nomor {dilpy_position} dan pilihanmu adalah bak nomor {pilihan_user}.")
        else:
            print(f"\n{bak}\n\nMaaf kamu kalah😿😿, DILPY berada di bak nomor {dilpy_position} sedangkan kamu memilih bak nomor {pilihan_user}.")
            
        play_again = input("\n\nApakah kamu ingin bermain lagi?? [y/n]: ")
        
        if play_again == "y":
            start()
        elif play_again == "n":
            main.main()
        else:
            play_again = input("\nMohon ketikkan huruf y/n: ")

if __name__ == '__main__':
    start()
