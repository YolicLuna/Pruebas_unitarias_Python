# Cobertura de codigo.

La cobertura de codigo es una medida porcentual que nos permite conocer que porcentaje de nuestro codigo a sido ejecutado y probado. Esto nos permite que, apartir de los resultados, nosotros podamos mejorar nuestro codigo o refactorizar. 

Para poder implementar la cobertura de codigo en Python, lo recomendable es trabajar con la libreria coverage. 

Para poder realizar la cobertura, haremos uso de las pruebas unitarias.
En consola ejecutamos "coverage run -m pytest", lo que hara que todas las pruebas de nuestro proyecto sean ejecutadas y la cobertura aplicara a todo.
Pero tambien podemos ser puntuales al ejecutar un archivo en especifico, esto se hace agregando la ruta al comando "coverage run -m pytest test/test_task.py", en el caso del comando de ejemplo, estariamos ejecutando solo las pruebas existentes en el archivo test_task.py.

Despues de la primer ejecucion, beremos que se crea unarchivo .coverage, el cual contiene los resultados de la cobertura de nuestro codigo. 
Para revisar su contenido deberemos ejecutar el comando "coverage report" y lo que se nos mostrara es un listado de los archivos que se ejecutaron y el porcentaje de codigo que se ejecuto de cada uno, es decir, a menor porcentaje, menor codigo fue ejecutado.
Si queremos mas informacion, podemos hacer uso de la bandera "-m".
Asi que al ejecutar "coverage report -m" ahora se nos mostrara, para cada archivo, las lineas en las que se encuentra el codigo que no fue ejecutado.

Lo recomendable es que nosotros creemes el archivo de cobertura usando las pruebas unitarias porque atraves de ellas es como estaremos probando nuestra app.

Todo lo dicho anteriormente funciona igual al trabajar con Unittest pero deberemos sustituir la palabra pytest por unittest en los comandos ejecutados.