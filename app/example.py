# se puede importar como script, similar a como lo hacemos en la terminal 
#Cuando utilizamos name == ‘main’ estamos dando dualidad a cierta función para que sea ejecutada en dos archivos distintos.

import main

print(main.data)
main.run()


# una de las formas para evitar que se ejecute en dos partes, es que la original este modularizada en una funcion 