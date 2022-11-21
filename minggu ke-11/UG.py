class RakObat:
    def __init__(self):
        self.size = 5
        self.map = [None] * self.size

    def _getHash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char) # mendapatkan nilai ASCII
        return hash % self.size

    def _probing(self, key):
        for index in range(self.size):
            # probeHash = (self._getHash(key)+index) % self.size
            probeHash = self._linearProbing(key, index)
            # valid bila index adalah None atau ber-flag deleted
            if (self.map[probeHash] is None) or (self.map[probeHash] == 'deleted'):
                return probeHash

        return None

    # melakukan linear probing
    def _linearProbing(self, key, index):
        return (self._getHash(key)+index) % self.size

    # menambahkan key pada hash table
    def tambahObat(self, key, value):
        # periksa apakah key_hash sudah terpakai
        key_hash = self._getHash(key)
        # buat pasangan key value
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            key_hash = self._probing(key)
            if key_hash is None:
                print("Rak Obat anda sudah penuh")
                return False

        self.map[key_hash] = list([key_value])
        return False

    def lihatObat(self, key):
        key_hash = self._getHash(key)
        if (self.map[key_hash] is not None) and (self.map[key_hash] != 'deleted'):
            for index in range(self.size):
                #mencari dengan melakukan probing
                key_hash = self._linearProbing(key, index)
                # periksa apakah key adalah data yg akan dihapus
                if(self.map[key_hash][0][0] == key):
                    return self.map[key_hash][0][1]

        print("Key ", key, " tidak ditemukan")
        return "None"

    def ambilObat(self, key):
        key_hash = self._getHash(key)
        if self.map[key_hash] is None:
            return False
        for index in range(self.size):
            #menghapus dengan melakukan linear probing
            key_hash = self._linearProbing(key, index)
            # periksa apakah key adalah data yg akan dihapus
            if(self.map[key_hash][0][0] == key):
                print('obat', key, 'diambil dari rak')
                self.map[key_hash] = "deleted"
                return True

        print("Key ", key, " tidak ditemukan")
        return False

    def printAll(self):
        print("="*20,'List Obat',"="*20)
        
        for item in self.map:
            if item != 'deleted':
                print(str("Nama : "+item[0][1])+" <> "+"Jenis : "+item[0][0])

        print("="*51)

if __name__ == "__main__":
    rak1 = RakObat()
    rak1.tambahObat("Covid", "AstraZeneca (A01)")
    rak1.tambahObat("Flu", "UltraFlu (A02)")
    rak1.tambahObat("Sakit Kepala", "Paramex (A03)")
    rak1.tambahObat("Maag", "Pro Maag (A04)")
    rak1.tambahObat("Sakit Kepala", "Bodrex (A05)")
    rak1.tambahObat("Vitamin", "Vitacimin")
    print(rak1.lihatObat("Sakit Kepala"))
    print(rak1.lihatObat("Migraine"))
    rak1.ambilObat("Flu")
    rak1.ambilObat("Malaria")
    rak1.printAll()