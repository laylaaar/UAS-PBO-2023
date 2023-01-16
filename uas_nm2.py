class animal:
    def _init_(self,nama,spesies,ordo,kelas):
        self.__nama = nama
        self.__spesies = spesies
        self.__ordo = ordo
        self.__kelas = kelas

    def show (self):
        print("{}\n\t Spesies : {}\n\t Ordo   : {}\n\t Classification    : {}". format(self.__nama,self.__spesies,self.__ordo,self.__kelas))

class animal_cat(animal):
      def __init__(self,__nama,__spesies,__ordo,__kelas):
        super()._init_(nama,spesies,ordo,kelas)
        super().show()

kucing = animal_cat('Kucing','Felis Catus','Carnivora', 'Mamamlia')