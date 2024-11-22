import fileinput
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""



def pregunta_01():
    input_file = "files/input/data.csv"  # Ruta del archivo
    sequence = []
    
    # Cargar los datos directamente en la función pregunta_01
    with fileinput.input(files=[input_file]) as f:
        for line in f:
            sequence.append(line.strip().split('\t'))  # Separar por tabulaciones

    total = 0
    for row in sequence:
        try:
            total += int(row[1])  # Sumar el valor de la segunda columna
        except ValueError:
            raise Exception(f"Error procesando la fila: {row}")
    
    return total

#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run_job():
    """Job"""
    result = pregunta_01() 
    print(result)


if __name__ == "__main__":
    run_job()
