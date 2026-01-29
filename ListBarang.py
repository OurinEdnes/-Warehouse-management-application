
class Barang:
    def __init__(self, id, nama, stock):
        self.idBarang = id
        self.indexBarang = 0
        self.NamaBarang = nama
        self.Stock = stock

class ListBarang:
    def __init__(self, company,Maxi = 10):
        self.NamaGudang = company
        self.ListBarangGudang = [None] * Maxi
        self.index = 0


    def AddBarangBaru(self, id, nama, stockAwal, idx):
        if idx is not None:
            self.AddStock(idx, stockAwal)
            return
        
        if self.index >= len(self.ListBarangGudang):
            print("Gudang penuh! Tidak bisa menambah barang baru.")
            return False
    
        barang_baru = Barang(id, nama, stockAwal)
        for i in range(self.index):
            if self.ListBarangGudang[i] is None:
                barang_baru.indexBarang = i
                self.ListBarangGudang[i] = barang_baru
                return True
        
        barang_baru.indexBarang = self.index
        self.ListBarangGudang[self.index] = barang_baru
        self.index += 1
        return True
        # self.ListBarangGudang.append(barang_baru)
    def AddStock(self, idx, value):
        self.ListBarangGudang[idx].Stock += value
        return

    def PerebahanBarangBarang(self, keyValue, id):
        if self.ListBarangGudang[id].Stock == 0:
            print("Barang Sudah Habis Harap pesan barang lain! --")
            return None

        if self.ListBarangGudang[id].Stock - keyValue < 0:
            print("Pesanan melebihi jumlah stock tersedia! ")
            print("Pesanan akan secara otomatis menjadi banyaknya sisa stock yang tersedia! ")
            temp = self.ListBarangGudang[id].Stock
            self.ListBarangGudang[id].Stock = 0
            return temp

        self.ListBarangGudang[id].Stock -= keyValue
        return keyValue
    
    def HapusBarang(self, idx):
        self.ListBarangGudang[idx] = None
        return

    def TampilData(self):
        print(f"Daftar data Barang pada Gudang {self.NamaGudang} :\n")
        print(f"{'Rak':<4} {'ID':<5} {'Nama Barang':<20} {'Stock':>5}")
        print("-" * 45)

        for i in range(self.index):
            b = self.ListBarangGudang[i]
            if b is None : continue
            print(f"{i+1:<4} {b.idBarang:<5} {b.NamaBarang:<20} {b.Stock:>5}")

    def TampilkanDataSearchIndx(self, idx):
        b = self.ListBarangGudang[idx]
        print("Barang Ditemukan : ")
        print(f"Barang : {b.idBarang:<3} | {b.NamaBarang:<10} | {b.Stock:>5}")

    def GetIndex(self, i):
        b = self.ListBarangGudang[i]
        if b is None:
            return None
        return b.indexBarang

    def GetNama(self, i):
        b = self.ListBarangGudang[i]
        if b is None:
            return None
        return b.NamaBarang
    
    def getAll(self, idx):
        barang = self.ListBarangGudang[idx]
        return barang.idBarang, barang.NamaBarang, barang.Stock