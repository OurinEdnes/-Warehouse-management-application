from collections import deque
import datetime

class AntrianPengiriman:
    def __init__(self):
    
        self.queue = deque()

    def enqueue(self, id_pesanan, nama_pelanggan, id_barang, jumlah):

        waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pesanan = {
            "id_pesanan": id_pesanan,
            "nama_pelanggan": nama_pelanggan,
            "id_barang": id_barang,
            "jumlah": jumlah,
            "waktu_permintaan": waktu
        }
        self.queue.append(pesanan)
        print(f"📌 [ENQUEUE] Pesanan {id_pesanan} milik {nama_pelanggan} masuk antrean.")

    def dequeue(self):

        if not self.is_empty():
            pesanan_diproses = self.queue.popleft()
            print(f"🚚 [DEQUEUE] Memproses pengiriman {pesanan_diproses['id_pesanan']}...")
            return pesanan_diproses
        else:
            print("⚠️ Antrean kosong, tidak ada barang yang dikirim.")
            return None

    def tampilkan_antrean(self):

        print("\n=== DAFTAR ANTREAN GUDANG SAAT INI ===")
        if self.is_empty():
            print("Kosong")
        for i, p in enumerate(self.queue, 1):
            print(f"{i}. {p['id_pesanan']} - {p['nama_pelanggan']} ({p['waktu_permintaan']})")
        print("======================================\n")

    def is_empty(self):
        return len(self.queue) == 0



gudang = AntrianPengiriman()

gudang.enqueue("ORD001", "Toko Fikri", "BRG01", 10)
gudang.enqueue("ORD002", "Divisi Retail", "BRG05", 25)
gudang.enqueue("ORD003", "Agen Sleman", "BRG02", 5)

gudang.tampilkan_antrean()

gudang.dequeue()

gudang.tampilkan_antrean()