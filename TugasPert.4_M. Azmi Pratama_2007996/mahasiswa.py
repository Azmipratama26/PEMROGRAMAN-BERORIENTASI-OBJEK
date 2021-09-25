class mahasiswa:
    def __init__(self, nim, nama, alamat):
        self.nim=nim
        self.nama=nama
        self.alamat=alamat

    def printname(self):
        print(self.nim)
        print(self.nama)
        print(self.alamat)

class satu(mahasiswa):
    def __init__(self, nim, nama, alamat):
        mahasiswa.__init__(self, nim, nama, alamat)
        self.jeniskelamin = "Laki-Laki"

    def tampilansatu(self):
        print("NIM           :", self.nim)
        print("Nama          :", self.nama)
        print("Alamat        :", self.alamat)
        print("Jenis Kelamin :", self.jeniskelamin)

class dua(mahasiswa):
    def __init__(self, nim, nama, alamat):
        mahasiswa.__init__(self, nim, nama, alamat)
        self.jeniskelamin = "Laki-Laki"

    def tampilandua(self):
        print("NIM           :", self.nim)
        print("Nama          :", self.nama)
        print("Alamat        :", self.alamat)
        print("Jenis Kelamin :", self.jeniskelamin)

class tiga(mahasiswa):
    def __init__(self, nim, nama, alamat):
        mahasiswa.__init__(self, nim, nama, alamat)
        self.jeniskelamin = "Perempuan"

    def tampilantiga(self):
        print("NIM           :", self.nim)
        print("Nama          :", self.nama)
        print("Alamat        :", self.alamat)
        print("Jenis Kelamin :", self.jeniskelamin)

a = satu(2007996,"Muhammad Azmi Pratama","Pandeglang")
b = dua (2004020,"Hamdi Apriansyah","Serang")
c = tiga(2008869,"Yuki Asuna","Bogor")

print("|====================================|")
print("         BIODATA MAHASISWA          ")
print("|====================================|")
a.tampilansatu()
print("====================================")
b.tampilandua()
print("====================================")
c.tampilantiga()