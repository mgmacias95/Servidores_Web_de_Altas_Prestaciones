# Tema 2 - Alta disponibilidad y escalabilidad

__1. Calcular la disponibilidad del sistema descrito en edgeblog.net si en cada subsistema tenemos en total 3 elementos.__

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

* [__supervisord__](http://supervisord.org/introduction.html): supervisor universal para servidores hecho en Python.

* [__uWSGI__](https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/uwsgi/): para Django y Apache.

* [__Forever__](https://github.com/hefangshi/forever-cluster): `forever` es una utilidad de _Node.js_ para línea de comandos que asegura que una aplicación se ejecute de manera continua. También permite monitorizar la aplicación usando `forever-monitor`. Tiene una funcionalidad mucho más reducida que `pm2` y, por tanto, es menos popular.

__3. ¿Cómo analizar el nivel de carga de cada uno de los subsistemas en el servidor? Buscar herramientas y aprender a usarlas.__



__4. Buscar diferentes tipos de productos:__

* __Buscar ejemplos de balanceadores software y hardware (productos comerciales).__
* __Buscar productos comerciales para servidores de aplicaciones. (3) Buscar productos comerciales para servidores de almacenamiento.__