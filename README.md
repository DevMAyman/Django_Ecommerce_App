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

BEFORE

![image](https://github.com/DevMAyman/Django_Ecommerce_App/assets/123351964/5090eb70-4b7b-4aa4-b6be-f90a00524ce1)

AFTER

![image](https://github.com/DevMAyman/Django_Ecommerce_App/assets/123351964/d9b3e594-85d6-4a88-a43d-0c10feea6f24)

### Step 5: Install Django

```bash
pip3 install django
```

### Step 6: Create your project

```bash
django-admin startproject project
```

### Step 7: Connect to postgres

Go to this website to deploy your postgres 
(https://railway.app/)

Then click on Start a New Project
Then choose Provision PostgreSQL
... Wait some time
Then click on Postgres
Then go to Variables

Now we have been finished all website configration 

Go to your project inside project directory go to settings.py scroll down till DATABASE object
Nearly at line 76 
go to webiste and fill DATABASE object with this values.
Each property in DATABASE object will be copied from Variables at website and its name is same with a liite change.
for example PASSWORD in website in property called PGPASSWORD while in your project called PASSWORD.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'railway',
        'USER':  PGUSER,
        'PASSWORD': PGPASSWORD,
        'PORT':' PGPORT
    }
}








