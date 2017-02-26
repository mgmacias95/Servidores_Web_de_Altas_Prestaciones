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
