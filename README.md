# Django Custom User with JWT

Simple Django custom user with JWT as the authentication method.

## Setup

The first thing to do is to clone the repository:

```bash
git clone https://github.com/IPoorya/django_custom_user_jwt
cd django_custom_user_jwt
```
Create a virtual environment to install dependencies in and activate it:
```bash
python3 -m venv env
source env/bin/activate
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install -r requirements.txt
```
Once pip has finished downloading the dependencies, create migrations and apply them:
```bash
python manage.py makemigrations
python manage.py migrate
```

and run server:
```bash
python manage.py runserver
```
check 127.0.0.1:8000/ for swagger 

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.