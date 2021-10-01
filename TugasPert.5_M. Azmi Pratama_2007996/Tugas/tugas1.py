class naruto:
    def __init__(self, nama, umur,alamat,hobi):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
        self.hobi = hobi

    def bersuara(self):
        print("Assalamualaikum, Perkenalkan Nama Saya",self.nama,"Umur Saya",self.umur,"Tahun,",
              "Saya Berasal dari",self.alamat,"Hobi saya",self.hobi)

class sasuke:
    def __init__(self, nama, umur,alamat,hobi):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
        self.hobi = hobi
        
    def bersuara(self):
        print("Hallo, Nama Saya",self.nama,"Umur Saya",self.umur,"Tahun,",
              "Saya Berasal dari",self.alamat,"Hobi saya",self.hobi)

class radit:
    def __init__(self, nama, umur,alamat,hobi):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
        self.hobi = hobi
        
    def bersuara(self):
        print("Nama Saya",self.nama,"Umur Saya",self.umur,"Tahun,",
              "Saya Berasal dari",self.alamat,"Hobi saya",self.hobi)

naruto1 = naruto("Naruto,", 19,"Pandeglang,","Berceramah. \n-------------------------------------------------------")
sasuke2 = sasuke("Sasuke,", 20,"Konoha,", "Bertarung. \n-------------------------------------------------------")
radit3 = radit("Radit,", 30,"Jakarta,", "Membaca Buku. \n-------------------------------------------------------")

for individu in (naruto1, sasuke2, radit3):
    individu.bersuara()