#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_key = None
validador = 0
for linea in sys.stdin:
    clave, valor = linea.strip().split('\t')
    if clave == current_key:
        if int(valor) > validador:
            validador = max(validador,int(valor))
    else:
        if current_key is not None:
            print(f"{current_key}\t{validador}")
        current_key = clave
        validador = int(valor)     

# Imprimir el último resultado parcial
if current_key is not None:
     print(f"{current_key}\t{validador}")