# Tema 5 - Medir prestaciones

__1. Buscar información sobre cómo calcular el número de conexiones por segundo. Para empezar, podéis revisr las siguientes webs  http://bit.ly/1ye4yHz y http://bit.ly/1PkZbLJ__.

En el caso de `nginx` esto es muy fácil de hacer ya que trae un módulo que se encarga de realizar estadísticas sobre las conexiones a nuestra máquina.

Para ello, tendremos que añadir a nuestro fichero de configuración `nginx.conf` lo siguiente:

```
location /nginx_status {
	# Turn on stats
	stub_status on;
	access_log   off;
	# only allow access from 192.168.1.5 #
	allow 192.168.1.5;
	deny all;
}
```

Tras esto, reiniciamos el servicio y accedemos a la siguiente url: `http://direccion_ip_del_sitio/nginx_status` y nos indicará el número de conexiones abiertas, el número de conexiones aceptadas, las que ha manejado y las conexiones que está manejando.

En caso de que nuestro sitio no utilice `nginx`, siempre estará a nuestra mano la herramienta `netstat`. Con `netstat` podemos obtener todas las conexiones que se realicen por http, al puerto 80, etc. Combinando la orden con un cauce y la herramienta `grep`.

```bash
# Para obtener todas las conexiones http
$ netstat | grep -c http | wc -l 
# Obtener todas las conexiones activas al servidor
$ netstat -na
# Obtener todas las conexiones activas al puerto 80
# y además ordenadas
$ netstat | grep :80 | sort
```

Apache también ofrece un módulo llamado `mod_status` que nos ofrece estadísticas sobre el servidor. Para activarlo, añadimos al `httpd.conf` lo siguiente:

```
<Location /server-status>
SetHandler server-status

Order Deny,Allow
Deny from all
Allow from .foo.com
</Location>
```

__2. Revisar los análisis de tráfico que se ofrecen en:__ http://bit.ly/1g0dkKj.
__Instalar wireshark y observar cómo fluye el tráfico de red en uno de los servidores web mientras se le hacen peticiones HTTP.__

__3. Buscar información sobre características, disponibilidad para diversos SO, etc de herramientas para monitorizar las prestaciones de un servidor.__
__Para empezar, podemos comenzar utilizando las clásicas de Linux:__
	* `top`.
	* `vmstat`.
	* `netstat`.