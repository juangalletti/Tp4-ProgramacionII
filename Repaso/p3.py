class Trabajador:
    def __init__(self,nombre, salario):
        self.nombre= nombre
        self.salario=salario


class Contador(Trabajador):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)

    def ejercer_profesion(self):
        return f"{self.nombre} esta haciendo Facturaciones "
    

class Arquitecto(Trabajador):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)

    def ejercer_profesion(self):
        return f"{self.nombre} esta diseñando un edificio"
    

Arquitecto1= Arquitecto("Pedro","1")
contador1= Contador("Lucas","3")


print(contador1.ejercer_profesion())
print(Arquitecto1.ejercer_profesion())

#Contador, Arquitecto y Enfermero. Cada subclase debe implementar un método 
#ejercer_profesion() con un comportamiento diferente