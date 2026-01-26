class LinkedList:
    def __init__(self):
        self.head = None

    # Bintang --
    def TambahData(self):
        nama = input("Masukkan nama barang: ")
        node_baru = Node(nama)

        if self.head is None:
            self.head = node_baru
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node_baru

        print("Barang berhasil ditambahkan")

    # Bintang --
    def RejectBarang(self):
        nama = input("Masukkan nama barang yang dihapus: ")

        if self.head is None:
            print("Linked list kosong")
            return

        if self.head.nama == nama:
            self.head = self.head.next
            print("Barang berhasil dihapus")
            return

        prev = self.head
        curr = self.head.next

        while curr is not None:
            if curr.nama == nama:
                prev.next = curr.next
                print("Barang berhasil dihapus")
                return
            prev = curr
            curr = curr.next

        print("Barang tidak ditemukan")