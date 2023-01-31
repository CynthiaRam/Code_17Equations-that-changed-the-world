# Propósito:
# Basándome en la obra de Ian Stewart ("17 Equations that changed the world") y ya que fue un placer haber
# leído su libro he decidido crear un script en Python por cada una de las ecuaciones mencionadas por Stewart
# con la finalidad de mostrar un poco su visión al mencionar la importancia de las mismas que a su criterio cambiaron 
# al mundo.
""" 
El teorema de pitagoras nos habla de la relacion que tienen los tres lados de un trinagulo rectangulo, nos permite calcular
distancias en terminos de coordenadas.

IMPACTO.- Topografía, Navegación, Relatividad Gral, teorias del espacio, el tiempo y la gravedad

Formula.- C** = a** + b**

"""
import math 

class Triangulo:
    
    def __init__(self,hipotenusa,catetoA,catetoB):
        
        self.hipotenusa = hipotenusa
        self.catetoA = catetoA
        self.catetoB =catetoB

    def calcular(self):
        if self.hipotenusa == 0:
            self.hipotenusa = math.sqrt((self.catetoA ** 2) + (self.catetoB ** 2))
            print("Hipotenusa = {:.2f} ".format(self.hipotenusa))
        else:  
            print("aqui")  
            if self.catetoA == 0:
                self.catetoA = math.sqrt((self.hipotenusa ** 2) - (self.catetoB ** 2))
                print("Cateto A =  {:.2f}".format(self.catetoA))
            else: 
                if self.catetoB == 0:
                    self.catetoB = math.sqrt((self.hipotenusa ** 2) - (self.catetoA ** 2))
                    print("Cateto B =  {:.2f}".format(self.catetoB))

triangulo = Triangulo(15,12,0)
triangulo.calcular()

