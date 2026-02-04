import datetime

class NodePesanan:
    def __init__(self, id_pesanan, nama_pelanggan, NamaBarang, jumlah, waktu):
        self.id_pesanan = id_pesanan
        self.nama_pelanggan = nama_pelanggan
        self.NamaBarang = NamaBarang
        self.jumlah = jumlah
        self.waktu_permintaan = waktu
        self.next = None

class AntrianPengiriman:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def is_empty(self):
        return self.front is None

    def enqueue(self, id_pesanan, nama_pelanggan, NamaBarang, jumlah):
        waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        node_baru = NodePesanan(id_pesanan, nama_pelanggan, NamaBarang, jumlah, waktu)

        if self.is_empty():
            self.front = node_baru
            self.rear = node_baru
        else:
            self.rear.next = node_baru
            self.rear = node_baru

        print(f"[ENQUEUE] Pesanan {id_pesanan} milik {nama_pelanggan} masuk antrean.")

    def dequeue(self):
        if self.is_empty():
            print("Antrean kosong, tidak ada barang yang dikirim.")
            return None

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        print(f"[DEQUEUE] Memproses pengiriman {temp.nama_pelanggan}...")
        return temp

    def tampilkan_antrean(self):
        print("\n=== DAFTAR ANTREAN PELANGGAN SAAT INI ===")

        if self.is_empty():
            print("Kosong")
            print("======================================\n")
            return

        temp = self.front
        i = 1
        while temp is not None:
            print(f"{i}. {temp.id_pesanan} - {temp.nama_pelanggan} ({temp.waktu_permintaan})")
            temp = temp.next
            i += 1

        print("======================================\n")

