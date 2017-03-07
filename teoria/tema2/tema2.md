# Tema 2 - Alta disponibilidad y escalabilidad

__1. Calcular la disponibilidad del sistema descrito en edgeblog.net si en cada subsistema tenemos en total 3 elementos.__

Hemos hecho un [script](https://github.com/mgmacias95/Servidores_Web_de_Altas_Prestaciones/blob/master/teoria/tema2/ej1.py) que lo calcula automáticamente.

| Component   |   Availability |   Availability2 |   Availability3 |
|:------------|---------------:|----------------:|----------------:|
| Web         |         0.85   |        0.9775   |        0.996625 |
| Application |         0.9    |        0.99     |        0.999    |
| Database    |         0.999  |        0.999999 |        1        |
| DNS         |         0.98   |        0.9996   |        0.999992 |
| Firewall    |         0.85   |        0.9775   |        0.996625 |
| Switch      |         0.99   |        0.9999   |        0.999999 |
| Datacenter  |         0.9999 |        0.9999   |        0.9999   |
| ISP         |         0.95   |        0.9975   |        0.999875 |

__2. Buscar frameworks y librerías para diferentes lenguajes que permitan hacer aplicaciones altamente disponibles con relativa facilidad. Como ejemplo, examina PM2: https://github.com/Unitech/pm2 que sirve para administrar clústeres de NodeJS.__

* [__Forever__](https://github.com/hefangshi/forever-cluster): `forever` es una utilidad de _Node.js_ para línea de comandos que asegura que una aplicación se ejecute de manera continua. También permite monitorizar la aplicación usando `forever-monitor`. Tiene una funcionalidad mucho más reducida que `pm2` y, por tanto, es menos popular.

* [__Pacemaker__](https://github.com/ClusterLabs/pacemaker): al igual que `pm2`, `pacemaker` es un CRM que nos da alta disponibilidad y escalabilidad. En [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-create-a-high-availability-setup-with-corosync-pacemaker-and-floating-ips-on-ubuntu-14-04) hay documentación disponible para crear, usándolo junto a `corosync`, una aplicación con alta disponibilidad.

* [__Keepalived__](http://www.keepalived.org/): software de enrutamiento. Su principal objetivo es proporcionar un sistema robusto y simple para _balanceo de carga_ y _alta disponibilidad_ a sistemas Linux. Al igual que con `pacemaker`, [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-set-up-highly-available-web-servers-with-keepalived-and-floating-ips-on-ubuntu-14-04) tiene documentación sobre cómo configurar un servicio con alta disponibilidad usando `keepalived`.


__3. ¿Cómo analizar el nivel de carga de cada uno de los subsistemas en el servidor? Buscar herramientas y aprender a usarlas.__



__4. Buscar diferentes tipos de productos:__

* __Buscar ejemplos de balanceadores software y hardware (productos comerciales).__
* __Buscar productos comerciales para servidores de aplicaciones.__
* __Buscar productos comerciales para servidores de almacenamiento.__