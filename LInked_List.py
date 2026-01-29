class Node:
    def __init__(self, nama, id, stock, stat):
        self.nama = nama
        self.id = id
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
        while temp is not None:
            print(f"{temp.id} | {temp.nama} | {temp.stock} | {temp.stat} ->", end=" ")
            temp = temp.next

        print("None")