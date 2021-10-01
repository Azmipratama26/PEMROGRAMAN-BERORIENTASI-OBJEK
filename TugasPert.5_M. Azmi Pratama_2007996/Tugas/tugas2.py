class hewan:
    def intro(self):
        print("Di dunia ini ada beberapa hewan berkaki empat dan berkaki dua")

    def kaki(self):
        print("Hampir semua hewan berkaki empat, namun ada beberapa yang berkaki dua")

class kucing(hewan):
    def kaki(self):
        print("Kucing berkaki empat")

class ayam(hewan):
    def kaki(self):
        print("Ayam Berkaki dua")
    
obj_hewan = hewan()
obj_kucing = kucing()
obj_ayam = ayam()

obj_hewan.intro()
obj_hewan.kaki()
print("\n-----------------------------")
obj_kucing.intro()
obj_kucing.kaki()
print("\n-----------------------------")
obj_ayam.intro()
obj_ayam.kaki()
print("\n-----------------------------")