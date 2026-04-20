class Dispositivo:
    def __init__(self,nombre):
        self.nombre=nombre

class Portatil (Dispositivo):
    def __init__(self, nombre):
        super().__init__(nombre)

    def Cargar_Bateria(self):
        print(f"Soy {self.nombre} y necesito carga")

class Conectado(Dispositivo):
    def __init__(self,nombre):
        super().__init__(nombre)

    def Conectar_red(self):
        print(f"Soy {self.nombre} y necesito Red")

class Laptop (Portatil ,Conectado ):
    def __init__(self, nombre):
        Portatil .__init__(self, nombre)
        Conectado .__init__(self, nombre)


Sam= Laptop("Samsung")
Sam.Cargar_Bateria()
Sam.Conectar_red()
