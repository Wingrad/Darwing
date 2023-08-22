#SON DATOS COMPLEJOS LOS QUE TIENEN VARIOS DATOS SIMPLE O UNO DENTRO DE OTRO.


#ESTA LISTA(ES UN TIPO DE MATRIZ) CONTIENE DIFERENTES TIPOS DE DATOS. SE USAN CORCHETES Y SE PUEDEN CAMBIAR LOS VALORES.
lista = ["Darwing Roa", "Villa mella", True, 188]
print(lista)

lista1 = ["Dalberg Roa", "soltero", 18, False, 18]
#ABAJO IMPRIMO EL ELEMENTO 1, QUE ES EL INDICE 0 DE MI LISTA. (0,1,2,3,4). SE REPITEN DATOS SI QUEREMOS.
print(lista1[2])

lista1[3] = 5824
print(lista1[3])
print(lista1)

Persona1 = ["Darwing Roa Lora", 17, 186]
print("Nombre completo:", Persona1[0], "Edad:", Persona1[1], "Altura:", Persona1[2] )




#EN LA TUPLA SE USAN (), pero se muestran con [] tambien.
#LA DIFERENCIA ES QUE EN LA TUPLA NO SE PUEDEN HACER CAMBIOS, EN LA LISTA SI. SI SE REPITEN DATOS SI QUIERES.
tupla = ("Huevos", "12 carnes", 911, False)
print(tupla[2])
#  ESTO ES LO QUE NO SE PUEDE HACER       tupla[0] = "mama"
print(tupla[0])




#Creando un conjunto (set) - No tiene ningun orden y todo puede cambiar de lugar, PERO LOS ELEMENTOS 
# tampoco SE CAMBIAN; NO SE REPITEN VALORES

Conjunto = {"Avion", 77, False}

# SE PUEDE RECONSTRUIR, PERO NO CAMBIAR VALORES. NO SE REPITEN VALORES
Conjunto = {"dalbergxdxddxd", 79}
#NO SE PUEDE MOSTRAR UN subindice EN ESPECIFICO --- EJ: print(Conjunto[0]), pero si completo
print(Conjunto)

