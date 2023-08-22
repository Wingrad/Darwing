a = 2
b = 7
c = a + b 
print(c)
Nombre = "Darwing"
Apellido = "Roa"
Nombre += "Mario" #Si escribo "nombre" de nuevo, se resetea 
print(Nombre + Apellido)


numero = 28
numero += 1
# El += es para sumarle un digito a otra variable.
numero += 76
#concatenar con + 
conteo = numero + 23 + 3
print (c + conteo)

nombre = "Melany"

#Se usa f bjhsdhidha {} para poder convertir cualquier. ES DECI: CONCATENAR CON F STRINGS.
bienvenida = f"Saludos, {nombre}, pase a la cocina."
del nombre
print(bienvenida)

# del..... sirve para desnombrar una variable, desaparecerla.
# No obstante,, si yo elimino una variable, pero anteriormente la habia puesto con {}, esta se habra convertido en texto y se mantendra en la otra variable
# BASICAMENTE, si se usa antes, lo borra, si se usa despues, se mantendra.

# OPERADORES DE PERTENENCIA E IDENTIDAD (IN Y NOT IN):
print("as" in bienvenida) #True. PEDIMOS QUE NOS DIGA SI ESA VARIABLE TIENE ESAS LETRAS.
print("aguacate" not in bienvenida) #True. QUE NOS DIGA SI NO ESTA EN LA VARIABLE.