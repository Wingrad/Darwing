animal = "chancHItoo felizo     "
print(animal.upper())#para poner todo en mayus... (.upper())
print(animal.lower()) #para poner todo en minus... (.lower())
print(animal.strip().capitalize())#para poner la primera letra mayus...(.capitalize)
print(animal.title())#pone la primera letra de cada plabra en mayus...(.title)
print(animal.strip()) #borra todos los espacios de la derecha/izquierda
print(animal.lstrip())#borra todos los espacios de la izquierda (.lstrip())
print(animal.rstrip())#borra todos los espacios de la derecha (.rstrip())
print(animal.find("HI"))#busca esa letra/numero y si esta en el texto aparece el numero el indice y si no esta te da un numero (.find())
print(animal.replace("c", "h"))#remplaza letras(.replace( , ))
print("c" in animal)#te responde true si se encuentra y false si no(" la letra que busca" in variable)
print("c" not in animal)#lo contrario de lo anterior
