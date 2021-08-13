# Datagetter

Este script es el complemento del proyecto de prueba [rest-fut21](https://github.com/Edmartt/rest-fut21)

## Instalación:
    
   ### En Windows:

    $ git clone https://github.com/Edmartt/rest-fut21.git
    $ cd rest-fut21/
    $ pip install -r requirements.txt
    $ set MYSQL_HOST=127.0.0.1
    $ set MYSQL_USER=nombre de usuario usado en el .env usado para las env vars de [rest-fut21](https://github.com/Edmartt/rest-fut21)
    $ set MYSQL_PASSWORD=password usado en el .env
    $ set MYSQL_DATABASE=nombre de la base de datos del .env
    $ set MYSQL_PORT=puerto usado en el .env


   ### En Linux:

    $ git clone https://github.com/Edmartt/rest-fut21.git
    $ cd rest-fut21/
    $ pip install -r requirements.txt
    $ export MYSQL_HOST=127.0.0.1
    $ export MYSQL_USER=nombre de usuario usado en el .env usado para las env vars de [rest-fut21](https://github.com/Edmartt/rest-fut21)
    $ export MYSQL_PASSWORD=password usado en el .env
    $ export MYSQL_DATABASE=nombre de la base de datos del .env
    $ export MYSQL_PORT=puerto usado en el .env

   ### Nota:
   	**Se requiere haber hecho el despligue del contenedor docker desde rest-fut21**
    
## Ejecución:

   ### En Windows:

    $ python script.py

   ### En Linux:
    
    $ python3 script.py
  
   El script hará GET request a la API de [Fifa Ultimate Team](https://www.easports.com/fifa/ultimate-team/api/fut/item?page=1) y guardará los datos en la base de datos del contenedor en ejecución. Nos preguntará si deseamos continuar a la siguiente página y si respondemos **y** continuará guardando los datos y así continuará el proceso con cada página disponible. Si escribimos 'n', terminará la ejecución del script y ya podremos continuar con el proceso de hacer requests a la api corriendo en el contenedor del proyecto rest-fut21.

   Si se desea comprobar los datos que se han ido guardando, se puede hacer conexión con el cliente de MariaDB/MySQL y acceder con **mysql -u dev --host=127.0.0.1 --port=puerto configurado en el .env -ppassword (la p es del parámetro password y el password está contiguo a la letra p si se desea o se da Enter y se pone el password en un espacio seguro)**
   
ejemplo:

    $ mariadb -u username --localhost=127.0.0.1 --port=puerto configurado en el .env -pmipassword

O
    $mariadb -u username --localhost=127.0.0.1 --port=puerto configurado en el .env -p (presionamos enter)

    Password: *********
