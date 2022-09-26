import json

with open('mahasiswa.json', 'r') as datafile:
    data = json.load(datafile)

    mahasiswa = int(input("Masukan jumlah mahasiswa baru : "))

    for i in range(0, mahasiswa):
       
        nama = input("Masukan nama Anda : ")
        lis = []
        dct = {}
        jml_hobi = int(input("Masukan Jumlah hobi : "))
        lis_hobi = []
        for j in range(1, jml_hobi+1):
            hobi = input("Masukan Hobi ke-{index} : ".format(index=j))
            lis_hobi.append(hobi)

        prestasi = input("Masukan Prestasi Anda : ")

        lis.append({"BioData":{"Hobi":lis_hobi,"Prestasi":prestasi}})
        data[nama] = lis

        print("=== Data berhasil ditambahkan ===")
        print()

#tambahkan data ke json
with open('mahasiswa.json', 'w') as datafile:
    json.dump(data, datafile)