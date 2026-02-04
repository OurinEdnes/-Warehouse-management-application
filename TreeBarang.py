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
        if nama.lower() == node.nama.lower():
            return
        if nama.lower() < node.nama.lower():
            if node.kiri is None:
                node.kiri = BarangNode(kode, nama)
            else:
                self._tambah(node.kiri, kode, nama)
        else:
            if node.kanan is None:
                node.kanan = BarangNode(kode, nama)
            else:
                self._tambah(node.kanan, kode, nama)

    # =========================
    # SEARCH BARANG
    # =========================
    def cari_barang(self, nama): #section untuk ngasih tahu untuk apa.
        hasil = self._cari(self.akar, nama) # ada dua pilihan antara none atau index data yang dicari
        
        if hasil is not None:
           return hasil
        else:
            return None
    
    def _cari(self, node, nama):
        if node is None:
            return None
        if node.nama == nama:
            return node.kode
        elif nama < node.nama:
            return self._cari(node.kiri, nama)
        else:
            return self._cari(node.kanan, nama)
        
    # =========================
    # DELETE BARANG
    # =========================
    def hapus_barang(self, nama):
        self.akar = self._hapus(self.akar, nama)

    def _hapus(self, node, nama):
        if node is None:
            return None

        # Cari node yang mau dihapus
        if nama.lower() < node.nama.lower():
            node.kiri = self._hapus(node.kiri, nama)

        elif nama.lower() > node.nama.lower():
            node.kanan = self._hapus(node.kanan, nama)

        else:
            # ===== NODE DITEMUKAN =====
            # Case 1: Tidak punya anak
            if node.kiri is None and node.kanan is None:
                return None

            # Case 2: Punya satu anak
            if node.kiri is None:
                return node.kanan
            elif node.kanan is None:
                return node.kiri

            # Case 3: Punya dua anak
            successor = self._min_value(node.kanan)
            node.nama = successor.nama
            node.kode = successor.kode
            node.kanan = self._hapus(node.kanan, successor.nama)

        return node

    def _min_value(self, node):
        current = node
        while current.kiri is not None:
            current = current.kiri
        return current
    

    # Debugging----
    def Cetak(self):
        print("=== CETAK TREE (In-Order) ===")
        self._cetak(self.akar, "ROOT")

    def _cetak(self, node, posisi):
        if node is None:
            return
        
        # KIRI
        self._cetak(node.kiri, "KIRI")
        
        # NODE SEKARANG
        print(f"[{posisi}] Kode: {node.kode}, Nama: {node.nama}")
        
        # KANAN
        self._cetak(node.kanan, "KANAN")

# # Bridging --------------------
#     def compare(self, kode):
#         hasil = self.compare_(self.akar, kode)
#         if hasil is not None:
#             return hasil
#         else:
#             return None
    
#     def compare_(self, node, kode):
#         if node is None:
#             return None
#         if node.nama == kode:
#             return node.kode
#         elif kode < node.nama:
#             return self.compare_(node.kiri, kode)
#         else:
#             return self.compare_(node.kanan, kode)  
                
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
