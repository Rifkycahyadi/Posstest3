import os

while True:
    try:
        os.system("cls" if os.name == "nt" else "clear")

        NIM = int(input("masukkan NIM anda ditambah dengan 10: "))
        n = 1 
        a = 1
        while n <= NIM:
            print(a)
            a += 1
            if a == 10:
                a -= 9
            n += 1
        break
    except ValueError:
        print("Maaf NIM anda tidak valid")