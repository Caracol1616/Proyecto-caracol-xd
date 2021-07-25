import time,  sys

from random import choice
#Funciones
def sutil(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(12. / 150)

def numeral(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(3. / 250)

def flashas(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(2. / 120)

def carga(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(3. / 100)

def opcion(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(8. / 200)

def lento(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 200)

def proceso(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(15. / 150)
      
  
# Colores

YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
RR = "\033[31;1m" # Red light
M = "\033[35;1m" # morado
GL = "\033[96;1m" #Blue aqua
C = "\033[36;1m"   #Cyan
W = "\033[0;1m"    #White
B = "\033[34m"    #Blue


i = 0
nome = ['Nombre']
nime = [True]
while i <= 50:
    i = i + 1
    class laberinto:

# Atributos del laberinto:

       Nombre = 'Laberinto'
       Animal = 'Valleta'
       Raza = 'Valleta ofc'
       Especie = 'Caracol'
       Tiempo = 5

#Metodos para la función de Laberinto

       def __init__(self) -> None:
          if nime[-1] == True:
             print (YY +self.Nombre + "  De juegos!")
             cao = self.Nombre
             nome.append(cao)
             nime.append(False)
             
             
             


       def Futbol(self):
          print(GL +"Que jugador ha ganado mas de 3 balones de oro")
          input('enter para ver la respuesta')
          for c in range (5):
          	print(B + 'Procesando')
          time.sleep(0.2)
          print(GG +self.Nombre +" Respuesta correcta: Messi")
          
       def Musica(self):
          print(M +self.Nombre+" Que cantante recibio el premio nobel de la literatura en 2017")
          input('enter para ver la respuesta')
          for c in range(5):
            print(M+'Procesando')
            time.sleep(1) 
          print(GG +self.Nombre +' Respuesta correcta : Bob Dylan cantante de musica popular')
       def Vehiculos (self):
          k = self.Nombre
          print(GG +self.Nombre + ' ')
          d = choice(['n', 'p'])
          if d == 'n':
            print(W+ k + ' De que marca fue el primer vehiculo construido y en que año?')
            
            input('Enter para ver la respuesta')
            for c in range (5):
            	print(RR + 'Procesando')
            time.sleep(0.3)
            print( GG+ k + ' La respuesta correcta es : benz patent año 1886')
          else:
            print(RR+ k + ' Respuesta no valida')
       def jugar(self):
           p = choice(['Un laberinto', 'Un carro', 'Una computadora', 'Una tablet', 'Una ps5'])
           print (GG +self.Nombre + ' Puedes escoger entre los temas anteriores ve a probarlos!!')
           time.sleep(0.2)
           print(GG+ self.Nombre + ' Estamos trabajando para mejorar tu comodidad!')

    # Funcion de mi laberinto

    clase = laberinto()
    time.sleep(0.5)
    print(GG+ '''
1) Futbol
2) Musica
3) Vehiculos
4) jugar''')
    try:
       c = int(input(YY+ 'Elige una opcion:'))
    except ValueError:
       print(RR +'Porfavor elige un numero de los que se encuentran en la lista')
    if c == 1:
       clase.Futbol()
    elif c == 2:
       clase.Musica()
    elif c == 3:
       clase.Vehiculos()
    elif c == 4:
       clase.jugar()
    else:
       print(RR+ "Porfavor elige un numero de los que estan en la lista")
else:
    print(YY+ f'Encontraste la salida{nome[-1]}')