import ListBarang

class Menu:
    def __init__(self):
        self.menu_func = [
            self.TambahData,
            self.RejectBarang,
            self.SearchBarang,
            self.AddPesananCustumer
        ]

    def TambahData(self):
        print("Tambah Data")

    def RejectBarang(self):
        print("Reject Barang")

    def SearchBarang(self):
        print("Search Barang")

    def AddPesananCustumer(self):
        print("Add Pesanan Customer")


if __name__ == "__main__":
    Tesseract = ListBarang.ListBarang("X.Comp")
    menu = Menu();
    while(True):
        print(f"========== Management Gudang ==========")
        print("Menu Gudang: ")
        print("1. Add Barang Baru. ")
        print("2. Reject Barang. ")
        print("3. Cari barang. ")
        print("4. Add Pesanan Barang. ")
        print("0. Keluar. ")
        choice = int(input("Pilih Menu: "))
        if(choice == 0):
            break
        menu.run(choice)
        
    Tesseract.AddBarangBaru(101, "Aqua Botol 250ml", 20)

    Tesseract.TampilData()
