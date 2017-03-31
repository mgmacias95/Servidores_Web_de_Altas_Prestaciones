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

En la página de [__Barracuda__](https://www.barracuda.com/products/loadbalancer/models/compare/1?models=240,540,642,842) podemos seleccionar un máximo de cuatro balanceadores de carga para comparar entre sí, aunque no enseñan el precio (cuando haces click en _Purchase_ sale un mensaje diciendo que no aceptan pedidos fuera de EEUU). Aún así, podemos hacer un pequeño análisis de los modelos que se están comparando:

El peor de todos, sin duda, es el modelo 240, ya que acepta muy pocos ordenadores (10) y no tiene mecanismos de seguridad incorporados como SSL o protección contra ataques DDoS. El resto de modelos comparados (520, 642 y 842) tienen las mismas características de seguridad y la diferencia entre ellos es el tráfico (_throughput_) máximo que aceptan y el número de servidores que soportan. También es verdad que hay más modelos, pero el comparador de Barracuda sólo acepta 4 modelos para comparar como máximo. 

Para una empresa pequeña, el ideal sería el 540 ya que incorpora mecanismos de seguridad. El modelo intermedio entre el 240 y el 540 (el modelo 440) no incorpora mecanismos de seguridad contra ataques DDoS y, por tanto, no sería una buena opción aunque fuese algo más económico.

Aunque en la página de Barracuda no aparece el precio, en [__Enter Computers__](http://www.entercomputers.com/networking/network-appliance-devices-1164/load-balancers.html) venden el modelo 440 por unos $5.500. Esto nos sirve para hacernos una idea del precio del resto de balanceadores de carga.

---

__3. Buscar información sobre los métodos de balaceo que implementan los dispositivos recogidos en el ejercicio 4.2__

Para encontrar información sobre los distintos métodos de balanceo de carga que imeplementan los dispositivos de _Barracuda_, tenemos que consultar la [hoja de especificaciones](https://assets.barracuda.com/assets/docs/dms/Barracuda_Load_Balancer_ADC_DS_ES.pdf). En la segunda página podemos ver una sección llamada _Balanceo de Carga_ en el que enumera los distintos métodos disponibles en sus balanceadores:

* Round-robin
* Round-robin ponderado
* Servidor con menos conexiones
* Adaptado por carga de CPU

Y en el caso de que queramos implementar balanceo de carga global, también nos permite balancear por IP y hacer _health check_ entre distintos servidores.

---

__4. Instala y configura en máquina virtual el balanceador *ZenLoadBalancer*__

---

__5. Probar los diferentes métodos de redirección HTTP. ¿Cuál es más adecuado y cuál no para hacer balanceo de carga global? ¿Por qué?__

---

__6. Buscar información sobre los bloques de IP para los distintos países y continentes. Implementar en Javascript o PHP la detección de zona desde donde se conecta un usuario.__

---

__7. Buscar información sobre distintos métodos y herramientas para implementar GSLB.__

