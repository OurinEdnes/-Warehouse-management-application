# =========================
# TREE BARANG (BST MANUAL)
# MODULE: INDEXING GUDANG
# =========================

class BarangNode:
    def __init__(self, kode, nama, rak):
        self.kode = kode          # ID Barang
        self.nama = nama          # Nama Barang
        self.rak = rak            # Lokasi Rak
        self.kiri = None          # Child kiri
        self.kanan = None         # Child kanan


class TreeBarang:
    def __init__(self):
        self.akar = None

    # =========================
    # INSERT BARANG
    # =========================
    def tambah_barang(self, kode, nama, rak):
        if self.akar is None:
            self.akar = BarangNode(kode, nama, rak)
        else:
            self._tambah(self.akar, kode, nama, rak)

    def _tambah(self, node, kode, nama, rak):
        if kode < node.kode:
            if node.kiri is None:
                node.kiri = BarangNode(kode, nama, rak)
            else:
                self._tambah(node.kiri, kode, nama, rak)
        elif kode > node.kode:
            if node.kanan is None:
                node.kanan = BarangNode(kode, nama, rak)
            else:
                self._tambah(node.kanan, kode, nama, rak)
        else:
            print("Kode barang sudah ada!")

    # =========================
    # SEARCH BARANG
    # =========================
    def cari_barang(self, kode):
        return self._cari(self.akar, kode)

    def _cari(self, node, kode):
        if node is None:
            return None
        if node.kode == kode:
            return node
        elif kode < node.kode:
            return self._cari(node.kiri, kode)
        else:
            return self._cari(node.kanan, kode)


# =========================
# SIMULASI PROGRAM GUDANG
# =========================

tree = TreeBarang()

# Data contoh barang di gudang
tree.tambah_barang(10, "Keyboard", "Rak A1")
tree.tambah_barang(5, "Mouse", "Rak A2")
tree.tambah_barang(15, "Monitor", "Rak B1")
tree.tambah_barang(3, "Flashdisk", "Rak C3")
tree.tambah_barang(8, "Headset", "Rak A3")

print("=== SISTEM PENCARIAN BARANG GUDANG ===")
kode_input = int(input("Masukkan kode barang: "))

hasil = tree.cari_barang(kode_input)

if hasil is not None:
    print("Barang ditemukan!")
    print("ID Barang  :", hasil.kode)
    print("Nama Barang:", hasil.nama)
    print("Lokasi Rak :", hasil.rak)
else:
    print("Barang tidak ditemukan di gudang.")
