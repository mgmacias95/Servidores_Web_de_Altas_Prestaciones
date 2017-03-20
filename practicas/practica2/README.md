# Práctica 2: Clonar la información de un sitio web
### Marta Gómez y Braulio Vargas

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