import main
from tools import kalkulator, rumus

def back_menu_dasar():
    back_menu_dasar = int(input('\nKetik 1 untuk kembali ke menu hitung-hitungan dasar kalkulator DilMath, ketik 2 untuk kembali ke menu Kalkulator DilMath, dan ketik 3 untuk kembali ke menu utama: '))
    
    while back_menu_dasar > 3:
        back_menu_dasar = int(input('Angka yang kamu masukan tidak valid! Silahkan ketikan ulang pilihan kamu: '))
        
    if back_menu_dasar == 1:
        math_dasar()
    elif back_menu_dasar == 2:
        kalkulator.start()
    elif back_menu_dasar == 3:
        print('\nTerimakasih telah mengunjungi DilMath')
        main.main()
            
def math_dasar():
    input_math_dasar = int(input('\nMenu Hitung-hitungan dasar DilMath:\n1. Hitung penjumlahan\n2. Hitung Pengurangan\n3. Hitung perkalian\n4. Hitung Pembagian\n5. Kembali ke menu Kalkulator DilMath\n6. Kembali ke menu utama\n\nSilahkan pilih menunya: '))
        
    while input_math_dasar > 6:
        input_math_dasar = int(input('Mohon maaf menu perhitungan dasar hanya sampai 6, silahkan ketikan ulang nomor menu yang akan kamu pilih: '))
        
    if input_math_dasar == 1:
        rumus.hitung_penjumlahan()
        back_menu_dasar()
    elif input_math_dasar == 2:
        rumus.hitung_pengurangan()
        back_menu_dasar()
    elif input_math_dasar == 3:
        rumus.hitung_perkalian()
        back_menu_dasar()
    elif input_math_dasar == 4:
        rumus.hitung_pembagian()
        back_menu_dasar()
    elif input_math_dasar == 5:
        kalkulator.start()
    elif input_math_dasar == 6:
        print('\nTerimakasih telah mengunjungi DilMath')
        main.main()

def back_menu_hLuas():
    back_menu_hLuas = int(input('\nKetik 1 untuk kembali ke menu Hitung Luas kalkulator DilMath, ketik 2 untuk kembali ke menu Kalkulator DilMath, dan ketik 3 untuk kembali ke menu utama: '))
    
    while back_menu_hLuas > 3:
        back_menu_hLuas = int(input('Angka yang kamu masukan tidak valid! Silahkan ketikan ulang pilihan kamu: '))
        
    if back_menu_hLuas == 1:
        math_hLuas()
    elif back_menu_hLuas == 2:
        kalkulator.start()
    elif back_menu_hLuas == 3:
        print('\nTerimakasih telah mengunjungi DilMath')
        main.main()
            
def math_hLuas():
    input_math_hLuas = int(input('\nMenu Menghitung Luas Bangun Datar DilMath:\n1. Hitung luas segitiga\n2. Hitung luas jajar genjang\n3. Hitung luas persegi panjang\n4. Hitung luas persegi\n5. Hitung luas lingkaran\n6. Kembali ke menu Kalkulator DilMath\n7. Kembali ke menu utama\n\nSilahkan pilih menunya: '))
        
    while input_math_hLuas > 7:
        input_math_hLuas = int(input('Mohon maaf menu hitung luas bangun datar hanya sampai 7, silahkan ketikan ulang nomor menu yang akan kamu pilih: '))
        
    if input_math_hLuas == 1:
        rumus.hitung_lSegitiga()
        back_menu_hLuas()
    elif input_math_hLuas == 2:
        rumus.hitung_lJgenjang()
        back_menu_hLuas()
    elif input_math_hLuas == 3:
        rumus.hitung_lPpanjang()
        back_menu_hLuas()
    elif input_math_hLuas == 4:
        rumus.hitung_lPersegi()
        back_menu_hLuas()
    elif input_math_hLuas == 5:
        rumus.hitung_lLingkaran()
        back_menu_hLuas()
    elif input_math_hLuas == 6:
        kalkulator.start()
    elif input_math_hLuas == 7:
        print('\nTerimakasih telah mengunjungi DilMath')
        main.main()
    
def back_menu_hKel():
    back_menu_hKel = int(input('\nKetik 1 untuk kembali ke menu Hitung Keliling kalkulator DilMath, ketik 2 untuk kembali ke menu Kalkulator DilMath, dan ketik 3 untuk kembali ke menu utama: '))
    
    while back_menu_hKel > 3:
        back_menu_hKel = int(input('Angka yang kamu masukan tidak valid! Silahkan ketikan ulang pilihan kamu: '))
        
    if back_menu_hKel == 1:
        math_hKel()
    elif back_menu_hKel == 2:
        kalkulator.start()
    elif back_menu_hKel == 3:
        print('\nTerimakasih telah mengunjungi DilMath')
        main.main()
            
def math_hKel():
    input_math_hKel = int(input('\nMenu Menghitung Keliling Bangun Datar DilMath:\n1. Hitung keliling segitiga\n2. Hitung keliling jajar genjang\n3. Hitung keliling persegi panjang\n4. Hitung keliling persegi\n5. Hitung keliling lingkaran\n6. Kembali ke menu Kalkulator DilMath\n7. Kembali ke menu utama\n\nSilahkan pilih menunya: '))
        
    while input_math_hKel > 7:
        input_math_hKel = int(input('Mohon maaf menu hitung luas bangun datar hanya sampai 7, silahkan ketikan ulang nomor menu yang akan kamu pilih: '))
        
    if input_math_hKel == 1:
        rumus.hitung_kelSegitiga()
        back_menu_hKel()
    elif input_math_hKel == 2:
        rumus.hitung_kelJgenjang()
        back_menu_hKel()
    elif input_math_hKel == 3:
        rumus.hitung_kelPpanjang()
        back_menu_hKel()
    elif input_math_hKel == 4:
        rumus.hitung_kelPersegi()
        back_menu_hKel()
    elif input_math_hKel == 5:
        rumus.hitung_kelLingkaran()
        back_menu_hKel()
    elif input_math_hKel == 6:
        kalkulator.start()
    elif input_math_hKel == 7:
        print('\nTerimakasih telah mengunjungi DilMath')
        main.main()
            
if __name__ == '__main__':
    math_dasar()
    math_hLuas()
    math_hKel()