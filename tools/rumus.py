
def hitung_penjumlahan():
        print('\nHitung penjumlahan ready!')
        angka_t1 = float(input('Masukkan angka pertama: '))
        angka_t2 = float(input('Masukkan angka kedua: '))
        penjumlahan = angka_t1 + angka_t2
        print('\nHasilnya adalah: ', penjumlahan)
        
def hitung_pengurangan():
    print('\nHitung pengurangan ready!')
    angka_k1 = float(input('Masukkan angka pertama: '))
    angka_k2 = float(input('Masukkan angka kedua: '))
    pengurangan = angka_k1 - angka_k2
    print('\nHasilnya adalah: ', pengurangan)

def hitung_perkalian():
    print('\nHitung perkalian ready!')
    angka_x1 = float(input('Masukkan angka pertama: '))
    angka_x2 = float(input('Masukkan angka kedua: '))
    perkalian = angka_x1 * angka_x2
    print('\nHasilnya adalah: ', perkalian)
    
def hitung_pembagian():
    print('\nHitung pembagian ready!')
    angka_b1 = float(input('Masukkan angka pertama: '))
    angka_b2 = float(input('Masukkan angka kedua: '))
    pembagian = angka_b1 / angka_b2
    print('\nHasilnya adalah: ', pembagian)
    
def hitung_lSegitiga():
    print('\nHIitung Luas Segitiga Ready!')
    alas_segitiga = float(input('Masukkan alas segitiga: '))
    tinggi_segitiga = float(input('Masukkan tinggi segitiga: '))
    luas_segitiga = 0.5 * (alas_segitiga * tinggi_segitiga)
    print('Luas segitiga adalah: ', luas_segitiga)
        
def hitung_lJgenjang():
    print('\nHIitung Luas Jajar Genjang Ready!')
    alas_jajargenjang = float(input('Masukkan alas jajar genjang: '))
    tinggi_jajargenjang = float(input('Masukkan tinggi jajar genjang: '))
    luas_jajargenjang = alas_jajargenjang * tinggi_jajargenjang
    print('Luas jajar genjang adalah: ', luas_jajargenjang)
    
def hitung_lPpanjang():
    print('\nHitung Luas Persegi Panjang Ready!')
    panjang_Ppanjang = float(input("Masukkan panjang persegi panjang: "))
    lebar_Ppanjang = float(input("Masukkan lebar persegi panjang: "))
    luas_Ppanjang = panjang_Ppanjang * lebar_Ppanjang
    print('Luas persegi panjang adalah: ', luas_Ppanjang)
    
def hitung_lLingkaran():
    print('\nHitung Luas Lingkaran Ready!')
    r = float(input("Masukkan jari jari: "))
    luas_lingkaran = 3.14 * (r**2)
    print('Luas lingkaran adalah: ', luas_lingkaran)
    
def hitung_kelSegitiga():
    print('\nHIitung Keliling Segitiga Ready!')
    a = float(input('Masukkan panjang sisi 1 segitiga: '))
    b = float(input('Masukkan panjang sisi 2 segitiga: '))
    c = float(input('Masukkan panjang sisi 3 segitiga: '))
    kel_segitiga = a + b + c
    print('Keliling segitiga adalah: ', kel_segitiga)
    
def hitung_kelJgenjang():
    print('\nHIitung Keliling Jajar Genjang Ready!')
    p_Jgenjang = float(input('Masukkan panjang jajar genjang: '))
    l_Jgenjang = float(input('Masukkan lebar jajar genjang: '))
    kel_Jgenjang = 2 * (p_Jgenjang + l_Jgenjang)
    print('Keliling jajar genjang adalah: ', kel_Jgenjang)
    
def hitung_kelPpanjang():
    print('\nHIitung Keliling Persegi Panjang Ready!')
    p_Ppanjang = float(input('Masukkan panjang persegi panjang: '))
    l_Ppanjang = float(input('Masukkan lebar persegi panjang: '))
    kel_Ppanjang = 2 * (p_Ppanjang + l_Ppanjang)
    print('Keliling persegi panjang adalah: ', kel_Ppanjang)
    
def hitung_kelPersegi():
    print('\nHIitung Keliling Persegi Ready!')
    s = float(input('Masukkan panjang sisi persegi: '))
    kel_persegi = 4 * s
    print('Keliling persegi adalah: ', kel_persegi)
    
def hitung_kelLingkaran():
    print('\nHIitung Keliling Lingkaran Ready!')
    r = float(input('Masukkan jari jari: '))
    kel_lingkaran = 2 * (3.14 * r)
    print('Keliling lingkaran adalah: ', kel_lingkaran)