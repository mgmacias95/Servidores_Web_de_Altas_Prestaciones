# Práctica 4: Asegurar la granja web


## Instalar un certificado SSL autofirmado para configurar el acceso por HTTPS

Para generar nuestro certificado SSL, ejecutaremos el comando `a2enmod ssl` y pasarán a activarse una serie de módulos en nuestra máquina. Una vez finalizada la ejecución del comando, tendremos que reiniciar el servicio de `apache2` y crear la carpeta `ssl` en el directorio de Apache donde almacenaremos nuestro certificado SSL.

Una vez hecho esto, generamos nuestro certificado SSL introduciendo la siguiente orden en nuestro terminal:

```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout 
  /etc/apache2/ssl/apache.key -out /etc/apache2/ssl/apache.crt
```

Esto generará las claves y nos pedirá cierta información para la creación del certificado, como se puede ver en la siguiente imagen.

![](enable_ssl.png)

A continuación, tendremos que pasar a editar el archivo de configuración de nuestro servidor para añadir nuestro certificado e indicar que el sitio utiliza un certificado SSL. Para ello, usaremos el siguiente comando `sudo nano /etc/apache2/sites-avilable/default-ssl`, y añadimos las líneas:
```
SSLCertificateFile /etc/apache2/ssl/apache.crt
SSLCertificateKeyFile /etc/apache2/ssl/apache.key
```
tal y como se ve en la siguiente imagen.

![](default-ssl-conf.png)

Una vez hecho esto, tenemos que activar el `default-ssl` con `a2ensite default-ssl` y reiniciar el servicio. 

![](activate_ssl.png)

Para comprobar que funciona, accederemos a nuestro sitio web y veremos que el certificado está activo, pero como no está firmado por ninguna entidad de confianza sino que es autofirmado, Firefox nos dirá que el sitio no es seguro, como se ve en la siguiente imagen:

![](self-signed.png)

