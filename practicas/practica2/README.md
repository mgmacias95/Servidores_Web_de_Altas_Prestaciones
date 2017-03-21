# Práctica 2: Clonar la información de un sitio web
### Marta Gómez y Braulio Vargas

## Copiando archivos por SSH
Para copiar archivos entre un servidor y otro podemos usar SSH de la siguiente forma:

```bash
$ tar czf - directorio_tonto/ | ssh alum2@192.168.0.204 'cat > ~/tar.tgz'
```

Así, comprimiremos el contenido del directorio `directorio_tonto` y enviaremos el archivo comprimido a nuestro segundo servidor. Ahora bien, esto puede resultar algo rudimentario por lo que es mejor usar alternativas como `rsync`

![copyssh](copyssh.png)

## Instalar la herramienta `rsync`

Para instalar la herramienta, tenemos que ejecutar la orden en nuestra máquina:

```bash

$ sudo apt install rsync
```

Una vez instalada la herramienta `rsync`, podemos hacer una comprobación rápida de que se ha instalado correctamente comprobando la versión de rsync, como se ve en la siguiente imagen:

![rsync-install](1.png)

Una vez comprobado que se ha instalado correctamente, para poder copiar el directorio _/var/www/_ de la máquina principal a la máquina secundaria, tenemos que ejecutar el siguiente comando en nuestra **máquina secundaria**:

```bash
$ rsync -avz -e ssh alum@192.168.1.136:/var/www/ /var/www/
```

Con esto, `rsync` realizará una copia del directorio de la máquina principal a la máquina secundaria por medio de `ssh`. Esto se especifica usando el parámetro `-e` y la dirección IP de la máquina principal. En la siguiente imagen podemos ver el resultado:

![rsync-copy](2.png)

Si quisiéramos excluir ciertos directorios de nuestra copia de seguridad podemos usar el parámetro `--exclude`. Si queremos que al borrar un archivo en un servidor se borre también en el otro, podemos usar el parámetro `--delete`:

```bash
$ rsync -avz --delete --exclude=**/stats --exclude=**/error --exclude=**/files/pictures -e ssh alum@192.168.0.203:/var/www/ /var/www/
```

![rsync-param](3.png)

Por último, para comprobar que la sincronización ha funcionado, probamos a listar el directorio `/var/www/html` en ambas máquinas:

![syncdone](syncdone.png)

## Acceder a SSH sin contraseña

Para poder acceder por SSH de una máquina a otra, lo primero es generar un par de claves RSA para la comunicació por SSH. Para ello, ejecutamos el comando:

```bash
ssh-keygen -b 4096 -t rsa
```

Que nos dará una salida por pantalla tal y como la que podemos ver a continuación:

![rsa](6.png)

Tras esto, tenemos que copiar la clave pública a la máquina principal. Para ello ejecutamos:

```bash
$ ssh-copy-id alum@192.168.0.203
```
![rsa2](7.png)

Y por último, probamos que se ha realizado la copia correctamente conectándonos a la máquina principal por SSH.
  
![ssh-publickey](4.png)

## Actualizar el contenido de _/var/www/_ con `crontab`.

Para realizar esta tarea, se ha modificado el fichero que se encuentra en _/etc/crontab_ de la máquina secundaria. Para ello, ejecutamos la siguiente línea en el terminal:

```bash
sudo nano /etc/crontab
```

Una vez dentro, insertamos la siguiente línea en nuestro fichero _crontab_:

```
0 */3 * * * root rsync -avz -e ssh alum@192.168.0.203:/var/www/ /var/www/
```

Con el patrón `0 */3 * * *` indicamos que se ejecute la orden en el minuto 0 cada tres horas. Existe la página https://crontab.guru/ que nos permite saber si estamos poniendo bien el patrón, y ver cuándo se ejecutará por primera vez instrucción que introduzcamos en el fichero crontab.

En la siguiente imagen podemos ver cómo quedaría el fichero crontab.

![crontab](5.png)
