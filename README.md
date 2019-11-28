# clatex
Este programa realizado en Python 3.x y usando el paquete pyperclip. Está pensado para generar tablas en LaTeX a partir de un archivo de texto.

# 1.Instalación

Primero de todo hay que clonar el repositorio:

git clone "https://github.com/azzorini/clatex"

Instalación manual: Para instalar este programa no hay más que tener instalado el paquete pyperclip, mover el archivo clatex.py a una carpeta del PATH y darle a dicho programa permisos de ejecución (en caso de no tener Python 3 como python será necesario cambiar la primera línea de clatex.py y cnelatex.py para indicar que se ejecute con Python 3).

Instalación automática (Beta): Existe la opción de utilizar el instalador que básicamente instalará pyperclip usando pip, copiará los archivos a /usr/local/bin (directorio que está en el PATH por defecto) y les dará permiso de ejecución, para ello haremos desde el directorio clonado:

chmod +x Install && sudo ./Install

Este instalador no está muy bien desarrollado y se aconseja un uso responsable de él (se recomienda la instalación manual)

# 2.Utilización

Hay dos comandos distintos que tienen dos fines diferentes: clatex y cnelatex. En lo que sí coinciden ambos es que:

1) Necesitan un archivo de entrada que sea un texto plano cada línea será una fila de la tabla y dentro de cada línea las diferentes celdas irán separadas por el caracter punto y coma (;). Es decir, en una variedad muy concreta de formato CSV.

2) La salida de este programa consiste en varias cosas:

  -Genera un archivo de latex (por defecto tabla.tex) con el código de la tabla.
  -Copia el código de la tabla al portapapeles.
  -Genera un archivo similar al de los datos pero con un "TXT_" delante que es el mismo archivo pero con la cabecera comentada y con todas las celdas separadas por tabuladores en lugar de con puntos y comas. De cara a que si se quiere procesar estos datos sea sencillo usando este fichero.

3) Para dudas sobre el uso del programa se puede poner el nombre del programa seguido de: help, -h o --help. Por ejemplo:

clatex help

cnelatex -h

4) La sintaxis es:

clatex/cnelatex [ArchivoEntrada] [PieDeTabla] [ArchivoSalida]

[ArchivoEntrada]: Es el fichero con los datos que hay que meter en la tabla, por lo tanto es indispensable si no se pasa como parámetro el programa nos lo pedirá por teclado.

[PieDeTabla]: Es el contenido que queremos que se muestre en el pie de la tabla. Por defecto es simplemente "Tabla", aunque es una cosa que se puede editar a posteriori en el código LaTeX generado.

[ArchivoSalida]: Es el archivo de LaTeX al que se va a copiar el código generado. Por defecto es "tabla.tex". Es una opción que no considero excesivamente útil pues ya te copia el contenido al portapapeles, pero se incluye por si en ciertas situaciones es de utilidad.

CLATEX

Convierte el archivo CSV en una tabla donde la primera línea es la cabecera y el resto de líneas corresponden a celdas separadas. Todas las celdas son consideradas como texto y por lo tanto salvo que se indique lo contrario serán tratadas como LaTeX trata el texto. Es decir el archivo ha de ser de la forma:

Cabecera 1;Cabecera 2;Cabecera 3

Celda 11;Celda 12;Celda 13

Celda 21;Celda 22;Celda 23

Celda 31;Celda 32;Celda 33

CNELATEX

Está pensado para tratar los datos como números (en notación inglesa) y además utiliza la primera mitad de celdas como datos y la segunda mitad de celdas como sus errores. Así que el formato que hay que usar sería el siguiente:

x;y

x 1;y 1;Error x 1;Error y 1

x 2;y 2;Error x 2;Error y 2

x 3;y 3;Error x 3;Error y 3

x 4;y 4;Error x 4;Error y 4

Nótese que las celdas serán tratadas ya, por defecto, como números, lo que dificulta que se pueda introducir texto en ellas.
