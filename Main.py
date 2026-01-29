import ListBarang
import LInked_List
import StackBarang
import QUEUE
import TreeBarang
import os
# ==============================================

Tesseract = ListBarang.ListBarang("Werehouse.comp")
Troli = StackBarang.StackBarang()
Truk = StackBarang.StackBarang()
Troli.set_nama("Troli")
Truk.set_nama("Truk")
Search = TreeBarang.TreeBarang()
History = LInked_List.LinkedList()

# --------------------------------------------

class Menu:
    def __init__(self):
        self.menu_func = [
            self.TambahData,
            self.rejectBarang,
            self.HistoryBarang,
            self.CekBarang,
            self.SearchBarang,
            self.AddPesananCustumer,
            self.CekCustumer,
            self.CekPackingBarang
        ]

    def TambahData(self): # Bintang --
        print("\n=== Tambah Data ===")
        Id = int(input("Masukan Id Barang: "))
        NamaBarang = str(input("Masukan Nama Barang: "))
        Stock = int(input("Masukan Stock Barang: "))
        Pass = Tesseract.AddBarangBaru(Id, NamaBarang, Stock)
        if Pass : History.TambahData(Id, NamaBarang, Stock, "Penambahan Barang")
        self.RestTree()

    def rejectBarang(self): 
        print("\n=== Reject Barang ===")
        id = str(input("Masukan Nama barang: "))
        idx = Search.cari_barang(id)

        if idx:
            Search.RestTree(id)
            idq, nama, stock = Tesseract.getAll(idx)
            Tesseract.HapusBarang(idx)
            History.TambahData(idq, nama, stock, "Penghapusan Barang")
            print("Barang Sudah DiReject! --")
            return
        
        print("Barangg Gagal DiReject! --")

    def HistoryBarang(self):
        print("\n=== HISTORY BARANG ===")
        History.Traverse()

    def CekBarang(self): 
        print("\n=== Cek Barang ===")
        Tesseract.TampilData()

    def SearchBarang(self): # Albani----
        self.RestTree()
        print("\n=== Search Barang ===")
        Id = str(input("Masukan Nama Barang : "))
        index = Search.cari_barang(Id)
        if index is None:
            print("Data Tidak Ditemukan! --")
            return

        Tesseract.TampilkanDataSearchIndx(index)
        
    def AddPesananCustumer(self): # Raja---
        print("\n=== Add Pesanan Customer ===")

    def CekCustumer(self):
        return

    def CekPackingBarang(self):  # Michdan — STACK
        print("=== PROSES PACKING BARANG (STACK / TROLI) ===")

        # STEP 1: Push barang ke troli (contoh 3 barang pertama)
        for i in range(len(Tesseract.ListBarangGudang)):
            barang = Tesseract.ListBarangGudang[i]
            Troli.push(barang)

        Troli.tampil()
        Truk.tampil()

        pilih = input("\nLanjutkan memindahkan barang ke truk? (y/n): ")
        if pilih.lower() != 'y':
            print("Proses pemindahan dibatalkan.")
            return

        # STEP 2: Pop barang ke truk (LIFO)
        print("\n---- Susun barang ke truk:")
        while not Troli.is_empty():
             Troli.pop()
            # Truk.push(barang)

    def RestTree(self):
        for i in range(len(Tesseract.ListBarangGudang)):
            Index = Tesseract.GetIndex(i)
            Nama = Tesseract.GetNama(i)
            if Index == None : continue
            Search.tambah_barang(Index, Nama)
            Search.Cetak()

    def run(self, i):
        if 0 <= i < len(self.menu_func):
            self.menu_func[i]()
            return
        else:
            print("Menu Tidak Tersedia!")
            return

if __name__ == "__main__":
    menu = Menu();
    choice = 0
    while(True):
        os.system('cls')
        print(f"========== Management Gudang ==========")
        print("Menu Gudang: ")
        print("1. Add Barang Baru. ")
        print("2. Reject Barang. ")
        print("3. History Barang. (Linked-List)")
        print("4. Cek Barang. (List)")
        print("5. Cari barang. ")
        print("6. Add Pesanan Barang. ")
        print("7. Cek Pemesan. (Queue) ")
        print("8. Cek Packing Barang. (Stack) ")
        print("0. Keluar. ")
        choice = int(input("Pilih Menu: "))
        if(choice <= 0):
            print("---- Keluar APP.....")
            break
        menu.run(choice-1)
        os.system('pause')