"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import fileinput


def pregunta_02():
    input_file = "files/input/data.csv"  # Ruta del archivo
    sequence = []

    # Cargar los datos directamente en la función pregunta_02
    with fileinput.input(files=[input_file]) as f:
        for line in f:
            sequence.append(line.strip().split('\t'))  # Separar por tabulaciones

    # Contar la cantidad de registros por letra de la primera columna
    counts = {}
    for row in sequence:
        letter = row[0]  # Primera columna (letra)
        counts[letter] = counts.get(letter, 0) + 1

    # Convertir a lista de tuplas ordenadas alfabéticamente
    result = sorted(counts.items())
    return result

def run_job():
    """Job"""
    result = pregunta_02()  # Llamar a pregunta_02 sin pasarle argumentos
    print(result)

if __name__ == "__main__":
    run_job()
