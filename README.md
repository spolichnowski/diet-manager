# Diet Manager

> Diet manager is an application that allows to track your daily calorie balance. With [Calorie Ninjas API](https://calorieninjas.com) application easily counts calories from given recipes or single ingredients. User can add and save new recipes, track progress when it comes to weight and body measurements.

## Technologies

- Python version: 3.9.6
- Django version: 3.2.6
- Pillow version: 8.3.1
- psycopg2 version: 2.9.1

## Setup

### To run the application:

First of all make sure that you have Python version 3.6.6 installed on your machine.
Prepare virtual environment, for example with:

- pyenv (https://github.com/pyenv/pyenv-virtualenv)
- conda (https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html)
- venv (https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

After creating and running your virtual environment make sure that your 'pip' package installer is working. Check its version for a test and if needed update it:

```
$ pip --version
$ pip install --upgrade pip
```

Now time to install all the requirements:

```
$ cd ../project folder/backend
$ pip install -r requirements.txt
```

If all the requirements has been installed time to create a database:

```
$ psql
$ CREATE USER 'user name' WITH PASSWORD 'password';
$ CREATE DATABASE 'name';
$ GRANT ALL PRIVILEGES ON DATABASE 'name' TO 'user name';
```

After that update settings or .env file with database information.
Now make migrations, migrate and run the server.

```
$ ./manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py runserver
```
Full form can also be used to run django commands: '$python3 manage.py "command"'

## Contact

Created by [Stanisław Polichnowski](https://www.spolichnowski.com)
Templates based on: [Creative Tim](https://www.creative-tim.com)
