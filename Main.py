import ListBarang
import LInked_List
import StackBarang
import QUEUE
import TreeBarang
import os
# ==============================================

Tesseract = ListBarang.ListBarang("Werehouse.comp")
Troli = StackBarang.StackBarang("Troli")
Truk = StackBarang.StackBarang("Truk")
Search = TreeBarang.TreeBarang()
History = LInked_List.LinkedList()
Pelanggan = QUEUE.AntrianPengiriman()

# --------------------------------------------

class Menu:
    def __init__(self):
        self.menu_func = [
            self.TambahData,
            self.HistoryBarang,
            self.CekBarang,
            self.SearchBarang,
            self.PesananCustumer,
            self.CekPackingBarang
        ]

    def TambahData(self): # Bintang --
        print("\n=== Tambah Data ===")
        Id = int(input("Masukan Id Barang: "))
        NamaBarang = str(input("Masukan Nama Barang: "))
        Stock = int(input("Masukan Stock Barang: "))
        # Bridging ------------
        idx = Search.compare(NamaBarang)
        Pass = Tesseract.AddBarangBaru(Id, NamaBarang, Stock, idx)
        if Pass == 1: History.TambahData(Id, NamaBarang, Stock, "Penambahan Barang")
        elif Pass == 2: History.TambahData(Id, NamaBarang, Stock, "Restock Barang")
        self.RestTree()

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
            Search.Cetak()
            return

        Tesseract.TampilkanDataSearchIndx(index)
        
    def PesananCustumer(self): # Raja---
        print("1. Tambah Pesanan. ")
        print("2. Cek Pesanan Customer. ")
        print("3. Pesanan Front Selesai. ")
        inp = int(input("Masukan Pilhan: "))
        if inp == 1:
            print("\n=== Add Pesanan Customer ===")
            idp = int(input("Masukan ID Pelanggan: "))
            nama = str(input("Masukan Nama Pelanggan: "))
            nmb = str(input("Masukan Nama Barang: "))
            jml = int(input("Masukan Jumlah Barang: "))
            idxb = Search.cari_barang(nmb)
            if idxb is None: 
                print("Barang tidak ditemukan! --")
                return
            
            jml = Tesseract.PerebahanBarangBarang(jml, idxb)
            if jml is None :
                return
            Pelanggan.enqueue(idp,nama,nmb,jml)
            Troli.push(idp, nama, nmb)
            History.TambahData(idp, nmb, jml, "Pesanan Barang")

            return
        elif inp == 2:
            Pelanggan.tampilkan_antrean()
            return
        elif inp == 3:
            print("\n=== Front Pesanan ===")
            if Truk.Top is None :
                print("Barang Belum dimasukan kedalam Truk! ---")
                return

            Pelanggan.dequeue()
            Truk.pop()
            return

    def CekPackingBarang(self):  # Michdan — STACK
        print("=== PROSES PACKING BARANG (STACK / TROLI) ===")
        Troli.tampil()
        Truk.tampil()

        print("\nTruk Hanya Dapat disi jika kapasitas Packing mencapai 10!")
        pilih = input("Lanjutkan memindahkan barang ke truk? (y/n): ")
        if pilih.lower() != 'y':
            print("Proses pemindahan dibatalkan.")
            return
        elif Truk.Top is not None :
            print("Harap Kirim terlebih dahulu pesanan yang ada di truck! --")
            return
        elif Troli.Isi < 5 :
            print("Tidak bisa dimuat kedalam truk, harap memiliki setidaknya 5 packing")
            return
        
        else:
            print("\n---- Susun barang ke truk:")
            while not Troli.is_empty():
                if Truk.Isi > 10 : break
                id, nama, barang = Troli.pop()
                Truk.push(id, nama, barang)

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

if __name__ == "__main__":
   # ================= DUMMY DATA =================
    # Barang awal di gudang
    idx1 = Search.compare("Laptop")
    Tesseract.AddBarangBaru(101, "Laptop", 15, idx1)
    History.TambahData(101, "Laptop", 15, "Initial Stock")

    idx2 = Search.compare("Mouse")
    Tesseract.AddBarangBaru(102, "Mouse", 40, idx2)
    History.TambahData(102, "Mouse", 40, "Initial Stock")

    idx3 = Search.compare("Keyboard")
    Tesseract.AddBarangBaru(103, "Keyboard", 25, idx3)
    History.TambahData(103, "Keyboard", 25, "Initial Stock")

    idx4 = Search.compare("Monitor")
    Tesseract.AddBarangBaru(104, "Monitor", 10, idx4)
    History.TambahData(104, "Monitor", 10, "Initial Stock")

    idx5 = Search.compare("Flashdisk")
    Tesseract.AddBarangBaru(105, "Flashdisk", 50, idx5)
    History.TambahData(105, "Flashdisk", 50, "Initial Stock")
    

    # ========== DUMMY QUEUE (PESANAN CUSTOMER) ==========
    Pelanggan.enqueue(201, "Budi", "Laptop", 1)
    Pelanggan.enqueue(202, "Siti", "Mouse", 2)
    Pelanggan.enqueue(203, "Andi", "Keyboard", 1)
    Pelanggan.enqueue(204, "Rina", "Flashdisk", 5)
    Pelanggan.enqueue(205, "Dewi", "Monitor", 1)

    History.TambahData(201, "Laptop", 1, "Pesanan Barang")
    History.TambahData(202, "Mouse", 2, "Pesanan Barang")
    History.TambahData(203, "Keyboard", 1, "Pesanan Barang")
    History.TambahData(204, "Flashdisk", 5, "Pesanan Barang")
    History.TambahData(205, "Monitor", 1, "Pesanan Barang")

    # ========== DUMMY STACK (TROLI / PACKING) ==========
    Troli.push(201, "Budi", "Laptop")
    Troli.push(202, "Siti", "Mouse")
    Troli.push(203, "Andi", "Keyboard")
    Troli.push(204, "Rina", "Flashdisk")
    Troli.push(205, "Dewi", "Monitor")

    # --------------------------------------------
    menu = Menu();
    choice = 0
    while(True):
        os.system('cls')
        print(f"========== Management Gudang ==========")
        print("Menu Gudang: ")
        print("1. Add Barang. ")
        print("2. History Barang. (Linked-List)")
        print("3. Cek Barang. (List)")
        print("4. Cari barang. (Tree)")
        print("5. Pesanan Barang. ")
        print("6. Cek Packing Barang. (Stack) ")
        print("0. Keluar. ")
        choice = int(input("Pilih Menu: "))
        if(choice <= 0):
            print("---- Keluar APP.....")
            break
        menu.run(choice-1)
        os.system('pause')