#Define las clases Volador (con método volar()) y Nadador (con método nadar()). Crea la 
#clase Pato que herede de ambas y agrega el método graznar(). Instancia Pato y prueba los 
#tres métodos. 

class Volador:
    def __init__(self,a):
        self.a=a

    def Volar(self):
        return f"esta volando"
    
class Nadador:
    def __init__(self, b):
        self.b= b

    def Nadar(self):
        return f"esta nadando"
    
class Pato(Volador,Nadador):
    def __init__(self, a,b):
        Nadador.__init__(self,a)
        Volador.__init__(self,b)

    def gaznar(self):
        return f"Esta gaznando"
    

Patricio= Pato("", "")

print(Patricio.gaznar())
print(Patricio.Volar())
print(Patricio.Nadar())