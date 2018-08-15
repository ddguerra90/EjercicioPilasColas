from cola import *
from pila import *
from libro import *

pila = Pila()
pilaEncontrado = Pila()

def asignarLibro (nom):
    libro = Libro(nombre)
    pila.apilar(libro)

def agruparLibros(b, libEnc):
    c=0
    pilaEncontrado.desapilar()
    while(c< (b-1)):
        libro = pilaEncontrado.desapilar()
        pila.apilar(libro)
        c=c+1
    pilaEncontrado.apilar(libEnc)
    mostrarLibros()

def mostrarLibros():
    c=0
    find = False
    print "LIBROS EN STOCK"
    while(c< (a-1)):
        lib = pila.desapilar()
        print lib.nombre
        c=c+1
    c=0
    print "LIBRO ENCONTRADO"
    print((pilaEncontrado.desapilar()).nombre)

def reordenarLibros():
    d=0
    while (d<a):
        desapilar = pilaEncontrado.desapilar()
        pila.apilar(desapilar)
        d = d+1

def consultar():
    var = raw_input("Ingrese el nombre del libro a consultar: ")
    busquedaLibro(var)

def busquedaLibro(var):
    b=0
    while (b<a):
        busquedaLibro = pila.desapilar()
        pilaEncontrado.apilar(busquedaLibro)
        b=b+1
        if(busquedaLibro.nombre == var and b==1):            
            mostrarLibros()
            break
        elif(busquedaLibro.nombre == var):        
            print "Libro Encontrado"            
            agruparLibros(b, busquedaLibro)
            break
        elif b==3:
            print "Libro No Encontrado"
            reordenarLibros()
            consultar()
    
i=1
a=0
while (i != 0):
    nombre = raw_input("Ingrese el nombre del libro: ")
    asignarLibro(nombre)
    a=a+1
    i = int(input("¿Desea ingresar otro libro? 1 Si/0 No:  "))
    if(i==0):
        consultar()
        
        

