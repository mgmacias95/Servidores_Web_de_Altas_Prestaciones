# Tema 4 - Balanceadores de carga

__1. Buscar información sobre cuánto costaría en la actualizad un _mainframe_. Comparar precio y potencia entre esa máquina y una granja web de unas prestaciones similares.__

### IBM z Systems Mainframes
El [IBM z13s](http://www-03.ibm.com/systems/z/hardware/z13s.html) es un servidor _mainframe_ de altaras prestaciones. En la página oficial de IBM podemos ver sus principales características pero, para poder entenderlas, es mejor consultar primero la [página de Wikipedia](https://en.wikipedia.org/wiki/IBM_zEnterprise_System#PU_characterization) sobre estos ordenadores. Tienen distintos tipos de procesadores: de carácter general (_**C**entral **P**rocessor_), para sistemas operativos Linux (_**I**ntegrated **F**acility for **L**inux_), para operaciones I/O y cuentas de usuario (_**S**ystem **A**ssist **P**rocessor_), para ejecutar Java y procesar XML (_System **z** **A**pplication **A**ssist **P**rocessor_), para hacer operaciones critográficas (_CryptoExpress_), etc.

Además, como mínimo estos ordenadores tienen 64GB de RAM y, como máximo, 1TB.

En cuanto al precio, el [IBM System z9](https://en.wikipedia.org/wiki/IBM_System_z9#Pricing) cuesta $100.000.

### DELL PowerEdge
El [DELL PowerEdge](http://www.dell.com/es/empresas/p/poweredge-r230/pd?oc=per2302&model_id=poweredge-r230) tiene las siguientes características:

    * Procesador Intel Xeon E3-1200 v5 3.0GHz con 8M de cache, 4 cores y 8 threads (procesador de propósito general).
    * 8 GB de RAM

Su precio es de 1144€. 

Para poder llegar a los 64 GB de RAM que tiene el _mainframe_ de IBM necesitaríamos 8 ordenadores de este tipo, lo que nos costaría 9152€. Con 8 servidores _DELL PowerEdge_ tendríamos 8 procesadores de propósito general y 64 GB de RAM, más o menos lo mismo que el _mainframe_ de IBM pero 10 veces más barato.

---

__2. Buscar información sobre precio y características de balanceadores hardware específicos. Compara las prestaciones que ofrecen unos y otros.__

En la página de [__Barracuda__](https://www.barracuda.com/products/loadbalancer/models/compare/1?models=240,540,642,842) podemos seleccionar un máximo de cuatro balanceadores de carga para comparar entre sí, aunque no enseñan el precio.

