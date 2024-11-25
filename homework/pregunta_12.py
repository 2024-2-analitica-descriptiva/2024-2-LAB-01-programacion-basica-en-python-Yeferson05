"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import fileinput

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    input_file = "files/input/data.csv"
    
    sequence = []

    with fileinput.input(files=[input_file]) as f:
        for line in f:
            sequence.append(line.strip().split('\t'))

    result = {}

    for row in sequence:
        if len(row) < 5:
            continue
        
        col1_value = row[0]
        col5_value = row[4]

        values = col5_value.split(',')

        sum_value = 0

        for value in values:
            number = value.split(":")[1]
            sum_value += int(number)

        if col1_value in result:
            result[col1_value] += sum_value
        else:
            result[col1_value] = sum_value
    return result

#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run_job():
    """Job"""
    result = pregunta_12()  
    print(result)

if __name__ == "__main__":
    run_job()