class Uno:
    
    Especialidad=('Ejecutivo')
    
    def __init__(self,nombre:str):
        self.Nombre=nombre
            
    def dar_puestos(self):
        return (f"{self.Nombre} es un {Uno.Especialidad}")

nombre1=Uno('Jhon')
nombre2=Uno('Pepe')
print(nombre1.dar_puestos())
print(nombre2.dar_puestos())

# class Dos:
    
#     Servicios = 0
    
#     def __init__(self,Menu:str):
#         self.Menu=Menu
        
#     def Numero_Plato(self):
#         Dos.Servicios +=1
#         print (f'{Dos.Servicios}. {self.Menu}')

# Palto=Dos('Arroz con leche')
# Palto2=Dos('Ajiaco')
# print(Palto.Numero_Plato())
# print(Palto2.Numero_Plato())

# class Tres:
    
#     Lugar = "Biblioteca Soacha"
    
#     def __init__(self,libro:str) :
#         self.Libro=libro
        
#     def Pedido (self, nuevo_lugar=None):
#         if nuevo_lugar:
#             Tres.Lugar = nuevo_lugar
#         print (f'{self.Libro} este libro se encuentra en la: {Tres.Lugar}')

# lib=Tres('100 años de soledad')
# lib.Pedido()

# lib2=Tres('El arte de la guerra')
# lib2.Pedido("Biblioteca de suba")

# class Cuatro:
    
#     Tipo = "Animal"
    
#     def __init__(self,nombre:str) :
#         self.Nombre=nombre
        
#     def Tipos (self, nuevo_tipo=None):
#         if nuevo_tipo:
#             Cuatro.Tipo = nuevo_tipo
#         print (f'{self.Nombre} es un(a): {Cuatro.Tipo}')

# Nom=Cuatro('GATO')
# Nom.Tipos()

# Nom2=Cuatro('Jhon')
# Nom2.Tipos("Persona")

# class Cinco: 
    
#     contador =   0
    
#     def __init__(self,nombres:str) :
#         self.Nombres=nombres
#         Cinco.contador +=1
        
#     def cantidad (self):
#        print(f'Datos : {self.Nombres}')
        
# empleado=Cinco('Luis')
# empleado2=Cinco('Nicola')
# empleado3=Cinco('Pepe')
# empleado4=Cinco('Kiloloco')
# print(Cinco.contador)

# class Seis:
    
#     def __init__(self) -> None:
#         pass
    

# SEGUNDO PUNTO 

# numero1=int(input("Ingrese el primer numero: "))
# numero2=int(input("Ingrese el segundo numero: "))

# class Uno:
#     def __init__(self,numero1:int,numero2:int):
#         self.numero1=numero1
#         self.numero2=numero2
        
#     def suma():
#         return numero1+numero2

# print(f'Los Numeros Sumados dan: {Calculadora.suma()}')


num=int(input('Ingrese el numero que desea saber si es par o impar: '))

class Dos:

    def es_par():
        if num % 2 == 0:
            print (f'{num} es par')
        else:
            print (f'{num} es impar')
         

print(Dos.es_par())

num=int(input('Ingrese el numero: '))

# class Tres:
    
#     def es_primo():
#         if num<= 1:
#             return False
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True

# print(Tres.es_primo())  

# class Cuatro:
    
#     def maximo(lista):
#         if not (lista):
#             return ('LLena la lista por favor')
#         grande=max(lista)
#         pequeño=min(lista)
#         return f'{grande} es el numero mas grande', f'{pequeño} es el numero mas pequeño '
# desconocido=Cuatro.maximo([3, 25, 18, 40, 1])

# print(desconocido)

#Punto 3 y 4 ya unidos

class Uno:
    contador = 0

    def __init__(self, libros):
        self.libros = libros
        Uno.contador += 1  
        print(f'TENEMOS : {self.libros}')
        
    def reset_contador(self):
        Uno.contador = 0

    def contar(self):
        return Uno.contador


lib1 = Uno('El pecado sin conocer')  
lib2 = Uno('Silencio')
print(f'Cantidad de libros: {lib1.contar()}')   

