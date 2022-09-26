class Mobil:
    _merk = ""
    _tipe = ""
    _kapasitasBBM = None
    _jenisBahanBakar = None

    def __init__(self, merk, tipe):
        self._merk = merk
        self._tipe = tipe

    def setKapasitasBBM(self, kapasitasBBM):
        self._kapasitasBBM = kapasitasBBM

    def setJenisBahanBakar(self, jenisBahanBakar):
        self._jenisBahanBakar = jenisBahanBakar

    def getKapasitasBBM(self):
        return self._kapasitasBBM

    def getJenisBahanBakar(self):
        return self._jenisBahanBakar

    def getMerk(self):
        return self._merk

    def getTipe(self):
        return self._tipe
        
    def printInfo(self):
        print("="*10 + " INFO " + "="*10)
        print("Merk\t\t:", self.getMerk())
        print("Tipe\t\t:", self.getTipe())
        print("Bahan Bakar\t:",self.getJenisBahanBakar())
        print("Kapasitas BBM\t:", self.getKapasitasBBM())
    
    def isiBBM(self, harga):
        if self.getJenisBahanBakar() is None or self.getKapasitasBBM() is None :
            print("ERROR! Kapasitas BBM atau Jenis Bahan Bakar belum di inputkan")
        else:
            print("Mengisi "+str(self.getKapasitasBBM())+" liter")
            print("Total Harga : Rp"+str(harga * self.getKapasitasBBM()))

if __name__ == "__main__":
    mobil1 = Mobil("Toyota", "Avanza")
    mobil1.printInfo()
    mobil2 = Mobil("Nissan", "Grand Livina")
    mobil2.setJenisBahanBakar("Bensin")
    mobil2.setKapasitasBBM(20)
    mobil2.printInfo()
    mobil1.isiBBM(14500)
    mobil2.isiBBM(14500)