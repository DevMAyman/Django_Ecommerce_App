# Django_Ecommerce_App

## Django Project Setup Guide

This guide will walk you through setting up a Django project on Ubuntu.

### Step 1: Install Python and Pip

Make sure you have Python and pip installed on your system.
pip is packege manager that using to download django framework

```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Step 2: Install latest version of virtualenv using pip3

```bash
  pip3 install virtualenv
```


### Step 3: Create virtual env for your project
Virtual env isolate your project packages from all other packages in your machine.
Navigate to directory you want locate your project in. 

Do not make specific directory for your project with its name as its virtualenv role.

```bash
  python3 -m venv ecommerce
```


### Stpe 4: Active virtualenv 

```bash
cd ./ecommerce
source ./bin/activate
```
It appears in two picture that my prompt changes when i active virtualenv than before. 


### Step 5: Install Django

```bash
pip3 install django
```

### Step 6: Create your project

```bash
django-admin startproject project
```

### Step 7: Connect to PostgreSQL

1. Deploy a PostgreSQL database using https://railway.app/ .
2. Start a New Project and choose to Provision PostgreSQL.
3. Wait for the provisioning process to complete.
4. Click on your PostgreSQL instance and navigate to Variables.

Once the website configuration is complete, configure your project's `settings.py` file as follows:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',           # Replace with your database name
        'USER':  PGUSER,             # Replace with PGUSER from Railway Variables
        'PASSWORD': PGPASSWORD,      # Replace with PGPASSWORD from Railway Variables
        'PORT': PGPORT               # Replace with PGPORT from Railway Variables
    }
}
```

If you want connect locally on mysql use that

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecommerce', # Create DB with that name first
        'USER':'root',
        'PASSWORD': 'mysql@123',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}
```
### Step 8: Configure .env file 

1. Add .env file. 
2. Add its name in .gitignore file.
3. Add your DB passwords and secret key.
4. Add python-dotenv
```bash
pip install python-dotenv
```
5. Add this lines in settings.py file
  import os
  from dotenv import load_dotenv
  dotenv_path = os.path.join(BASE_DIR, 'config', '.env')
  load_dotenv(dotenv_path)

6. Then get your secrets and password from .env
os.environ.get('Name_in_env')

### Step 9: Do not forget add requirements.txt

Like package.json, in python we have requirements.txt file.
In this file we lock all packages we use them in our application.
When someone clone our project, just write this command to add all packages in his project

```bash
pip install -r requirements.txt
```

