#Define la jerarquía: Ser Vivo → Planta → Arbol. Cada clase agrega un método propio:
#crecer(), fotosintesis(), dar_frutos(). Instancia Arbol y demuestra que puede llamar a los tres
#métodos.


class SerVivo:
    def __init__(self, a_servivo):
        self.a_servivo = a_servivo

    def crecer(self):
        return f"{self.a_servivo} está creciendo"


class Planta(SerVivo):
    def __init__(self, a_servivo, a_animal):
        super().__init__(a_servivo)
        self.a_animal = a_animal

    def fotosintesis(self):
        return f"{self.a_animal} está haciendo la fotosintesis"


class Arbol(Planta):
    def __init__(self, a_servivo, a_animal, a_perro):
        super().__init__(a_servivo, a_animal)
        self.a_perro = a_perro

    def dar_frutos(self):
        return f"{self.a_perro} está dando frutos"


# Instanciar Perro
mi_arbol = Arbol("","","")

# Probar los métodos heredados y el propio
print(mi_arbol.crecer())  # método de SerVivo
print(mi_arbol.fotosintesis())     # método de Animal
print(mi_arbol.dar_frutos())    # método de Perro
