#!/usr/bin/python
#-*- coding: utf-8 -*-

import csv
import sys
import pyperclip

def lee_csv(filename, L, delim=';'):
	try:
		f = open(filename, newline='')
	except:
		return False
	
	spamreader = csv.reader(f, delimiter=delim)
	for fil in spamreader:
		L.append(fil)
		
	f.close()
	return True

def list2file(f, L):
	for elem in L:
		f.write(elem.replace(',', '.') + '\t')
	f.write('\n')

def list2latex(L):
	if (len(L) == 0):
		return ""
	
	r = L[0]
	L = L[1:]
	
	for elem in L:
		r += " & " + elem
		
	r += " \\\\"
	
	return r

data = []

nargs = len(sys.argv)
infile = input("Introduce el nombre del fichero con los datos: ") if (nargs <= 1) else sys.argv[1]
cap = "Tabla" if (nargs <= 2) else sys.argv[2]
outfile = "tabla.tex" if (nargs <= 3) else sys.argv[3]


if (infile == "help" or infile == "-h" or infile == "--help"):
	print("""Este programa necesita recibir un archivo de texto plano
en el que las celdas estén separadas por ';'
y cuya primera columna sea el encabezado de la tabla.

Además para usarlo es necesario incluir:
	\\usepackage{booktabs}
	\\usepackage[table]{xcolor}

Así como los paquetes que se usen por parte del usario dentro de la tabla.

Sintaxis:

clatex [ArchivoEntrada] [PieDeTabla] [ArchivoSalida]
""")
	exit()

if (not(lee_csv(infile, data))):
	print("Error con la lectura del archivo de datos {}".format(infile))
	exit()

try:
	fout = open(outfile, 'w')
except:
	print("Error al abrir el archivo de salida {}".format(outfile))
	exit()

try:
	ftxt = open("TXT_" + infile, 'w')
except:
	print("Error al abrir el archivo de salida {}".format("TXT_" + infile))
	exit()

latex = """\\begin{table}[htbp]
\\rowcolors{2}{black!5}{white}
\\centering
\\begin{tabular}{ccr}
\\toprule
"""

latex += list2latex(data[0]) + "\n\\midrule\n"
ftxt.write('#')
list2file(ftxt, data[0])
data = data[1:]

for line in data:
	latex += list2latex(line) + '\n'
	list2file(ftxt, line)

latex += """\\bottomrule
\\end{tabular}
\\caption{""" + cap + """}
\\end{table}
"""

fout.write(latex)
fout.close()
ftxt.close()
pyperclip.copy(latex)
pyperclip.paste()
