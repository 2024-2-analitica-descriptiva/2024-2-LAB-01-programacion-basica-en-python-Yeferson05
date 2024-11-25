"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import fileinput


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    input_file = "files/input/data.csv"  
    sequence = []

   
    with fileinput.input(files=[input_file]) as f:
        for line in f:
            sequence.append(line.strip().split('\t'))  

    
    data = {}
    for row in sequence:
        column_5 = row[4]  
        pairs = column_5.split(",")  
        for pair in pairs:
            key, value = pair.split(":") 
            value = int(value) 
            if key not in data:
                data[key] = []  
            data[key].append(value)
             
    result = []
    for key in sorted(data.keys()): 
        min_val = min(data[key])
        max_val = max(data[key])
        result.append((key, min_val, max_val))

    return result

#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run_job():
    """Job"""
    result = pregunta_06()  
    print(result)

if __name__ == "__main__":
    run_job()
