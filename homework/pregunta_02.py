"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import fileinput


def pregunta_02():
    input_file = "files/input/data.csv"  
    sequence = []

    
    with fileinput.input(files=[input_file]) as f:
        for line in f:
            sequence.append(line.strip().split('\t')) 

   
    counts = {}
    for row in sequence:
        letter = row[0]  
        counts[letter] = counts.get(letter, 0) + 1

    
    result = sorted(counts.items())
    return result
#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run_job():
    """Job"""
    result = pregunta_02()  
    print(result)

if __name__ == "__main__":
    run_job()
