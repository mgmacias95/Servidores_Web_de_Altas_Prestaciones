# Tema 3 - La red de una granja web

__1. Buscar con qué órdenes de terminal o herramientas gráficas podemos configurar bajo Windows y bajo Linux el enrutamiento del tráfico de un servidor para pasar tráfico de una subred a otra.__

### Windows

Windows Server proporciona una herramienta gráfica capaz de añadir a nuestro servidor la funcionalidad para realizar un NAT y poder enrutar el tráfico de una subred a otra. En la [documentación oficial](https://technet.microsoft.com/en-us/library/cc770798(v=ws.10).aspx) se explica de forma muy breve cómo crear paso a paso una configuración NAT en nuestro servidor, y enrutar el tráfico a una máquina u otra gracias a la herramienta ___Server Manager___ de Windows Server.

Pero para un mayor detalle y una explicación más clara, podemos ir a la documentación de [Dell](http://www.dell.com/support/article/us/en/19/HOW10169/configuring-windows-server-2012-r2-as-a-router?lang=EN), que va más paso a paso que la documentación oficial y añade capturas de pantalla que facilitan mucho el trabajo.

Esta herramienta nos permite definir qué servidor realizará el NAT, configurar a qué interfaz de red está conectado el servidor, configurar los DNS y el DHCP, incluso teniéndolo separado del RRAS.

### Linux

Para enrutar el tráfico en Linux, podemos usar `route` para crear nuestra NAT y poder redirigir el tráfico en nuestra máquina. En este [enlace](http://linux-ip.net/html/tools-ip-route.html) podemos encontrar una gran cantidad de comandos muy bien explicados sobre cómo usar todas las opciones posibles de `route` junto con ejemplos. Los más importantes son:

Nos permite ver la tabla principal de direcciones:

```bash
$ route -n
```
Ver la tabla local de enrutamiento:

```bash
$ ip route show table local
```
Añadir una dirección a la tabla de direccionamiento:

```bash
$ ip route add 10.38.0.0/16 via 192.168.100.1
```

Añadir una dirección de direccionamiento por defecto:

```bash
$ ip route add 10.38.0.0/16 via 192.168.100.1
```

Cear una NAT para una red entera:

```bash
$ ip route add nat 205.254.211.32/29 via 192.168.100.32
```
__2. Buscar con qué órdenes de terminal o herramientas gráficas podemos configurar bajo Windows y bajo Linux el filtrado y bloqueo de paquetes.__

### Windows

En _Windows Server_ disponemos de una herramienta nativa para el filtrado de paquetes. En la [documentación oficial](https://technet.microsoft.com/en-us/library/cc732746(v=ws.10).aspx) encontramos información básica sobre cómo utilizarla. Nos permite añadir reglas para poder realizar el filtrado:

* Permitir todo el tráfico menos el que las reglas de filtrado definen.
* Restringir todo el tráfico menos el que las reglas de filtrado definen.

Además, podemos definir el filtrado para distintos protocolos como TCP (SMTP, HTTP, DHCP, SSH, POP3...), UDP (DNS, NAT...) o IPSec. Tal y como explican en [Windows IT Pro](http://windowsitpro.com/security/packet-filtering-and-windows) el filtrado de paquetes TCP/IP tiene sus limitaciones pero es muy eficiente. En cambio, el filtrado de paquetes con IPsec ofrece una mayor flexibilidad pero es más difícil de configurar y tiene un redimiento menor.

En [Windows IT Pro](http://windowsitpro.com/security/packet-filtering-and-windows) explican también que, aunque hay _Firewalls_ y herramientas hechas por terceros, están más pensadas para un uso doméstico que para su uso en un servidor.

### Linux

La herramienta para bloqueo de paquetes y enrutamiento más usada en Linux es `iptables`. Debido a su gran popularidad, hay un montón de tutoriales en internet sobre su uso. En _DigitalOcean_ disponemos de uno donde [se explica su arquitectura y funcionamiento](https://www.digitalocean.com/community/tutorials/a-deep-dive-into-iptables-and-netfilter-architecture) y otro donde dan [indicaciones para bloquear y filtrar paquetes de entrada en CentOS6](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-basic-iptables-firewall-on-centos-6) y [también para Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-using-iptables-on-ubuntu-14-04).

Para consultar las reglas que tenemos actualmente definidas:

```bash
$ sudo iptables -L
```

Y para consultar las reglas definidas con un formato diferente al anterior:

```bash
$ sudo iptables -S
```

Para borrar todas las reglas que tenemos definidas:

```
$ sudo iptables -F
```

Para aceptar conexiones al puerto 80:

```bash
$ sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```

La opción `-A` indica que queremos añadir una nueva regla. En el caso de `iptables` esta regla puede ser tanto de entrada como de salida. La opción `-p tcp` comprueba que los paquetes que se reciben son TCP. Por último, podemos tanto aceptar como bloquear paquetes.
