class NodeTabungan:
    no_rekening = None
    nama = None
    saldo = None
    next = None
 
    def __init__(self, no_rekening, nama, saldo=0):
        self.no_rekening = no_rekening
        self.nama = nama
        self.saldo = saldo
        self.next = None

class SLNC:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def insert_head(self, no_rekening, nama, saldo):
        baru = NodeTabungan(no_rekening, nama, saldo)
        if self.isEmpty()==True:
            self.head = baru
            self.tail = baru
            self.tail.next = None
        else:
            baru.next = self.head
            self.head = baru
        self.size += 1

    # def delete_head(self):
    #     if self.isEmpty() == False:
    #         d = ""
    #         if self.head.next==None:
    #             d = self.head.element
    #             self.head=None
    #             self.tail=None
    #         else:
    #             hapus = self.head
    #             d = hapus.element
    #             self.head = self.head.next
    #             hapus.next=None
    #             del hapus
    #         self.size -= 1
    #         print(d," terhapus!")
    #     else:
    #         print("Kosong!")

    # def delete_tail(self):
    #     if self.isEmpty() == False:
    #         d = None
    #         bantu = self.head
    #         if(self.head != self.tail):
    #             while bantu.next != self.tail:
    #                 bantu = bantu.next
    #             hapus = self.tail
    #             self.tail = bantu
    #             d = hapus.element
    #             del hapus
    #             self.tail.next = None
    #         else:
    #             d = self.tail.element
    #             self.head=tail=None
    #         self.size -= 1
    #         print(d, " terhapus!")
    #     else:
    #         print("Kosong!")

    # def delete(self, position):
    #     if self.size == 0:
    #         return False
    #     elif position == 0:
    #         self.delete_head()
    #     elif position + 1 >= self.size:
    #         self.delete_tail()
    #     else:
    #         delete_node = self.head
    #         for i in range(position):
    #             delete_node = delete_node.next
    #         helper = self.head
    #         while helper.next != delete_node:
    #             helper = helper.next
    #         helper.next = delete_node.next
    #         del delete_node
    #     self.size = self.size - 1

    def filter(self, batas):
        kepala = self.head

        try:
            while kepala is not None:
                if kepala.saldo < batas:
                    del kepala.saldo
                kepala.next
        except:
            print("Rekening yang berhasil dihapus sebanyak : 0 buah")
    

    def print(self):
        if self.isEmpty()==False:
            bantu = self.head
            while(bantu!=None):
                print("Norek: ",bantu.no_rekening," ")
                print("Nama: ",bantu.nama," ")
                print("Saldo: ",bantu.saldo," ")
                print()
                bantu = bantu.next
            print()
        else:
            print("Kosong")

    def update(self, batas):
        kepala = self.head
        if batas > 100 or batas < 0:
            print("Maaf besaran persen harus diantara 0-100")   
        else:
            while kepala is not None:
                if kepala.saldo < batas:
                    del kepala.saldo
                kepala.next

slnc=SLNC()
slnc.insert_head(201,"Hanif", 250000)
slnc.insert_head(110,"Yudha", 150000)
slnc.print()
slnc.filter(100)
slnc.print()
slnc.update(200)
slnc.update(50)
slnc.print()