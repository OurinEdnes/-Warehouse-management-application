class ListBarang:
    def __init__(self, company):
        self.NamaGudang = company
        self.ListBarangGudang = []


    def AddBarangBaru(self, id, nama, stockAwal):
        Data_Barang = {
            "idBarang" : id,
            "NamaBarang" : nama,
            "Stock" : stockAwal
        }
        self.ListBarangGudang.append(Data_Barang)

    # def PerebuhanBarangBarang(self):

    # def HapusBarang(self):

    def TampilData(self):
        print(f"Dafta data Barang pada Gudang {self.NamaGudang}")
        for i, b in enumerate(self.ListBarangGudang, start=1):
            print(f"{1}.{b['idBarang']} - {b['NamaBarang']} - {b['Stock']}")
