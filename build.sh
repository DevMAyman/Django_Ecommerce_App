set -o errexit

pip install -r requirements.txt

python manage.py collectstaticp
python manage.py migrate