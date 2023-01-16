class animal:
    def _init_(self,nama,spesies,ordo,kelas):
        self.nama = nama
        self.spesies = spesies
        self.ordo = ordo
        self.kelas = kelas

    def show (self):
        print("{}\n\t Spesies : {}\n\t Ordo   : {}\n\t Classification    : {}". format(self.nama,self.spesies,self.ordo,self.kelas))

class animal_cat(animal):
      def __init__(self,nama,spesies,ordo,kelas):
        super()._init_(nama,spesies,ordo,kelas)
        super().show()

class animal_swan(animal):
    def __init__(self,nama,spesies,ordo,kelas):
        super()._init_(nama,spesies,ordo,kelas)
        super().show()

kucing = animal_cat('Kucing','Felis Catus','Carnivora', 'Mamamlia')
angsa = animal_swan('Angsa','Cygnini','Anseriformes','Aves')