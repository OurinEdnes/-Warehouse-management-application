import ListBarang
import StackBarang
import QUEUE
import TreeBarang
import os
# ==============================================

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
        self.RestTree()
        print("\n=== Search Barang ===")
        Id = str(input("Masukan Nama Barang : "))
        index = Search.cari_barang(Id)
        Tesseract.TampilkanDataSearchIndx(index)
        
    def AddPesananCustumer(self): # Raja---
        print("Add Pesanan Customer")


    def CekPackingBarang(self):  # Michdan — STACK
        print("=== PROSES PACKING BARANG (STACK / TROLI) ===")

        # STEP 1: Push barang ke troli (contoh 3 barang pertama)
        for i in range(min(3, len(Tesseract.ListBarangGudang))):
            barang = Tesseract.ListBarangGudang[i]
            Troli.push(barang)

        Troli.tampil()
        Truk.tampil()

        pilih = input("\nLanjutkan memindahkan barang ke truk? (y/n): ")
        if pilih.lower() != 'y':
            print("Proses pemindahan dibatalkan.")
            return

        # STEP 2: Pop barang ke truk (LIFO)
        print("\nSusun barang ke truk:")
        while not Troli.is_empty():
             Troli.pop()
            # Truk.push(barang)

    def RestTree(self):
        for i in range(len(Tesseract.ListBarangGudang)):
            Index = Tesseract.GetIndex(i)
            Nama = Tesseract.GetNama(i)
            if Index == None : continue
            Search.tambah_barang(Index, Nama)

    def run(self, i):
        if 0 <= i < len(self.menu_func):
            self.menu_func[i]()
            return
        else:
            print("Menu Tidak Tersedia!")
            return

Tesseract = ListBarang.ListBarang("Werehouse.comp")
Troli = StackBarang.StackBarang()
Truk = StackBarang.StackBarang()
Troli.set_nama("Troli")
Truk.set_nama("Truk")
Search = TreeBarang.TreeBarang()


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