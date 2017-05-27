# Prácticas de Servidores Web de Altas Prestaciones

## Práctica 1
1. Configuración inicial de VirtualBox
2. Instalación de un servidor LAMP en Ubuntu Server
3. Comprobación de los servicios SSH y Apache

## Práctica 2
1. Copiar archivos por SSH.
2. Configurar `rsync` entre nuestras dos máquinas.
3. Configurar SSH para poder acceder a nuestras dos máquinas sin contraseña.
4. Configurar un demonio `crontab` para sincronizar el contenido de nuestras dos máquinas virtuales con `rsync`.

## Práctica 3
1. Instalar de `nginx` y configurarlo como balanceador de carga _Round-Robin_.
2. Configurar `nginx` como un balanceador de carga ponderado.
3. Prueba de ambas configuraciones.
4. Instalar `haproxy` y configurar el balanceador de carga.
5. Prueba del balanceador.
6. Instalar `pound` y configurar el balanceador de carga.
7. Prueba del balanceador.
8. Instalar _Apache Benchmark_ y probar el funcionamiento de los tres balanceadores ante una alta carga.

## Práctica 4
1. Istalar un certificado SSL autofirmado.
2. Configurar el cortafuegos.
3. Hacer un script que configure iptables al arrancar.
4. Crear una máquina cortafuegos que se colocará delante del balanceador de carga.

## Práctica 5
1. Creación de una base de datos e inserción de datos.
2. Replicar una base de datos con `mysqldump`.
3. Replicar una base de datos con una configuración Maestro-Esclavo.
4. Replicar una base de datos con una configuración Maestro-Maestro.

## Práctica 6
1. Añadir discos virtuales a un servidor.
2. Configurar un RAID 1 por software.
3. Automatizar el montaje del RAID al arrancar.
4. Simular un fallo en uno de los discos.
5. Realizar una configuración NFS.
