set -o errexit

pip install -r requirements.txt

python manage.py migrate