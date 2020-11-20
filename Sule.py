import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("="*36)
print("\t---SELAMAT DATANG---")
print("\t      ---DI---")
print("\t  ---TOKO SULE---")
print("="*36)
nama = str(input("Masukkan nama anda: "))
def menu():
    print("Tersedia:")
    print("1. kue keju")
    print("2. kue coklat")
    pilih = input("pilih menu>>> ")
    
    if(pilih == "1"):
        jumlah_kue_keju()
    elif(pilih == "2"):
        jumlah_kue_coklat()
    else:
        print("Anda memilih menu yang salah")
        back_to_menu()

def back_to_menu():
    print("\n")
    input("Tekan Enter Untuk Kembali.....")
    menu()
def jumlah_kue_keju():
    clear_screen()
    kue_keju = 6000
    jumlah = int(input("Berapa kue keju yang akan anda dibeli: "))
    if(jumlah >=1) and (jumlah <=3):
        total_harga1 = (jumlah * kue_keju)
        print("Total harga adalah: "+str(total_harga1))
        print("Beli minimal 4 kue dan anda akan mendapatkan potongan harga")
        print("Terima kasih telah mampir")
    
    elif(jumlah >=4) and (jumlah >=15):
        total_harga1 = (jumlah * kue_keju * 90/100)
        print("Total harga adalah: "+str(total_harga1))
        print("Selamat anda mendapatkan potongan harga sebesar 10%")
        print("Terima kasih telah mampir")
    
    elif(jumlah >=16) and (jumlah <=25):
        total_harga1 = (jumlah * kue_keju * 85/100)
        print("Total harga adalah: "+str(total_harga1))
        print("Selamat anda mendapatkan potongan harga sebesar 15%")
        print("Terima kasih telah mampir")

    elif(jumlah == 0):
        total_harga1 = (jumlah * kue_keju)
        print("Total harga adalah: "+str(total_harga1))
        print("jumlah yang di masukkan tidak boleh 0")
        print("Silahkan kembali ke menu dan masukkan jumlah yang ingin anda beli")

    else:
        print("mohon maaf kami hanya menyediakan stok 25 kue saja")
        print("Terima kasih telah mampir")

def jumlah_kue_coklat():
    clear_screen()
    kue_coklat = 3500
    jumlah = int(input("Berapa kue coklat yang akan anda beli: "))
    if(jumlah >=1) and (jumlah <=4):
        total_harga2 = (jumlah * kue_coklat)
        print("Total harga adalah: "+str(total_harga2))
        print("Beli minimal 5 kue dan anda akan mendapatkan potongan harga")
        print("Terima kasih telah mampir")
    
    elif(jumlah >=5) and (jumlah <=20):
        total_harga2 = (jumlah * kue_coklat * 97/100)
        print("Total harga adalah: "+str(total_harga2))
        print("Selamat anda mendapatkan potongan harga sebesar 7%")
        print("Terima kasih telah mampir")
    
    elif(jumlah >=21) and (jumlah <=35):
        total_harga2 = (jumlah * kue_coklat * 88/100)
        print("Total harga adalah: "+str(total_harga2))
        print("Selamat anda mendapatkan potongan harga sebesar 12%")
        print("Terima kasih telah mampir")

    elif(jumlah == 0):
        total_harga2 = (jumlah * kue_coklat)
        print("Total harga adalah: "+str(total_harga2))
        print("jumlah yang di masukkan tidak boleh 0")
        print("Silahkan kembali ke menu dan masukkan jumlah yang ingin anda beli")

    else:
        print("mohon maaf kami hanya menyediakan stok 25 kue saja")
        print("Terima kasih telah mampir")
