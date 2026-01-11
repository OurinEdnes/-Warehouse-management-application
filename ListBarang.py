class Barang:
    def __init__(self, id, nama, stock):
        self.idBarang = id
        self.indexBarang = 0
        self.NamaBarang = nama
        self.Stock = stock

class ListBarang:
    def __init__(self, company):
        self.NamaGudang = company
        self.ListBarangGudang = []


    def AddBarangBaru(self, id, nama, stockAwal):
        barang_baru = Barang(id, nama, stockAwal)
        self.ListBarangGudang.append(barang_baru)

    # def PerebuhanBarangBarang(self):

    # def HapusBarang(self):

    def TampilData(self):
        print(f"Daftar data Barang pada Gudang {self.NamaGudang} :\n")
        print(f"{'Rak':<4} {'ID':<8} {'Nama Barang':<20} {'Stock':>5}")
        print("-" * 45)
        for i, b in enumerate(self.ListBarangGudang, start=1):
            print(f"{i:<4} {b.idBarang:<8} {b.NamaBarang:<20} {b.Stock:>5}")

