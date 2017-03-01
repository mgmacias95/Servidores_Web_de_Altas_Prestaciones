import pandas as pd
import sys

add_one_rep = lambda x: x.ix[0] + (1 - x.ix[0]) * x.ix[1]

if len(sys.argv) != 3:
    file = "tabla.csv"
    replicas = 3
else:
    file = sys.argv[1]
    replicas = int(sys.argv[2])

# leemos un csv con la información de la disponibilidad de cada uno de los componentes
availability_chart = pd.read_csv(file)

# calculamos la disponibilidad al hacer una réplica de todos los servidores
# availability_chart['Availability2'] = availability_chart[['Availability', 'Availability']].apply(add_one_rep, axis=1)

for i in range(2,replicas+1):
    name = 'Availability'+str(i)
    last_name = 'Availability' if i==2 else 'Availability'+str(i-1)
    availability_chart[name] = availability_chart[[last_name, 'Availability']].apply(add_one_rep, axis=1)

print(availability_chart)
