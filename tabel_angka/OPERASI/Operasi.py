from . view import tampilan     # mengambil fungsi dari module view yang dibikin

def pertambahan():
    tampilan('pertambahan')
    benar = True
    while benar:
        while True:
            try:
         
                radius = int(input("Masukkan angka: "))
                if isinstance(radius, int):
                    break
            except ValueError:
                print("Angka tidak valid")
        
        
        for i in range(1, radius+1):
            print("-"*15)
            for j in range(1, radius+1):
                hasil = i + j
                print(f"{i} + {j} = {hasil}")
            print("-"*15)
            
        def akhir(berhenti:str) --> str: #untuk memastikan apakah memilih y atau n
            if berhenti == "n" or berhenti == "N":
                berhenti = True
                return berhenti
            elif berhenti == "y" or berhenti == "Y":
                return False
            else:
                print("Inputan tidak valid")
     
        #mengecek apakah ingin dilanjut atau tidak
        while benar:
            lanjut = input("Apakah ingin lanjut(y/n)?: ")
            if akhir(lanjut) == True:
                benar = False
            else:
                break


# sama seperti sebelum nya hanya beda di operasi nya
def pengurangan(): # untuk output dari tabel pengurangan sedikit kurang jelas, karena saya tidak tahu bagus nya gimana :v
    tampilan('pengurangan')
    benar = True
    while benar:
        while True:
            try:
         
                radius = int(input("Masukkan angka: "))
                if isinstance(radius, int):
                    break
            except ValueError:
                print("Angka tidak valid")
        
        
        for i in range(1, radius+1):
            print("-"*15)
            for j in range(1, radius+1):
                hasil = i - j
                print(f"{i} - {j} = {hasil}")
            print("-"*15)
            
        def akhir(berhenti):
            if berhenti == "n" or berhenti == "N":
                berhenti = True
                return berhenti
            elif berhenti == "y" or berhenti == "Y":
                return False
            else:
                print("Inputan tidak valid")
     
        while benar:
            lanjut = input("Apakah ingin lanjut(y/n)?: ")
            if akhir(lanjut) == True:
                benar = False
            else:
                break
                
def perkalian():
    tampilan('perkalian')
    benar = True
    while benar:
        while True:
            try:
         
                radius = int(input("Masukkan angka: "))
                if isinstance(radius, int):
                    break
            except ValueError:
                print("Angka tidak valid")
        
        
        for i in range(1, radius+1):
            print("-"*15)
            for j in range(1, radius+1):
                hasil = i * j
                print(f"{i} x {j} = {hasil}")
            print("-"*15)
            
        def akhir(berhenti):
            if berhenti == "n" or berhenti == "N":
                berhenti = True
                return berhenti
            elif berhenti == "y" or berhenti == "Y":
                return False
            else:
                print("Inputan tidak valid")
     
        while benar:
            lanjut = input("Apakah ingin lanjut(y/n)?: ")
            if akhir(lanjut) == True:
                benar = False
            else:
                break
                
def pembagian():
    tampilan('pembagian')
    benar = True
    while benar:
        while True:
            try:
         
                radius = int(input("Masukkan angka: "))
                if isinstance(radius, int):
                    break
            except ValueError:
                print("Angka tidak valid")
        
        
        for i in range(1, radius+1):
            print("-"*15)
            for j in range(1, radius+1):
                hasil = i / j
                print(f"{i} / {j} = {hasil}")
            print("-"*15)
            
        def akhir(berhenti):
            if berhenti == "n" or berhenti == "N":
                berhenti = True
                return berhenti
            elif berhenti == "y" or berhenti == "Y":
                return False
            else:
                print("Inputan tidak valid")
     
        while benar:
            lanjut = input("Apakah ingin lanjut(y/n)?: ")
            if akhir(lanjut) == True:
                benar = False
            else:
                break