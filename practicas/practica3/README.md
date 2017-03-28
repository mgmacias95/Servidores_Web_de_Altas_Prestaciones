# Práctica 3: Balanceo de Carga

### Marta Gómez y Braulio Vargas

## Configurando un Balanceador de Carga con nginx

## Configurando un Balanceador de Carga con haproxy
Para instalar `haproxy` ejecutamos

```bash
$ sudo apt install haproxy
```

Una vez instalado, debemos indicarle las IPs de las dos máquinas servidoras. Para ello, modificamos el fichero `/etc/haproxy/haproxy.cfg` añadiendo a la configuración de `haproxy` lo siguiente:

```
global
    maxconn 256

frontend http-in
    bind *:80
    default_backend servers

backend servers
    server  m1 192.168.0.204 maxconn 32
    server  m2 192.168.0.203 maxconn 32
```

### Probando que el balanceador funciona
Para probar que el balanceador funciona, cambiamos ligeramente la página de prueba de cada una de las máquinas de forma que se pueda diferenciar cuando accedemos a una u a otra.

Después, lanzamos `haproxy` con el siguiente comando:

```bash
$ sudo /usr/sbin/haproxy -f /etc/haproxy/haproxy.cfg
```

Si accedemos desde nuestro navegador a la URL del balanceador (`192.168.0.207`) iremos intercalando entre las páginas de prueba de cada servidor:

![haproxy_m1](haproxy_m1.png)
![haproxy_m2](haproxy_m2.png)

