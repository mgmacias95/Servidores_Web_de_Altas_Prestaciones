# Kubernetes y computación cloud

### Marta Gómez Macías y Braulio Vargas López

# Docker y los contenedores.

Docker es un entorno virtualizado de ejecución de contenedores, agregando un sistema ligero de despliegue y una ejecución de las máquinas virtualizadas más ligera que la virtualización clásica, que lo hace muy cómodo para la computación cloud.

## Qué es un contenedor

Un contenedor es, por decirlo de una manera, una simplificación de la virtualización clásica ya que un contenedor ofrece la capacidad de ofrecernos un sistema de ficheros completo, con un sistema operativo completo, capaz de alojar cualquier librería que seamos capaces de instalar, y lo más importante, nuestra aplicación; sin la necesidad de tener un hypervisor.

![docker](https://www.docker.com/sites/default/files/what_is_a_container.png)

Además, ofrece una solución genial al problema de "esto en mi máquina funciona, no sé por qué en la tuya no", ya que el contenedor es independiente al hardware y software que haya instalado en la máquina anfitriona.

Los contenedores también tienen otras ventajas, como el que se ejecutan sobre el espacio de usuario sobre el kernel del SO, permite tener muchas instancias de esa misma máquina ejecutándose a la vez con una sobrecarga menor para la máquina que la que habría en el caso de hacerlo con máquinas virtuales.

## Imágenes docker
Las [__imágenes__](https://docs.docker.com/glossary/?term=image) son la base de los contenedores. Consisten en un sistema de archivos raíz con un determinado software instalado. Las imágenes no pueden cambiar una vez construidas. Son los [_contenedores_](https://docs.docker.com/glossary/?term=container) los que sí cambian. Un _contenedor_ es una instancia de una imagen.

Para construir una imagen se utilizan los denominados [__Dockerfiles__](https://www.digitalocean.com/community/tutorials/docker-explained-using-dockerfiles-to-automate-building-of-images). También hay [un repositorio](https://hub.docker.com/explore/) con imágenes listas para descargar.

![dockerhub](dockerhub.png)

Otra cosa destacada de las imágenes es que pueden ser descargadas ([`docker pull`](https://docs.docker.com/engine/reference/commandline/pull/)) y subidas ([`docker push`](https://docs.docker.com/engine/reference/commandline/push/)) a un repositorio remoto. También pueden tener un control de versiones y etiquetas ([`docker tag`](https://docs.docker.com/engine/reference/commandline/tag/)), como un programa fuente subido a _Github_. Podemos ver las diferencias ([`docker diff`](https://docs.docker.com/engine/reference/commandline/diff/#examples)) entre distintos contenedores para ver cómo difieren de sus imágenes base.

### Capas en un contenedor

![contenedor](https://www.docker.com/sites/default/files/Container%402x.png)

### Capas en una máquina virtual

![contenedor](https://www.docker.com/sites/default/files/VM%402x.png)

Esto ofrece muchas ventajas, tanto durante la fase de desarrollo de una aplicación como en la de producción. En la fase de desarrollo, podemos usar los contenedores como máquinas de usar y tirar, ya que en ella instalas las librerías que necesitas, tu aplicación, y puedes probarla prácticamente de manera instantánea, y en caso de que esta máquina falle y muera, es tan sencillo como "tirarla a la basura" y ejecutar una nueva.

También se puede modificar estos contenedores modificando el archivo _Dockerfile_ donde podemos definir con unas sencilla reglas, qué hará el contenedor, pudiendo definir contenedores con _Nginx_ y _php_, _Apache_, etc.

# Clústering de contenedores: Docker Swarm y Kubernetes

## Docker Swarm

![dockerswarn](https://raw.githubusercontent.com/docker/swarm/master/logo.png)

Docker Swarm es una herramienta hecha por y para hacer clústers de contenedores Docker, usando la misma API que Docker y que funciona directamente con este tipo de contenedores. Esto ofrece las ventajas de trabajar con la misma API que Docker, lo que nos permite trabajar de forma muy rápida y cómoda, ya que no hay que adaptarse a un nuevo entorno, pero, tiene las mismas desventajas que tiene Docker.

Docker y su API hay ciertas cosas que no soporta, y en caso de que la API no soporte algo, ese algo no podrá ser instalado en todo nuestro clúster.

## Kubernetes  

![kubernetes](https://raw.githubusercontent.com/kubernetes/kubernetes/master/logo/logo.png)

Como podemos encontrar en su [página web](https://kubernetes.io), Kubernetes es un sistema para el despliegue automático de aplicaciones contenerizadas, generalmente mediante Docker. Esto se conoce como el orquestador de contenedores. Además de esto, fue desarrollado por Google y escrito en _Go_. Pero, ¿por qué no usar directamente contenedores Docker? 

1.  Docker no es capaz de ver nada más allá del host que ejecuta el contenedor. 
2.  Si tenemos varios contenedores, estos no pueden ser vistos como una sola unidad.
3.  Por sí mismo, Docker no es capaz de manejar y desplegar una gran cantidad de aplicaciones.

Para eso viene al rescate Kubernetes.  Aunque antes de empezar con él, debemos entender un poco la terminología que usa:

### Kubernetes Pods y los _minions_

![minion](https://c1.staticflickr.com/3/2880/12909509855_0640e249dc_b.jpg)

Los ___Pods___ son la unidad más básica que puede desplegar Kubernetes. Un Pod encapsula un aplicación en un contenedor, capaz de almacenar recursos, tener una dirección IP única y opciones de configuración del contenedor. Estos contenedores suelen ser contenedores _Docker_. Estos contenedores con una aplicación específica, que se asignan a una máquina específica o MV se les conoce como los _Kubernetes Nodes_, antes conocidos como _minions_. Existen dos tipos de Pods:

* __Pods que ejecutan un solo contenedor__: son el caso de uso más común en Kubernetes. En este caso, se puede ver al Pod como una encapsulación del contenedor y de este modo, Kubernetes solo se tiene que encargar de gestionar los Pods.

* __Pods que ejecutan varios contenedores__: puede ser que en algún Pod necesitamos varios contenedores que estén interconectados entre sí. Un ejemplo puede ser que un contenedor actúe como servidor web y otro almacene datos en una base de datos. El Pod hará que ambos contenedores se vean como una sola unidad de trabajo y gestiona la comunicación entre ambos. Este caso es un poco más complejo, pero Kubernetes es capaz de llevarlo a cabo.

	Estos contendeores se comunican de forma interna mediante el _localhost_ y a la hora de comunicarse con el exterior, deberán compartir los recursos de red.

![pods](https://kubernetes.io/images/docs/pod.svg)

A la hora de realizar un escalado horizontal, se deben generar varios Pods por cada instancia, lo que se conoce como ___replicado___. Es aquí cuando entra en juego el ___Controlador___ o ___Controller___ que realiza una abstracción sobre los Pods replicados y los gestiona como si fueran una sola unidad.

Para más información, podemos visitar la [página oficial](https://kubernetes.io/docs/concepts/workloads/pods/pod-overview/).

### Controller

Un _Controller_ se encarga de crear y controlar varios Pods, de replicar los Pods, desplegarlos y mantener el clúster. De hecho, siguiendo la filosofía de los contenedores (usar y tirar), si un nodo muere, automáticamente el Controller lo replica y reemplaza al nodo muerto. Existen tres tipos de Controllers:

* __Deployment__: este tipo de _Controller_ se encarga de darnos la opción de declarar cómo queremos que se desplieguen nuestros pods, declarando el estado en el que queremos que estén, y este controller cambiará el estado actual al estado declarado. Más información [aquí](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

* __StatefulSets__: provee a cada Pod una identificación única y nos facilita el escalado de las aplicaciones y su despliegue. Más información [aquí](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/).

* __DaemonSets__: se encarga de gestionar de que los nodos de nuestro clúster tienen una copia de los pods que hemos creado, ya que conforme vayamos añadiendo nodos al clúster, tendremos que añadirle a estos nodos los pods necesarios. Más información en la [documentación oficial](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/).

### _kube-proxy_

_kube-proxy_ es el proxy de red de Kubernetes, que está peresente en cada uno de los nodos del clúster, y podemos configurarlo en función de los servicios que vaya a dar cada uno de los nodos. Además de esto, nos provee de un DNS para nuestro clúster, para poder asignar las IPs.

## El poder de Kubernetes

Kubernetes nos ofrece la posiblidad de manejar nuestro clúster de una forma muy cómodo, ya que automatiza una gran cantidad de tareas como son la creación de nuevas instancias para escalar nuestras aplicaciones, monitorización, la forma de desplegar nuestras aplicaciones, etc. Simplemente tenemos que declarar cómo queremos hacer estas tareas mediante ficheros _YAML_.

También nos ofrece balanceo de carga, en caso de que un contenedor falle, es capaz de tirarlo y crear uno nuevo, para seguir funcionando, se encarga de administrar nuestro almacenamiento, ya sea en local o en un servicio externo en la nube, etc.

Kubernetes, comparado con el orquestador de contenedores DockerSwarn, no está obligado a usar siempre contenedores Docker, lo que nos permite una mayor flexibilidad en nuestro trabajo que DockerSwarm, ya que podemos usar otras alternativas y no estar atados por las limitaciones de la API de Docker. Además de esto, Kubernetes se puede usar para administrar cualquier tipo de clúster, ya sea un clúster de contenedores o bien, un clúster tradicional o una composición de ambos. 

Esto en parte es lo que hace más complicada la configuración de Kubernetes. Al haber tantos escenarios posibles, realizar una configuración correcta para nuestro clúster puede ser algo más difícil que por ejemplo, DockerSwarm. Aunque, esto no tiene porque ser exactamente así, ya que existen plataformas con AWS, Google Cloud, u OpenShift, donde Kubernetes ya viene configurado y sólo nos tenemos que preocupar de desarrollar y desplegar nuestra aplicación.

# Usando OpenShift para crear y subir aplicaciones

## ¿Qué es OpenShift?
Actualmente, hay varios tipos de servicios cloud:

* [_Software as a service_](https://www.salesforce.com/saas/): en vez de ofrecer un software que tiene que ser instalado en el cliente, se ofrece una aplicación web. El cliente sólo necesita un navegador para poder usar el software. Ejemplos: correo electrónico web, calculadora online, juegos javascript, etc. 
* [_Infrastructure as a service_](http://www.fujitsu.com/us/services/infrastructure/iaas/): ofrece recursos computaciones (almacenamiento, procesamiento, redes, etc). El cliente contrata los recursos que necesita y se le ofrecen como entornos virtualizados (contenedores) en los cuales puede instalar y ejecutar el software que quiera. Ejemplos: Amazon Web Services, Digital Ocean, Google Cloud Services....
* [_Platform as a service_](https://azure.microsoft.com/en-us/overview/what-is-paas/): al igual que el IaaS, se ofrece al cliente una máquina con unas determinadas prestaciones y se paga por uso. Además de ofrecer esto, el PaaS también ofrece software y herramientas de desarrollo para que el programador sólo se preocupe del desarrollo de su aplicación y se olvide de tener que estar pagando licencias, actualizando software, etc. Ejemplos: Microsoft Azure, OpenShift, Heroku...

__OpenShift__ se encuentra dentro del _PaaS_. Esto permite al usuario abstraerse del sistema operativo y el hardware subyacente, centrándose únicamente en desarrollar su aplicación. Además, _OpenShift_ tiene soporte para los framework web más populares (Django, Node.js, Ruby on Rails...) y, al ser software libre, podemos extenderlo y añadir soporte a cualquier otro. 

_OpenShift_ ha sido desarrollado por __Red Hat__ y se basa en ofrecer contenedores __Kubernetes__ con el software que elijamos (django, ruby on rails, etc). Como veremos a continuación, es muy sencillo desplegar aplicaciones en la nube.

![arquitectura](arquitectura_openshift.png)

## Creando nuestra primera aplicación
En OpenShift nos ofrecen un [tutorial](https://docs.openshift.com/online/getting_started/basic_walkthrough.html#getting-started-basic-walkthrough) para familiarizarnos con su herramienta. Vamos a seguirlo y a analizar el resultado.

1. En primer lugar, debemos hacer un fork del repositorio ![nodejs-ex](https://github.com/openshift/nodejs-ex) a nuestra cuenta personal de github y clonarlo en nuestro ordenador.

2. Una vez tenemos el repositorio clonado, creamos un nuevo proyecto en la consola web de OpenShift.

    ![newproject](newproject.png)

3. OpenShift nos ofrece varias opciones, según la herramienta con la que hayamos desarrollado nuestro proyecto. En nuestro caso, elegimos __Javascript__.

    ![catalogo](catalogo.png)

4. Seleccionamos la plantilla __Node.js + MongoDB__:

    ![options](options.png)

5. En la siguiente pantalla, sólo debemos cambiar la URL de Github por la de nuestro propio fork:

    ![create](create.png)

6. Una vez creada nuestra aplicación, tenemos varias opciones:
    * Usar la herramienta de consola `oc` para trabajar.
    * Usar la consola web de OpenShift

    ![nextsteps](nextsteps.png)

### Sincronizando Github y OpenShift
Si queremos que cada cambio que subamos a github se sincronice automáticamente con OpenShift, debemos configurar un [_Webhook_](https://developer.github.com/webhooks/). Para ello debemos:

1. Copiar la URL de nuestro _Webhook_. Tenemos varias opciones:
    * Copiarla de la sección _Making Code Changes_ de la pantalla _Next Steps_.
    * Copiarla de la consola web de OpenShift:
        
        a. Accede a los _Builds_ de tu proyecto y haz click sobre uno de ellos
        
        ![builds](builds.png)

        b. En la pestaña _Configuration_ se encuentra la URL de nuestro _Webhook_

        ![webhooks](webhooks.png)

2. En la pestaña _Settings_ de nuestro proyecto de Github, acceder a _Webhooks & Services_ y copiar la URL en el campo __Payload URL__.

    ![webhooks](webhooks.png)


### Usando la herramienta `oc`
La herramienta para línea de comandos de _OpenShift_ es muy sencilla de usar: basta con descargar el ejecutable que nos dan en su página web comprimido en `tar.gz` y extraerlo:

```bash
$ tar -xf ~/Downloads/oc-3.4.1.2-1-linux.tar.gz
```

![downloadoc](downloadoc.png)

Una vez extraído, tendremos un archivo ejecutable llamado `oc`

![loginoc](loginoc.png)

## Análisis de la interfaz de OpenShift

La interfaz web de _OpenShift_ es bastante sencilla. Tiene seis submenús básicos:

![interfaz1](interfaz1.png)

Cada uno de estos nos permite controlar las distintas versiones (builds) de nuestra aplicación, los distintos [pods](https://docs.openshift.org/latest/architecture/core_concepts/pods_and_services.html) y aplicaciones que tengamos (esto tiene más sentido para una versión que permita tener más de un servicio a la vez), los recursos que tenemos disponibles y los que estamos usando etc.

![interfaz2](interfaz2.png)
![interfaz3](interfaz3.png)
![interfaz4](interfaz4.png)
