# Tema 7 - Almacenamiento de datos

__1. ¿Qué tamaño de unidad RAID se obtendrá al configurar un *RAID 0* a partir de dos discos de 100GB y 100GB?__

__¿Qué tamaño de unidad RAID se obtendrá al configurar un *RAID 0* a partir de tres discos de 200GB cada uno?__

Al configurar un [RAID 0](https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_0) con dos discos de igual capacidad, el tamaño total será la suma de la capacidad de ambos. 200 y 600GB respectivamente en los casos del enunciado. 

Ahora bien, si hacemos un RAID 0 con discos de diferente tamaño, el tamaño total del RAID será el tamaño del disco más pequeño multiplicado por el número de discos.

---

__2. ¿Qué tamaño de unidad RAID se obtendrá al configurar un *RAID 1* a partir de dos discos de 100GB y 100GB?__

__¿Qué tamaño de unidad RAID se obtendrá al configurar un *RAID 1* a partir de tres discos de 200GB cada uno?__

En el caso del [RAID 1](https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_1), como su objetivo es clonar archivos en ambos discos duros de forma que si uno deja de funcionar los datos seguirán ahí, si hacemos un RAID 1 a partir de dos o más discos del mismo tamaño, el tamaño del RAID será igual al tamaño de los discos. 100 y 200GB respectivamente en los casos del enunciado.

---

__4. Buscar información sobre los sistemas de ficheros en red más utilizados en la actualidad y comparar sus características. Hacer una lista de ventajas e inconvenientes de todos ellos, así como grandes sistemas en los que se utilicen.__

* [__NFS__](http://web.mit.edu/rhel-doc/4/RH-DOCS/rhel-rg-es-4/ch-nfs.html): Hay tres versiones: NFSv2, NFSv3, NFSv4. 

    La NFSv4 incluye seguridad Kerberos, trabaja con cortafuegos, permite ACLs y utliza operaciones con descripción de estado. Todas las versiones utilizan TCP aunque la NFSv2 y la NFSv3 pueden utilizar también UDP. La desventaja de esto es que si el servidor se cae, al ser UDP sin supervisión, los clientes seguirán saturando la red con peticiones al servidor.

* [__SMB__](https://es.wikipedia.org/wiki/Server_Message_Block): permite compartir archivos, impresoras, etc entre nodos de una red de ordenadores que usen __Windows__. Fue desarrollado por IBM y fue renombrado a __CIFS__ por Microsoft en 1998. CIFS añadió a SMB soporte para enlaces (tanto simbólicos como duros) y mayores tamaños de archivo. [__Samba__](https://es.wikipedia.org/wiki/Samba_(programa)) es una implementación libre del este protocolo que funciona en Unix.  

* [__AFS__](https://en.wikipedia.org/wiki/Andrew_File_System): es un sistema de archivos distribuido que usa un conjunto de _servidores de confianza_ para ofrecer una serie de espacios de nombres transparentes a la localización para todos los ordenadores cliente. 

    Como ventaja sobre los sistemas de archivos de red tradicionales, tiene que éste es más escalable y seguro. Usa Kerberos para la autentificación (como NFS) e implementa listas de control de acceso en directorios para usuarios y grupos. Cada cliente guarda una caché en su sistema de archivos local para incrementar la velocidad en peticiones al mismo archivo.

    Las modificaciones que se hagan a un archivo se realizarán sobre el archivo que está en caché y sólo se copiarán los cambios al servidor una vez éste haya sido cerrado. Si otro usuario modifica un archivo en caché, el servidor notifica al usuario (esto se denomina _callbacks_ y sirve para mantener la consistencia).

__Configurar en una máquina virtual un servidor NFS. Montar desde otra máquina virtual en la misma subred la carpeta exportada y comprobar que ambas pueden acceder a la misma para lectura y escritura.__

Esto ha sido ya hecho en la [práctica 6](https://github.com/mgmacias95/Servidores_Web_de_Altas_Prestaciones/tree/master/practicas/practica6)
