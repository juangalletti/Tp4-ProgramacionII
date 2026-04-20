#Crea cuatro clases: W, X(W), Y(W) y Z(X, Y). Cada una implementa un método info() que 
#imprime su letra. Instancia Z y llama a info(). Luego imprime el MRO usando Z.__mro__ y 
#explica por escrito por qué se ejecuta el método de X antes que el de Y.

class W:
    def metodo(self):
        print("Esta es la letra A")

class X(W):
    def metodo (self):
        print("Esta es la letra B")

class Y(W):
    def metodo (self):
        print("Esta es la letra C")

class Z(X, Y):
    print("Esta es la letra d")


d1= Z()

d1.metodo()

print(Z.__mro__)

#Python busca primero en B y después en C