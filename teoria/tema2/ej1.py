import pandas as pd
import sys
from tabulate import tabulate

add_one_rep = lambda x: x.ix[0] + (1 - x.ix[0]) * x.ix[1] if x.ix[2] else x.ix[1]

if len(sys.argv) != 3:
    file = "tabla.csv"
    replicas = 3
else:
    file = sys.argv[1]
    replicas = int(sys.argv[2])

# leemos un csv con la información de la disponibilidad de cada uno de los componentes
availability_chart = pd.read_csv(file)

# calculamos la disponibilidad las réplicas de todos los servidores
for i in range(2,replicas+1):
    name = 'Availability'+str(i)
    last_name = 'Availability' if i==2 else 'Availability'+str(i-1)
    availability_chart[name] = availability_chart[[last_name, 'Availability', 'Replicate']].apply(add_one_rep, axis=1)

# remove replicate flag column
del availability_chart['Replicate']

print(tabulate(availability_chart, headers='keys', tablefmt='pipe', showindex=False))
