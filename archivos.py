#Manipulación de archivos

archivo = open("archivo.csv", "w")

#Encabezado en la primera linea
archivo.write("Nombre,edad,salario\n")
archivo.write("Juan Carlos Olivares Rojas,12,1000\n")
archivo.write("Aaron,30,150\n")
archivo.write("Blanca,,18\n")
archivo.write("Juan Pablo,12\n")