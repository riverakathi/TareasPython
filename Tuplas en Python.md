## Tuplas en Python
# Las tuplas son un tipo de dato que permite almacenar información, por tanto forma parte de los tipos de datos colección. Las tuplas guardan los datos en forma de vectores y su uso es muy similar a las listas, con la salvación de que las tuplas son inmutables , y por lo tanto no pueden modificar los datos una vez inicializados.

#Creación de Tuplas
Una tupla se define utilizando paréntesis () y separando los elementos por comas. Por ejemplo:
```sh
mi_tupla = (1, 2, 3, 4, 5,6)
```
#Acceso a elementos:
Los elementos de una tupla se pueden acceder mediante índices, de la misma manera que en las listas. Por ejemplo:
```sh
print(mi_tupla[0])  # Imprime el primer elemento: 1
```
#Modificación y Eliminación de Tuplas:
Dado que las tuplas son inmutables, no se pueden modificar ni eliminar elementos individualmente. Sin embargo, se pueden eliminar la tupla completa utilizando la palabra clave del. Por ejemplo:
```sh
del mi_tupla
```
#Diferencias con Listas:
- Mutabilidad: Las listas son mutables, lo que significa que se pueden modificar, agregar o eliminar elementos después de su creación. Las tuplas, por otro lado, son inmutables y no se pueden modificar una vez creadas.
- Las listas se definen utilizando corchetes [], mientras que las tuplas utilizan paréntesis ().
- Rendimiento: Las operaciones en tuplas suelen ser más rápidas que en listas debido a su inmutabilidad.

#Usos Comunes de Tuplas
>Retorno múltiple de valores desde funciones: Una función puede devolver una tupla de valores, y el llamador puede desempaquetar la tupla para acceder a los valores individuales.
>Diccionarios como clave: Dado que las tuplas son inmutables, pueden usarse como claves en diccionarios, mientras que las listas no pueden.
>Representación de datos estructurados: Las tuplas se pueden usar para representar datos estructurados cuando la estructura de datos no debe cambiar.
>Iteración eficiente: Las tuplas son más eficientes que las listas para iterar sobre grandes conjuntos de datos debido a su inmutabilidad.

## Métodos disponibles sobretuplas
- count(): Devuelve el número de ocurrencias de un elemento en la lista
```sh
tuple.count('p')
```
- index(): Devuelve el índice que ocupa un elemento
```sh
tuple.index('e')
```
##Ejercicios
1- Crea una tupla con números del 1 al 5 y muestra su longitud.
```sh
tupla_numeros = (1, 2, 3, 4, 5)
print("Longitud de la tupla:", len(tupla_numeros))
```
2- Accede al segundo elemento de una tupla de nombres.
```sh
tupla_nombres = ('Migel', 'Luis', 'Kevin')
print("Segundo elemento de la tupla:", tupla_nombres[1])
```
3- Concatena dos tuplas y muestra el resultado.
```sh
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print("Tupla concatenada:", tupla_concatenada)
```
4- Intenta modificar un elemento en una tupla y observa el error resultante.
```sh
tupla_modificar = (1, 2, 3)
# Intentar modificar un elemento
# Esto generará un error: tupla_modificar[0] = 5
```
5- Crea una tupla con una lista como elemento y verifica si la lista se puede modificar.
```sh
tupla_lista = ([1, 2, 3],)
tupla_lista[0][0] = 100
print("Lista modificada en la tupla:", tupla_lista)
```
6- Crea una tupla con tres valores y desempaquétalos en tres variables.
```sh
tupla_valores = (15, 26, 33)
x, y, z = tupla_valores
print("Desempaquetado de valores:", x, y, z)
```
7- Convierte una tupla en una lista.
```sh
tupla_original = (1, 2, 3)
lista_convertida = list(tupla_original)
print("Tupla convertida en lista:", lista_convertida)
```
8- Crea una tupla vacía y verifica su tipo.
```sh
tupla_vacia = ()
print("Tipo de la tupla vacía:", type(tupla_vacia))
```
9- Crea una tupla con un solo elemento numérico y verifica su tipo.
```sh
tupla_un_elemento = (42,)
print("Tipo de la tupla con un solo elemento:", type(tupla_un_elemento))
```
10- Utiliza una tupla como clave en un diccionario y asigna un valor a esa clave.
```sh
diccionario = {}
tupla_clave = (1, 2)
diccionario[tupla_clave] = "Valor"
print("Diccionario con tupla como clave:", diccionario)
```
-Rivera Kathia
