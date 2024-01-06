from proses import hitung as math, konvSuhu

def kalkulator(pilih):
    print("\033[H\033[2J")
    print("Selamat datang di Kalkulator Sederhana MadPy!!\n1.Penjumlahan\n2.Pengurangan\n3.Perkalian\n4.Pembagian")

    operator = int(input("Masukkan operasi yang ingin dilakukan 1 s/d 4: "))
    a = float(input("Angka pertamanya adalah : "))
    b = float(input("Angka keduanya adalah : "))
    hasil = math(a,b,operator)
    print("Hasil dari operasi tersebut adalah {}".format(hasil))

def konversi(pilih):
    print("\033[H\033[2J")
    print("======================\nSelamat datang di Konversi Suhu Sederhana Madpy!!")
    print("Pilih klasifikasi suhu yang akan di konversi!! (misal Reamur atau Fahrenheit)")
    klasSuhu = input("Masukkan Klasifikasi Suhu yang ingin di ubah (C/R/F/K): ")
    
    if klasSuhu == "C" or klasSuhu == "c" or klasSuhu=="Celcius" or klasSuhu=="celcius":
        klasSuhu = "c"
        print("========================\nKlasifikasi Konversi Celcius\n1.Celcius -> Reamur\n2.Celcius -> Fahrenheit\n3.Celcius -> Kelvin")
        konv = int(input("Tentukan jenis konversi : "))
        suhu = float(input("Masukkan suhu (range -273 s/d 100): "))
    elif klasSuhu == "R" or klasSuhu == "r" or klasSuhu=="Reamur" or klasSuhu=="reamur":
        klasSuhu = "r"
        print("========================\nKlasifikasi Konversi Reamur\n1.Reamur -> Celcius\n2.Reamur -> Fahrenheit\n3.Reamur -> Kelvin")
        konv = int(input("Tentukan jenis konversi : "))
        suhu = float(input("Masukkan suhu (range -273 s/d 80) : "))
    elif klasSuhu == "F" or klasSuhu == "f" or klasSuhu=="Fahrenheit" or klasSuhu=="fahrenheit":
        klasSuhu = "f"
        print("========================\nKlasifikasi Konversi Fahrenheit\n1.Fahrenheit -> Celcius\n2.Fahrenheit -> Reamur\n3.Fahrenheit -> Kelvin")
        konv = int(input("Tentukan jenis konversi : "))
        suhu = float(input("Masukkan suhu (range -459 s/d 212): "))
    elif klasSuhu == "K" or klasSuhu == "k" or klasSuhu=="Kelvin" or klasSuhu=="kelvin":
        klasSuhu = "k"
        print("========================\nKlasifikasi Konversi Kelvin\n1.Kelvin -> Celcius\n2.Kelvin -> Reamur\n3.Kelvin -> Fahrenheit")
        konv = int(input("Tentukan jenis konversi : "))
        suhu = float(input("Masukkan suhu (range 0 s/d 100) : "))
    hasil,klasSuhu,awal = konvSuhu(klasSuhu,suhu,konv)
    print(f"Hasil dari konversi {awal} ke {klasSuhu} adalah {hasil}° {klasSuhu}")


#Tampilan utama
menu = True
while(menu==True):
    print("\033[H\033[2J")
    print("Selamat datang di Aplikasi Multifungsi Furpy!!\n1.Kalkulator Aritmatika\n2.Konversi Suhu")
    pilih = int(input("Kamu ingin menjelajah dimana? (1/2) : "))
    if(pilih == 1):
        menuArm = True
        while(menuArm == True):
            kalkulator(pilih)
            lanjut = input("Ingin menghitung lagi (y) atau Kembali ke menu(n)?")
            if lanjut == "y" or lanjut == "Y" or lanjut == "Ya" or lanjut == "ya":
                menuArm = True
            else:
                menuArm = False
            break
    elif(pilih == 2):
        menuSuhu = True
        while(menuSuhu == True):
            konversi(pilih)
            lanjut = input("Ingin mengkonversi lagi (y) atau Kembali ke menu(n)?")
            if lanjut == "y" or lanjut == "Y" or lanjut == "Ya" or lanjut == "ya":
                menuSuhu = True
            else:
                menuSuhu = False
            break
    lanjut = input("=====================================\nIngin melanjutkan berhitung(y) atau Keluar(n)?")
    if lanjut == "y" or lanjut == "Y" or lanjut == "Ya" or lanjut == "ya":
        menu = True
    else:
        menu = False