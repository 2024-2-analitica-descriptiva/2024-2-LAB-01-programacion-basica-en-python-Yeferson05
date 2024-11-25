"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import fileinput
def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    input_file = "files/input/data.csv"  
    sequence = []

    with fileinput.input(files=[input_file]) as f:
        for line in f:
            sequence.append(line.strip().split('\t')) 

    result = []
    for row in sequence:
        letter = row[0] 

        if row[3] != "":
            col4_count = len(row[3].split(","))
        else:
            col4_count = 0

        
        if row[4] != "":
            col5_count = len(row[4].split(","))
        else:
            col5_count = 0

        result.append((letter, col4_count, col5_count))

    return result

#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run_job():
    """Job"""
    result = pregunta_10() 
    print(result)

if __name__ == "__main__":
    run_job()