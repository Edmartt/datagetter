# Datagetter

This script fetch data from fifa fut21 api and complementary for using [rest-fut21](https://github.com/Edmartt/rest-fut21)

## Install:

### On Windows

```
git clone https://github.com/Edmartt/datagetter.git
```

```
cd datagetter/
```

```
pip install -r requirements.txt
```

```
set MYSQL_HOST=0.0.0.0
```

```set MYSQL_USER=the same username for the database user in [rest-fut21](https://github.com/Edmartt/rest-fut21)```

```set MYSQL_PASSWORD=same as above, put the same password that you have for your mariadb/mysql instance```

```set MYSQL_DATABASE=the same as rest-fut21```

```set MYSQL_PORT=32000 (this is a forwarded port from the same container running rest-fut21 service)```


### On Linux

```
git clone https://github.com/Edmartt/datagetter.git
```
```
cd datagetter/
```

```
pip install -r requirements.txt
```

```
export MYSQL_HOST=0.0.0.0
```

```export MYSQL_USER=the same username used for rest-fut21```
    
```export MYSQL_PASSWORD=the same used for rest-fut21```

```export MYSQL_DATABASE=the same database for rest-fut21```

```export MYSQL_PORT=32000 (this is a forwarded port from the same container running rest-fut21 service)```

#### Note:

**it requires that the container with the rest21 service it's started**
	

Set a **.env** file for using before running following the **.env.example** file

## Running:

   ### On Windows:

    $ python script.py

   ### On Linux:
    
    $ python3 script.py
  
   The script will do a GET request to [Fifa Ultimate Team](https://futdb.app/api) API and will save the data in the rest-fut21 project container database. Every successful request it will ask if we want to continue and if we answer a **y** it will keep saving the data for every available page with data. If we type* ***n** the script will end of getting pages data and now we can use rest-fut21 making request according to docs in the readme.

If you want to test the saved data just create a connection with the MariaDB/MySQL client installed on your local machine 

#### Note:

Remember that you will be running the rest-fut21 project first with docker-compose, and this is necessary because we need to save the data in mariadb/mysql volumen for querying this data later in rest-fut21 service

i.e:


    $ mariadb -u username -h 0.0.0.0 -P <forwarded-port-from-rest-fut21> -p mypassword

Or:

    $ mariadb -u username -h 0.0.0.0 -P <forwarded-port-from-rest-fut21> -p (press enter)

    Password: *********
