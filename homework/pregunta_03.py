"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import fileinput
def pregunta_03():

    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    input_file = "files/input/data.csv"  
    sequence = []

    
    with fileinput.input(files=[input_file]) as f:
        for line in f:
            sequence.append(line.strip().split('\t'))  

    
    sums = {}
    for row in sequence:
        letter = row[0]  
        try:
            value = int(row[1])  
            sums[letter] = sums.get(letter, 0) + value
        except ValueError:
            raise Exception(f"Error procesando la fila: {row}")

    
    result = sorted(sums.items())
    return result

#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run_job():
    """Job"""
    result = pregunta_03()  
    print(result)

if __name__ == "__main__":
    run_job()
