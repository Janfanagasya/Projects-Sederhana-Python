import OPERASI  # package yang saya bikin
import os

os.system('cls')

#main menu

print("="*30)
print("\nSelamat datang di Tabel Angka\n")
print(("="*30)+"\n")
print("-"*30)
print("Pilih nomor operasi")
print("1. Pertambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("-"*30)

chose = input("Pilih nomor operasi angka [1, 2, 3, 4]: ")

match chose:
    case "1": OPERASI.pertambahan()
    case "2": OPERASI.pengurangan() #konsep dari tabel pengurangan ini mungkin kurang jelas, jadi bingung bagus nya gimana :>
    case "3": OPERASI.perkalian()
    case "4": OPERASI.pembagian()
    case _: 
        print("Nomor tidak valid")
