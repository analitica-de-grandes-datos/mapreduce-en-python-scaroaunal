#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for linea in sys.stdin:
  lista = linea.split(",")
  credit_history = lista[2]
  print(f"{credit_history}\t1")