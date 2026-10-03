import random
import os

os.system('cls')

#fungsi untuk memulai game
def gamepy():
    answer = "?"
    print("="*25)
    print(f"Angka = {answer}")
    print("="*25)
    
    objek = random.randint(1, 100) # jawaban dari game
    try:
        while True:
            try:
                input_angka = int(input("Tebak angka dari 1 sampai 100: "))
            except ValueError:
                print("Input harus bilangan bulat positif integer")
                
            if input_angka == objek:
                
                print("\nSelamat anda benar menebaknya")
                print("="*25)
                print(f"Angka = {objek}")
                print("="*25)
                
                #memastikan apakah game nya ingin dilanjutkan
                lanjutan = input("Ingin lanjut (y/n)?: ")
                if lanjutan == "n" or lanjutan == "N":
                    break
                elif lanjutan == "y" or lanjutan == "Y":
                    pass
                else:
                    print("input tidak valid")
            
            #hint dan mengecek apakah angka yang dicari sudah semakin deket
            if abs(input_angka - objek) < 5:
                print("Angka sudah dekat")
            if input_angka < objek:
                print("Angka lebih besar")
            if input_angka > objek:
                print("Angka lebih kecil")
                
    except KeyboardInterrupt:
        print("\nKeluar dari game")
 
    
    
    