class Cow:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Saya sapi. Nama saya adalah {self.name}. Umur saya {self.age} tahun.")

    def make_sound(self):
        print("Moo")


class Wolf:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Saya serigala. Nama saya adalah {self.name}. Umur saya {self.age} tahun.")

    def make_sound(self):
        print("Awoo")


sapi = Cow("Shaun the Sheep", 2.5)
serigala = Wolf("Husk", 4)

for animal in (sapi, serigala):
    animal.make_sound()
    animal.info()
    animal.make_sound()