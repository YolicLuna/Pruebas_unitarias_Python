# ¿Qué son la pruebas unitarias?

La spruebas unitarias son pruebas automatizadas que tienen como objetivo verificar el funcionamiento de una unidad de codigo. 
La unidad podría definirse como una parte muy pequeña de una aplicación o programa, puede ser una rituna, una funcion, un metodo, etc.

## Ventajas

Una de las ventajas es poder dividir nuestro codigo en unidades, lo que permite encontrar los problemas, bugs, de forma mas sencilla. dando la seguridad de que si en algun momento queremos realizar un cambio sobre el proyecto sin temer a que otras partes del proyecto dejen de funcionar.
Esto hace que nuestros proyectos se vuelven mucho mas falices de mantener. 

Otra ventaja es que indirectamente estaremos documentando nuestro codigo, por lo que tendremos un panorama mas amplio de lo que construimos, que se necesita y que es lo que no se necesita. 


Las pruebas unitarias trabajan de manera independiente una de otra, no importa cuantas pruebas tengamos en el mismo proyecto, cada una no dependera de la otra para realizar su trabajo, el cual será testear la unidad de codigo


# Documentacion con comentarios

Recordemos que el caracter numeral # nos permite comentar una sola linea de codigo.

Ejemplo: # Esta funcion sirve para sumar

Mientras que las triples comillas dobles """ """ o triple comillas somples ''' ''' nos permite que nuestros comentarios tengan saltos de linea.

Ejemplo:

""" 
Esta funcion sirve para sumar todos los resultados
de las ventas del mes pasado.
"""
'''
Esta funcion sirve para sumar todos los resultados
de las ventas del mes pasado.
'''

Recordemos que dentro de los comentarios de triples comillas podemos usar las otras comillas.

Ejemplo:
""" 
Esta funcion sirve para sumar todos los resultados
de las ventas del mes pasado de la tabla ''' ventas '''.
"""
'''
Esta funcion sirve para sumar todos los resultados
de las ventas del mes pasado de la tabla """ ventas """.
'''

Recordemos que Python ignora las lineas comentadas, así que, al encontrarse con estas lineas, Python no las ejecutará. 
Los comentarios sirven para documentar y/o testear nuestro codigo.
 
