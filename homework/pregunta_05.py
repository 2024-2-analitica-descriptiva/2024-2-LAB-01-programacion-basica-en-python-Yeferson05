"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import fileinput

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    input_file = "files/input/data.csv"  
    sequence = []

    
    with fileinput.input(files=[input_file]) as f:
        for line in f:
            sequence.append(line.strip().split('\t'))  

    
    data = {}
    for row in sequence:
        letter = row[0]  
        value = int(row[1])  
        if letter not in data:
            data[letter] = []
        data[letter].append(value)
        
    result = []
    for letter in sorted(data.keys()):  
        max_val = max(data[letter])
        min_val = min(data[letter])
        result.append((letter, max_val, min_val))

    return result

#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run_job():
    """Job"""
    result = pregunta_05()  
    print(result)

if __name__ == "__main__":
    run_job()
