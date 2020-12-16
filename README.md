# employee_management_system

git clone https://github.com/motaz-hejaze/employee_management_system.git

cd employee_management_system

virtualenv venv -p python3.7

Linux,Unix => source venv/bin/activate
Windows => venv/Scripts/activate

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
