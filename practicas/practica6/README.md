# Práctica 6 - Discos en RAID

## Añadiendo discos virtuales

![](1.png)

Para añadir un disco virtual a una máquina virtual (_VirtualBox_), sólo hay que entrar en la configuración de la máquina y, en la pestaña de almacenamiento, hacer click en el botón señalado en azul. Esto nos abrirá un asistente que creará el disco virtual con el nombre y tamaño que digamos.

## Configuración del RAID por software
En primer lugar, debemos tener el paquete `mdadm` instalado.

![](2.png)

Una vez instalado el paquete `mdadm`, debemos crear el RAID. Para ello, necesitamos saber la identificación asignada a los dos nuevos discos. Dicha identificación podemos obtenerla con el comando `sudo fdisk -l`:

![](3.png)

En este caso, los identificadores asignados han sido __/dev/sdb__ y __/dev/sdc__.

Y ahora sí, creamos el RAID usando el dispositivo `/dev/md0`:

![](4.png)

Una vez creado, le damos formato ext2, que es el que da `mkfs` por defecto:

![](5.png)

A continuación, creamos el directorio en el que se montará el RAID y lo montamos:

![](6.png)

Como se aprecia, ha sido montado correctamente.

Por último, comprobamos el estado del RAID:

![](7.png)

Tal y como hemos hecho, el RAID tiene dos discos y ambos están funcionando correctamente.

## Automatizar el montaje del RAID al arrancar
Para no tener que montar el disco cada vez que arranquemos el sistema, debemos automatizar dicha tarea __añadiéndolo al fstab__.

Para ello, en primer lugar debemos obtener el _UUID_ del disco:

![](8.png)

Una vez obtenido, lo añadimos a la última línea del fichero `/etc/fstab`:

![](9.png)

Para comprobar que el proceso ha ido correctamente, reiniciamos el sistema y ejecutamos `sudo mount`:

![](10.png)

El disco se ha montado automáticamente, pero ahora con el nombre `/dev/md127`.
