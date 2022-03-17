entrada = input("introduce el nombre del color: \n")#declaramos para la entrada de info del usuario
colores = ("verde","azul","negro","gris","rojo")#declaramos la tupla
if entrada in colores:#primera condicion. si esta en la lista lo que escribio el usuario, imprime lo que esta dentro del if
    print("el color esta en la lista")
else:#y si no está, muestra el else
    print("el color no esta en la lista :(")