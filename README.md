# Tarea 7: Pruebas de software UTFSM 2020-1
Búsqueda visual consiste en verificar si el texto de una imagen control se encuentra en las imagenes de prueba entregadas.

## Instrucciones
Código desarrollado en python3.
Librerias necesaria: 
- boto3 : pip install boto3

Las pruebas se realizan sobre archivos que deben estar en un AWS S3 bucket.
Para acceder a este y realizar las pruebas requeridas debes modificar el archivo 'info.txt' agregando los datos segun corresponda, por ejemplo

- nombre_backet = nameMyBacket
- img_control = control.png
- img_pruebas = p1.png, p2.png, p3.png

Donde 'nameMyBacket' corresponde al nombre de tu backet AWS S3.
'control.png' corresponde al nombre de la imagen de control junto a su extensión.
'p1.png' , 'p2.png' , 'p3.png' corresponden a los nombres de las imagenes que serán comparadas con la imagen control. Estos nombres deben estar separados por una coma.

### Respuestas
Se puede observar los resultados de comparación en el archivo 'log.txt' presente en la carpeta raiz.
