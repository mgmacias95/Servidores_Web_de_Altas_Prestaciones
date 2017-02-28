# Tema 1 - Introducción

__1. Buscar información sobre las tareas o servicios web para los que se usan más los siguientes programas__: 

* __apache__
* __nginx__
* __thttpd__
* __Cherokee__
* __node.js__

## Apache
[Apache](http://httpd.apache.org/) es un servidor HTTP (`httpd`) para __alojar servicios y páginas web__ desarrollado por la [Apache Software Foundation](http://www.apache.org/) desde 1995. Debido a su gran popularidad, dispone de una buena documentación,además, es extensible mediante módulos y puede procesar un gran número de lenguajes interpretados sin recurrir a software externo.

## Nginx
[Nginx](https://www.nginx.com/) es un servidor que soporta aplicaciones HTTP, TCP y UDP. Al igual que _Apache_ es un también un servidor web. Fue desarrollado para soportar una gran carga de peticiones, algo muy reclado en la web actual. 

### Apache vs Nginx
En [DigitalOcean](https://www.digitalocean.com/community/tutorials/apache-vs-nginx-practical-considerations) explican las diferencias que se deben tener en cuenta la hora de escoger entre uno y otro.

- __Manejo de Conexiones__: `apache` dispone de varios módulos para poder manejar las distintas conexiones debido a la evolución que ha tenido desde 1995. En cambio, `nginx` está diseñado desde el primer día para manejar miles de conexiones en cada una de las hebras y hacer que el uso de CPU y memoria tienda a ser prácticamente constante.

- __Contenido dinámico__: `apache` dispone de módulos para poder procesar contenido dinámico dentro del propio servidor sin tener que depender de componentes externos. `nginx`, al contrario, debe depender pasar la petición de contenido dinámico a un procesador externo y esperar la respuesta del mismo con el contenido ya renderizado.

- __Configuración Distribuida vs Centralizada__: `apache` utiliza los ficheros `.htaccess` para proporcionar acceso y permisos a los usuarios de nuestro sistema a determinados directorios del sistema. Además, esto permite una configuración descentralizada del servidor. `nginx` por su parte, no usa esta configuración y, aunque perdemos flexibilidad, ganamos rendimiento. Además, también ganamos en seguridad ya que no damos acceso a los usuarios a determinados permisos del sistema.

- __Fichero vs URI__: `apache` interpreta una petición como un recurso físico en el sistema. Por otro lado, al estar diseñado tanto para servidor web como para servidor proxy `nginx` trabaja principalmente con URIs.

- __Módulos__: `apache` permite cargar y descargar de forma dinámica módulos mientras el servidor está ejecutándose. En cambio, en `nginx` los módulos no se pueden cargar de forma dinámica, lo que hace que `nginx` sea mucho menos flexible.

## thttpd

[thttpd](http://www.acme.com/software/thttpd/) es un servidor web libre desarrollado por [ACME Laboratories](http://acme.com/), compatible con la mayoría de sistemas _Unix_, que tiene como principales características:

- __Simple__: solo utiliza lo mínimo posible para poder usar el protocolo HTTP.
- __Ligero__: el número de archivos que necesita es muy reducido, con tamaños pequeños para estos ficheros y el ejecutable, poco uso de memoria durante la ejecución, etc. Para más información, podemos consultar este [enlace](http://www.acme.com/software/thttpd/benchmarks.html).
- __Multiplataforma__: como se ha dicho antes, es posible ejecutarlo en una gran variedad de sistemas basados en Unix.
- __Rápido__: ante un alto nivel de carga, responde mucho más rápido que otros sistemas.
- __Seguridad__: desde ACME Labs., hacen todo lo posible para mantener la seguridad, frente a ataques al servidor, mejorando la seguridad de la herramienta.

## Cherokee

Es una herramienta que nos permite configurar fácilmente un servidor web, que nos permite instalar una gran cantidad de servicios, poder crear infraestructuras virtuales, soporta muchas herramientas web (FastCGI, SCGI, PHP, uWSGI, SSI, etc.), SSL/TLS, etc. También ofrece una interfaz gráfica para poder configurar el servidor web y poder ejecutar aplicaciones en Django, Ruby On Rails, videostreaming, etc.

## Node.js

[Node.js](https://nodejs.org/en/about/) es un entorno _Javascript_ asíncrono orientado a eventos. Esto quiere decir que el servidor sólo reaccionará cuando un evento ocurra. Está diseñado para construir aplicaciones escalables y con requisitos de tiempo real, puede manejar múltiples conexiones a la vez. 

Otros servidores usan hebras del sistema operativo, lo cual es muy ineficiente y difícil de usar. Además, prácticamente ninguna función de Node.js ejecuta I/O por lo que los procesos no se bloquean, esto permite hacer sistemas escalables. Para más información consultar la [documentación](https://nodejs.org/en/docs/guides/blocking-vs-non-blocking/).

Además, Node.js funciona en Javascript, lo que nos permite usar el mismo lenguaje de programación tanto en el _frontend_ como en el _backend_.
