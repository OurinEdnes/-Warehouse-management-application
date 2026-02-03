class Node:
    def __init__(self, id, nama, stock, stat):
        self.id = id
        self.nama = nama
        self.stock = stock
        self.stat = stat
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def isNull(self):
        return self.head is None

    # Bintang --
    def TambahData(self, nama, id, stock, stat):
        node_baru = Node(nama, id, stock, stat)

        if self.head is None:
            self.head = node_baru
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node_baru

    def Traverse(self):
        if self.isNull():
            print("History Kosong! ---")
            return
        temp = self.head
        no = 1
        while temp is not None:
            print(f"{no}. {temp.id:<15} | {temp.nama:<10} | {temp.stock:>5} | {temp.stat}")
            temp = temp.next
            no += 1

        print("None")

    def HapusDataByNama(self, nama, statusMaksud):
        if self.isNull():
            print("History Kosong! Tidak ada yang dihapus.")
            return

        # Jika data yang dihapus ada di head
        if self.head.nama == nama:
            self.head = self.head.next
            print(f"History dengan nama {nama} berhasil dihapus.")
            return

        # Cari node yang akan dihapus
        prev = self.head
        curr = self.head.next
        statusMaksud = self.head.stat

        while curr is not None:
            if curr.nama == nama:
                prev.next = curr.next
            print(f"History dengan nama {nama} dengan status {statusMaksud} berhasil dihapus.")
            return
        prev = curr
        curr = curr.next

        print(f"History dengan nama {nama} dengan status {statusMaksud} tidak ditemukan.")
