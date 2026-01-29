# =========================
# TREE BARANG (BST MANUAL)
# MODULE: INDEXING GUDANG
# =========================

class BarangNode:
    def __init__(self, kode, nama):
        self.kode = kode          # ID Barang
        self.nama = nama          # Nama Barang
        #-------------------------------------
        self.kiri = None          # Child kiri
        self.kanan = None         # Child kanan


class TreeBarang:
    def __init__(self):
        self.akar = None

    # =========================
    # INSERT BARANG
    # =========================
    def tambah_barang(self, kode, nama):
        if self.akar is None:
            self.akar = BarangNode(kode, nama)
        else:
            self._tambah(self.akar, kode, nama)

    def _tambah(self, node, kode, nama):
        if kode < node.kode:
            if node.kiri is None:
                node.kiri = BarangNode(kode, nama)
            else:
                self._tambah(node.kiri, kode, nama)
        elif kode > node.kode:
            if node.kanan is None:
                node.kanan = BarangNode(kode, nama)
            else:
                self._tambah(node.kanan, kode, nama)

    # =========================
    # SEARCH BARANG
    # =========================
    def cari_barang(self, kode):
        hasil = self._cari(self.akar, kode)
        if hasil is not None:
            return hasil
        else:
            print("Barang Tidak Ada!")
            return None
    
    def _cari(self, node, kode):
        if node is None:
            return None
        if node.nama == kode:
            return node.kode
        elif kode < node.nama:
            return self._cari(node.kiri, kode)
        else:
            return self._cari(node.kanan, kode)

    def Cetak(self):
        self._cetak(self.akar)

    def _cetak(self, node):
        if node is None:
            return

        self._cetak(node.kiri)
        print(node.kode, node.nama)
        self._cetak(node.kanan)


# Bridging --------------------
    def compare(self, kode):
        hasil = self.compare_(self.akar, kode)
        if hasil is not None:
            return hasil
        else:
            return None
    
    def compare_(self, node, kode):
        if node is None:
            return None
        if node.nama == kode:
            return node.kode
        elif kode < node.nama:
            return self.compare_(node.kiri, kode)
        else:
            return self.compare_(node.kanan, kode)  
                
# # =========================
# # SIMULASI PROGRAM GUDANG
# # =========================

# tree = TreeBarang()

# # Data contoh barang di gudang
# tree.tambah_barang(10, "Keyboard")
# tree.tambah_barang(5, "Mouse")
# tree.tambah_barang(15, "Monitor",)
# tree.tambah_barang(3, "Flashdisk")
# tree.tambah_barang(8, "Headset")

# print("=== SISTEM PENCARIAN BARANG GUDANG ===")
# kode_input = int(input("Masukkan kode barang: "))

# hasil = tree.cari_barang(kode_input)

# if hasil is not None:
#     print("Barang ditemukan!")
#     print("ID Barang  :", hasil.kode)
#     print("Nama Barang:", hasil.nama)
#     print("Lokasi Rak :", hasil.rak)
# else:
#     print("Barang tidak ditemukan di gudang.")
