import pandas as pd
import sys

add_one_rep = lambda actual, single: 100 * (actual + (1 - actual) * single)

if len(sys.argv != 3):
    file = "tabla.csv"
    replicas = 3
else:
    file = sys.argv[1]
    replicas = int(sys.argv[2])

# leemos un csv con la información de la disponibilidad de cada uno de los componentes
availability_chart = pd.read_cs(file)

