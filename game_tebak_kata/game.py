import os
import random

os.system("cls")


# fungsi untuk memulai game
def main_game(kategori: str, daftar_kata: list) --> str:
    turn = 7
    objek = random.choice(daftar_kata)

    while turn > 0:
        tebak = input(f"Tebak {kategori} apa? : ").strip()

        if tebak.lower() == objek:
            print(f"\nSelamat! Anda berhasil menebak kata '{objek.title()}'")
            break
        else:
            turn -= 1
            if turn > 0:
                print(
                    f"Anda salah, Anda masih punya {turn} kesempatan lagi!!"
                )
            else:
                print(
                    f"\nAnda telah gagal, jawabannya adalah: {objek.title()}"
                )

    print("Game telah selesai.\n")


# Main Menu
title = "Selamat Datang di Game Tebak Kata"
print(f"{title.upper():*^40}\n")

print("Pilih kategori yang ada:")
print("""
========================
1. Buah-buahan
2. Sayur-sayuran
3. Bahasa Pemrograman
========================
""")

pilih = input("No.: ")

# list kategori game tebak kata
daftar_buah = [
    "apel",
    "pisang",
    "lemon",
    "semangka",
    "leci",
    "rambutan",
    "durian",
    "anggur",
    "nanas",
    "nangka",
]
daftar_sayur = [
    "bayam",
    "kangkung",
    "kol",
    "selada",
    "kacang panjang",
    "toge",
    "seledri",
    "kubis",
    "kacang polong",
    "buncis",
]
daftar_pemrograman = [
    "python",
    "javascript",
    "java",
    "c++",
    "c#",
    "c",
    "node.js",
    "ruby",
    "php",
    "kotlin",
]

# pilih opsi kategori game
match pilih:
    case "1":
        main_game("buah", daftar_buah)
    case "2":
        main_game("sayur", daftar_sayur)
    case "3":
        main_game("bahasa pemrograman", daftar_pemrograman)
    case _:
        print("Input tidak valid!")