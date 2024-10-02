#EJEMPLO NUMERO UNO

class clase1:

    def sumar(num1,num2):
        return num1+num2


print (clase1.sumar(4,3.6))

#EJEMPLO NUMERO DOS

class Almacen:
    contador=1
    def __init__(self,Nombre):
        self.nombre=Nombre
    
    def imprimir_datos(self):
        print(self.nombre)
    
almacen1=Almacen('Exito')
almacen1.imprimir_datos()
print(almacen1.contador)

#EJEMPLO NUMERO TRES

class Almacen:
    contador=0
    def __init__(self,Nombre):
        self.nombre=Nombre
        Almacen.contador+=1
    def imprimir_datos(self):
        print(f'Datos : {self.Nombre}')

almacen1=Almacen('Exito')
almacen2=Almacen('Carulla')
almacen3=Almacen('Surtimax')
almacen4=Almacen('Katronix')
print(almacen1.nombre)
print(almacen1.contador)

#EJEMPLO NUMERO CUATRO

class Circulo:

    PI=3.1416
    def __init__(self,radio:float):
        self.radio=radio

radio1=(5*5)
resul=Circulo(radio1*Circulo.PI)

print(resul.radio)

#EJEMPLO NUMERO CINCO


numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero: "))


class Ecuacion:
    def __init__(self,numero1:int,numero2:int):
        self.numero1=numero1
        self.numero2=numero2

    def suma():
        return numero1+numero2
    
    def division():
        if numero2 == 0:
            print("NO PUEDO DIVIDIR")
        else:
            return numero1//numero2
    
    def multiplicacion():
        return numero1*numero2
    
    def resta ():
        return numero1-numero2
    

print(f'Suma: {Ecuacion.suma()}')
print(f'Resta: {Ecuacion.resta()}')
print(f'Multiplicación: {Ecuacion.resta()}')
print(f'Division: {Ecuacion.division()}')