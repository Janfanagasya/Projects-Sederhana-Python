import GAME
import os

os.system('cls')

# main menu
try:
    print("="*20)
    print("GAME TEBAK ANGKA")
    print("="*20)

    # mulai game atau tidak
    while True:
        confirm = input("Mulai permainan? (y/n): ")
        
        if confirm == "n" or confirm == "N":
            break
        elif confirm == "y" or confirm == "Y":
            GAME.gamepy() 
        else:
            print("input tidak valid")
            
    print("Program berakhir, terimakasih")
except KeyboardInterrupt:
    print("\nKeluar dari program")    

