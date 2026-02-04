import datetime

class Pelanggan:
    def __init__(self, id, nama, waktu, barang):
        self.IdPelangan = id
        self.NamaPelangggan = nama
        self.Barang = barang
        self.waktu_Pemroses = waktu
        self.next = None

class StackBarang:
    def __init__(self, nama):
        self.nama = nama
        self.Top = None
        self.Isi = 0

    def push(self, id, nama, barang):
        waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Pack = Pelanggan(id, nama, waktu, barang)
        if self.is_empty():
            self.Top = Pack
        else:
            Pack.next = self.Top
            self.Top = Pack

        self.Isi += 1
        print(f"[PUSH] Packing pesanan atas nama {nama} ---")

    def pop(self):
        if self.is_empty():
            print(f"{self.nama} kosong!")
            return None
        
        barang = self.Top
        self.Top = self.Top.next
       
        self.Isi -= 1
        print(f"[POP] Barang {barang.NamaPelangggan}")
        return barang.IdPelangan, barang.NamaPelangggan, barang.Barang

    def is_empty(self):
        return self.Top is None

    def tampil(self):
        print(f"\nIsi {self.nama} (atas ke bawah):")

        if self.is_empty():
            print(f"{self.nama} kosong.")
            return
        
        current = self.Top
        i = 1
        while current:
            print(
                f"{i}. "
                f"Nama: {current.NamaPelangggan} | "
                f"ID: {current.IdPelangan} | "
                f"Barang: {current.Barang:<15} | "
                f"Waktu: {current.waktu_Pemroses}"
            )
            current = current.next
            i += 1