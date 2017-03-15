# Tema 3 - La red de una granja web

__1. Buscar con qué órdenes de terminal o herramientas gráficas podemos configurar bajo Windows y bajo Linux el enrutamiento del tráfico de un servidor para pasar tráfico de una subred a otra.__

__2. Buscar con qué órdenes de terminal o herramientas gráficas podemos configurar bajo Windows y bajo Linux el filtrado y bloqueo de paquetes.__

### Windows

En _Windows Server_ disponemos de una herramienta nativa para el filtrado de paquetes. En la [documentación oficial](https://technet.microsoft.com/en-us/library/cc732746(v=ws.10).aspx) encontramos información básica sobre cómo utilizarla. Nos permite añadir reglas para poder realizar el filtrado:

* Permitir todo el tráfico menos el que las reglas de filtrado definen.
* Restringir todo el tráfico menos el que las reglas de filtrado definen.

Además, podemos definir el filtrado para distintos protocolos como TCP (SMTP, HTTP, DHCP, SSH, POP3...), UDP (DNS, NAT...) o IPSec. Tal y como explican en [Windows IT Pro](http://windowsitpro.com/security/packet-filtering-and-windows) el filtrado de paquetes TCP/IP tiene sus limitaciones pero es muy eficiente. En cambio, el filtrado de paquetes con IPsec ofrece una mayor flexibilidad pero es más difícil de configurar y tiene un redimiento menor.

En [Windows IT Pro](http://windowsitpro.com/security/packet-filtering-and-windows) explican también que, aunque hay _Firewalls_ y herramientas hechas por terceros, están más pensadas para un uso doméstico que para su uso en un servidor.

