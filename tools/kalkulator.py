import main
from libs import welcome_massage
from tools import menukal

def start():
    welcome_massage()
    
    print('Selamat Datang di Kalkulator DILPY\n')
    
    user_input = int(input('Menu Kalkulator DilMath:\n1. Hitung-hitungan dasar\n2. Hitung luas bangun datar\n3. Hitung keliling bangun datar\n4. Kembali ke menu utama\n\nSilahkan pilih menunya: '))

    while user_input > 4:
        user_input = int(input('Mohon masukkan angka sesuai menu: '))

    if user_input == 1:
        menukal.math_dasar()
    elif user_input == 2:
        menukal.math_hLuas()
    elif user_input == 3:
        menukal.math_hKel()
    elif user_input == 4:
        print('\nTerimakasih telah mengunjungi DilMath')
        main.main()
    
if __name__ == '__main__':
    start()