nombre = "Nicolas"
print(nombre)

apellido= "Molina Rey"
print(apellido)

nombreCompleto=nombre+" "+apellido

print(nombreCompleto)

quote = "Yo soy Nicolas "
print(quote)

quote2= "Ella dijo Hola"
print(quote2)


template = "Hola mi nombre es "+ nombre + "y mi apellido es "+ apellido
print(template)

template="Hola mi nombre es {} y mi apellido es {}".format(nombre,apellido)
print("v2", template)


template=f"Hola, mi nombre es {nombre} y mi apellido es {apellido}"
print("v3",template)