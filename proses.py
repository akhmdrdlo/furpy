def hitung(a,b,operator):
    if(operator==1):
        hasil = a+b
        return hasil
    elif(operator==2):
        hasil = a-b
        return hasil
    elif(operator==3):
        hasil = a*b
        return hasil
    elif(operator==4):
        hasil = a/b
        return hasil 
    else:
        print("Tidak ada operator yang kamu maksud!!")

def konvSuhu(klasSuhu,suhu,konv):
    if(klasSuhu=="c"):
        awal = "Celcius"
        if(konv==1):
            hasil = suhu*4/5
            klasSuhu = "Reamur"
        elif(konv==2):
            hasil = suhu*9/5 + 32
            klasSuhu = "Fahrenheit"
        elif(konv==3):
            hasil = suhu+273
            klasSuhu = "Kelvin"   
        else:
            print("Tidak ada konversi Celcius yang kamu maksud!!")
        return hasil,klasSuhu,awal
    elif(klasSuhu=="r"):
        awal = "Reamur"
        if(konv==1):
            hasil = suhu*5/4
            klasSuhu = "Celcius"
        elif(konv==2):
            hasil = suhu*9/4 + 32
            klasSuhu = "Fahrenheit"
        elif(konv==3):
            hasil = suhu*5/4+273
            klasSuhu = "Kelvin"   
        else:
            print("Tidak ada konversi Reamur yang kamu maksud!!")
        return hasil,klasSuhu,awal
    elif(klasSuhu=="f"):
        awal = "Fahrenheit"
        if(konv==1):
            hasil = (suhu-32)*5/9
            klasSuhu = "Celcius"
        elif(konv==2):
            hasil = (suhu-32)*4/9
            klasSuhu = "Reamur"
        elif(konv==3):
            hasil = (suhu-32)*5/9+273
            klasSuhu = "Kelvin"  
        else:
            print("Tidak ada konversi Fahrenheit yang kamu maksud!!")
        return hasil,klasSuhu,awal
    elif(klasSuhu=="k"):
        awal = "Kelvin"
        if(konv==1):
            hasil = suhu-273
            klasSuhu = "Celcius"
        elif(konv==2):
            hasil = (suhu-273)*4/5
            klasSuhu = "Reamur"
        elif(konv==3):
            hasil = (suhu-273)*9/5+32
            klasSuhu = "Fahrenheit"   
        else:
            print("Tidak ada konversi Kelvin yang kamu maksud!!")   
        return hasil,klasSuhu,awal

    def fisika(pilih):
        if(pilih == 1):
            print("")