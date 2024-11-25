"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import fileinput
def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    input_file = "files/input/data.csv"  
    sequence = []


    with fileinput.input(files=[input_file]) as f:
        for line in f:
            sequence.append(line.strip().split('\t'))  

    result = {}

    for row in sequence:
        col2_value = int(row[1]) 
        col4_value = row[3]

        for letter in col4_value.split(','):
            letter = letter.strip() 
            if letter in result:
                result[letter] += col2_value 
            else:
                result[letter] = col2_value

    return dict(sorted(result.items()))  

#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run_job():
    """Job"""
    result = pregunta_11()  
    print(result)

if __name__ == "__main__":
    run_job()