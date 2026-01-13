import ListBarang
import os

class Menu:
    def __init__(self):
        self.menu_func = [
            self.TambahData,
            self.rejectBarang,
            self.CekBarang,
            self.SearchBarang,
            self.AddPesananCustumer,
            self.CekPackingBarang
        ]

    def TambahData(self): # Bintang --
        print("Tambah Data")
        Tesseract.AddBarangBaru(101, "Aqua Botol 250ml", 20)

    def rejectBarang(self): 
        print("rejectBarang")

    def CekBarang(self): 
        print("Cek Barang")
        Tesseract.TampilData()

    def SearchBarang(self): # Albani----
        print("Search Barang")

    def AddPesananCustumer(self): # Raja---
        print("Add Pesanan Customer")

    def CekPackingBarang(self): # Michdan---
        print("Add Pesanan Customer")

    def run(self, i):
        if 0 <= i < len(self.menu_func):
            self.menu_func[i]()
            return
        else:
            print("Menu Tidak Tersedia!")
            return

Tesseract = ListBarang.ListBarang("Werehouse.comp")

if __name__ == "__main__":
    menu = Menu();
    choice = 0
    while(True):
        os.system('cls')
        print(f"========== Management Gudang ==========")
        print("Menu Gudang: ")
        print("1. Add Barang Baru. ")
        print("2. Reject Barang. ")
        print("3. Cek Barang. ")
        print("4. Cari barang. ")
        print("5. Add Pesanan Barang. ")
        print("6. Cek Packing Barang. ")
        print("0. Keluar. ")
        choice = int(input("Pilih Menu: "))
        if(choice <= 0):
            print("---- Keluar APP.....")
            break
        menu.run(choice-1)
        os.system('pause')
