# Tema 2 - Alta disponibilidad y escalabilidad

__1. Calcular la disponibilidad del sistema descrito en edgeblog.net si en cada subsistema tenemos en total 3 elementos.__

Hemos hecho un [script](https://github.com/mgmacias95/Servidores_Web_de_Altas_Prestaciones/blob/master/teoria/tema2/ej1.py) que lo calcula automáticamente.

| Component   |   Availability |   Availability2 |   Availability3 |
|:------------|---------------:|----------------:|----------------:|
| Web         |    0.850000000 |     0.977500000 |     0.996625000 |
| Application |    0.900000000 |     0.990000000 |     0.999000000 |
| Database    |    0.999000000 |     0.999999000 |     0.999999999 |
| DNS         |    0.980000000 |     0.999600000 |     0.999992000 |
| Firewall    |    0.850000000 |     0.977500000 |     0.996625000 |
| Switch      |    0.990000000 |     0.999900000 |     0.999999000 |
| Datacenter  |    0.999900000 |     0.999900000 |     0.999900000 |
| ISP         |    0.950000000 |     0.997500000 |     0.999875000 |

__2. Buscar frameworks y librerías para diferentes lenguajes que permitan hacer aplicaciones altamente disponibles con relativa facilidad. Como ejemplo, examina PM2: https://github.com/Unitech/pm2 que sirve para administrar clústeres de NodeJS.__

* [__Forever__](https://github.com/hefangshi/forever-cluster): `forever` es una utilidad de _Node.js_ para línea de comandos que asegura que una aplicación se ejecute de manera continua. También permite monitorizar la aplicación usando `forever-monitor`. Tiene una funcionalidad mucho más reducida que `pm2` y, por tanto, es menos popular.

* [__Pacemaker__](https://github.com/ClusterLabs/pacemaker): al igual que `pm2`, `pacemaker` es un CRM que nos da alta disponibilidad y escalabilidad. En [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-create-a-high-availability-setup-with-corosync-pacemaker-and-floating-ips-on-ubuntu-14-04) hay documentación disponible para crear, usándolo junto a `corosync`, una aplicación con alta disponibilidad.

* [__Keepalived__](http://www.keepalived.org/): software de enrutamiento. Su principal objetivo es proporcionar un sistema robusto y simple para _balanceo de carga_ y _alta disponibilidad_ a sistemas Linux. Al igual que con `pacemaker`, [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-set-up-highly-available-web-servers-with-keepalived-and-floating-ips-on-ubuntu-14-04) tiene documentación sobre cómo configurar un servicio con alta disponibilidad usando `keepalived`.


__3. ¿Cómo analizar el nivel de carga de cada uno de los subsistemas en el servidor? Buscar herramientas y aprender a usarlas.__

Usando una herramienta que monitorice cada servicio por separado. Algunos ejemplos de herramientas que permiten esto de forma sencilla son:

* [__Munin__](munin-monitoring.org): presenta gráficos de carga de distintos servicios y componentes de un servidor. Podemos ver la información que ofrece en su [live demo](http://demo.munin-monitoring.org/munin-monitoring.org/buildd.munin-monitoring.org/).

* [__Inciga__](https://www.icinga.com/): proporciona una interfaz gráfica para realizar tareas de monitorización y, además, tiene un histórico de problemas, notificaciones, problemas de servicios/aplicaciones y es extendible. Nació como un _fork_ de _Nagios_.

* [__Cacti__](http://www.cacti.net/): interfaz PHP para [RRDtool](http://oss.oetiker.ch/rrdtool/). Permite hacer gráficos sobre distintas métricas tales como tráfico, uso de un determinado recurso... De hecho, en la documentación de _RRDtool_ explican que podemos hacer gráficos de cualquier conjunto de datos que queramos: _RRDtool_ nos ayuda a crear una base de datos y crear gráficos en PNG de los mismos.

__4. Buscar diferentes tipos de productos:__

* __Buscar ejemplos de balanceadores software y hardware (productos comerciales).__
* __Buscar productos comerciales para servidores de aplicaciones.__
* __Buscar productos comerciales para servidores de almacenamiento.__

- Balanceadores de carga software:
  - __[Enterprise VA MAX](https://www.loadbalancer.org/products/virtual/enterprise-va-max)__: balanceador de carga software de la empresa _loadbalencer.org_. Ofrece un balanceador de carga software, con capacidad para una alta escalabilidad del sistema, a cambio de una licencia de pago.
  - __[nginx](http://nginx.org/en/docs/http/load_balancing.html)__: nginx también permite actuar como un balanceador de carga HTTP. 
  - __[Pound](http://www.apsis.ch/pound)__: Pound es otro balanceador de carga software capaz de balancear una gran cantidad de nodos ante peticiones HTTP. Es gratuito y con licencia GPT. 
  - __[Pen](http://siag.nu/pen/)__: es un balanceador de carga capaz de manejar peticiones DNS, HTTP o SMTP, además de tener una alta disponibilidad, alta escalabilidad y robustez. También se puede instalar en una gran cantidad de sistemas Linux, como en Windows. 
+ Balanceadores de carga hardware:
