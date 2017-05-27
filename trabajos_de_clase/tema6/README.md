# Tema 6 - Asegurar el sistema web

__1. Aplicar con *iptables* una política de denegar todo el tráfico en una de las máquinas de prácticas. Comprobar el funcionamiento.__

__Aplicar con *iptables* una política de permitir todo el tráfico en una de las máquinas de prácticas. Comprobar el funcionamiento.__

---

__2. Comprobar qué puertos tienen abiertos nuestras máquinas, su estado y qué programa o demonio los ocupa.__

---

__3. Buscar información acerca de los tipos de ataques más comunes en servidores (p. ej. secuestros de sesión). Detallar en qué consisten, y cómo se pueden evitar.__

Además de los ataques mencionados en el tema 6 de teoría, algunos de los más populares son:

* [__Secuestro de sesión__](https://en.wikipedia.org/wiki/Session_hijacking): consiste en entrar de forma no autorizada a un información o servicios de un sistema informático. Este acceso se hace robando la _cookie mágica_ que se usa para autenticar a un usuario en un servidor remoto. En el desarrollo web, las cookies se utilizan para mantener la sesión del usuario y dichas cookies pueden ser robadas con facilidad por un atacante. Así, si nos identificamos en una web y alguien nos roba la cookie HTTP, podrá identificarse en dicha web sin necesidad de introducir nuestro usuario y contraseña. Hay más tipos de secuestros informáticos detallados en [Wikipedia](https://es.wikipedia.org/wiki/Hijacking).

* [__Inyección SQL__](https://es.wikipedia.org/wiki/Inyecci%C3%B3n_SQL): consiste en introducir código SQL maligno dentro del código SQL programado, para alterar el funcionamiento normal de un programa o aplicación y lograr así que se ejecute dicho código invasor en la base de datos. Dicho código malicioso podrá insertar registros, modificar o eliminar datos, autorizar accesos e incluso ejecutar otro tipo de código malicioso en el ordenador.

* [__Man-in-the-middle__](https://en.wikipedia.org/wiki/Man-in-the-middle_attack): el atacante se coloca entre una comunicación entre dos finales. Puede o bien simplemente escuchar la comunicación entre ambos o, incluso, modificarla. Muchos protocolos, como SSH, realizan pruebas de integridad en las comunicaciones para asegurarse de que nadie las está escuchando o modificando. Braulio y yo hicimos un [trabajo](https://github.com/mgmacias95/SSH-El-Ataque-MITM) sobre este ataque en SSH para la asignatura _Ingeniería de Servidores_.

* [__DNS Amplification Attack__](https://www.us-cert.gov/ncas/alerts/TA13-088A): es una forma muy popular del ataque DDoS que se basa en el uso de los DNS públicamente accesibles para saturar a la víctima con tráfico DNS.
