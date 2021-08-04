#Datagetter

Este script es el complemento del proyecto de prueba [rest-fut21](https://github.com/Edmartt/rest-fut21)

## Instalación:
    
   ### En Windows:

    $ git clone https://github.com/Edmartt/rest-fut21.git
    $ cd rest-fut21/
    $ pip install -r requierements.txt
    $ set MYSQL_HOST=127.0.0.1
    $ set MYSQL_USER=dev
    $ set MYSQL_PASSWORD=dev
    $ set MYSQL_DATABASE=playersdata
    $ set MYSQL_PORT=32000


   ### En Linux:

    $ git clone https://github.com/Edmartt/rest-fut21.git
    $ cd rest-fut21/
    $ pip install -r requierements.txt
    $ export MYSQL_HOST=127.0.0.1
    $ export MYSQL_USER=dev
    $ export MYSQL_PASSWORD=dev
    $ export MYSQL_DATABASE=playersdata
    $ export MYSQL_PORT=32000

   ### Nota:
   	**Se requiere haber hecho el despligue del contenedor docker desde rest-fut21**
    
## Ejecución:

   ### En Windows:

    $ python script.py

   ### En Linux:
    
    $ python3 script.py
  
   El script hará GET request a la API de [Fifa Ultimate Team](https://www.easports.com/fifa/ultimate-team/api/fut/item?page=1) y guardará los datos en la base de datos del contenedor en ejecución. Nos preguntará si deseamos continuar a la siguiente página y si respondemos **y** continuará guardando los datos y así continuará el proceso con cada página disponible. Si escribimos 'n', terminará la ejecución del script y ya podremos continuar con el proceso de hacer requests a la api corriendo en el contenedor del proyecto rest-fut21.

   Si se desea comprobar los datos que se han ido guardando, se puede hacer conexión con el cliente de MariaDB/MySQL y acceder con **mysql -u dev --host=127.0.0.1 --port=32000 -pdev**
