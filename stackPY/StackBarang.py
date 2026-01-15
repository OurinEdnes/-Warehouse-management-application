class StackBarang:
    def __init__(self):
        self.stack = []

    def push(self, barang):
        self.stack.append(barang)
        print(f"[PUSH] Barang {barang.NamaBarang} masuk ke troli")

    def pop(self):
        if self.is_empty():
            print("Troli kosong!")
            return None
        barang = self.stack.pop()
        print(f"[POP] Barang {barang.NamaBarang} dipindahkan ke truk")
        return barang

    def is_empty(self):
        return len(self.stack) == 0

    def tampil_troli(self):
        print("\nIsi Troli (atas ke bawah):")
        for b in reversed(self.stack):
            print(f"- {b.NamaBarang}")
