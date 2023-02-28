
# didactic-octo-fiesta

### Setup

The first thing to do is to clone the repository:

```sh
git clone https://github.com/mariaadannies/didactic-octo-fiesta.git
cd didactic-octo-fiesta
```
Check if python already installed or no:
```
python -V
```

Create a virtual environment to install dependencies in and activate it:
```
python –m venv env    
```

Activate virtual environment:
```
(Window)    env\Scripts\activate
(Mac)       env/bin/activate
```

Install Django:
```
python -m pip i Django
```

Runserver:
```
py manage.py runserver
```

Navigate to `http://127.0.0.1:8000`