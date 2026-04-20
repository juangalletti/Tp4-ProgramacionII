#Crea una clase Electrodomestico con atributos marca y consumo_watts. Hereda en una
#clase Lavarropas y agrega el atributo capacidad_kg. Instancia la subclase y muestra todos
#los atributos.


class Electrodomestico:
    def __init__(self, Marca, consumo_watts):
        self.Marca = Marca
        self.consumo_watts = consumo_watts


class Lavarropas(Electrodomestico):
    def __init__(self, Marca, consumo_watts):
        super().__init__(Marca, consumo_watts)  # Llamada al constructor de la clase padre
        