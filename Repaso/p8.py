#Crea las clases Impresora y Escaner, sin relación de herencia, ambas con un método 
#ejecutar(). Escribe una función operar(dispositivo) que llame a dispositivo.ejecutar(). 
#Demuestra que la función acepta instancias de ambas clases sin importar su tipo.

class Impresora:
    def ejecutar(self):
        return "Guau!"

class Escaner:
    def ejecutar(self):
        return "Miau!"


# Función polimórfica
def hacer_sonido(dispositivo):
    print(dispositivo.ejecutar())


im1= Impresora()

hacer_sonido(im1)