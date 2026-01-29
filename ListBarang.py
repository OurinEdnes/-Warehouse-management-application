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


    def AddBarangBaru(self, id, nama, stockAwal):
        if self.index >= len(self.ListBarangGudang):
            print("Gudang penuh! Tidak bisa menambah barang baru.")
            return
    
        barang_baru = Barang(id, nama, stockAwal)
        self.ListBarangGudang[self.index] = barang_baru
        self.index += 1

        # self.ListBarangGudang.append(barang_baru)

    # def PerebahanBarangBarang(self):

    # def HapusBarang(self):

    def TampilData(self):
        print(f"Daftar data Barang pada Gudang {self.NamaGudang} :\n")
        print(f"{'Rak':<4} {'ID':<5} {'Nama Barang':<20} {'Stock':>5}")
        print("-" * 45)

        for i in range(self.index):
            b = self.ListBarangGudang[i]
            print(f"{i+1:<4} {b.idBarang:<5} {b.NamaBarang:<20} {b.Stock:>5}")

    def TampilkanDataSearchIndx(self, idx):
        b = self.ListBarangGudang[idx]
        print("Barang Ditemukan : ")
        print(f"Barang : {b.idBarang:<3} | {b.NamaBarang:<20} | {b.Stock:>5}")

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