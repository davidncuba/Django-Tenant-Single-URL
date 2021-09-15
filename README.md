<h4 align="center">Django Tenants Single URL</h4>
<h2 align="center">tenant.localhost:8000 <img src="https://cdn-icons-png.flaticon.com/128/1828/1828665.png" width="25"></h2>
<h1 align="center">localhost:8000<img src="https://cdn-icons-png.flaticon.com/128/3472/3472620.png" width="25"><h2>

## How To Use

To clone and run this application:

```bash
# Clone this repository
$ git clone https://github.com/davidncuba/Django-Tenant-Single-URL.git

# Go into the repository
$ cd Django-Tenant-Single-URL

# Create a Virtualenv
$ python3 -m venv env  
$ source env/bin/activate 
  
# Install dependencies
$ pip install -r requirements.txt

# Configure Postgresql 
$ setup/setting.py

# Make migrations django
$ python manage.py makemigrations

#Migrate to Database
$ python manage.py migrate

#create new tenant schema(you can create many tenant)
$ python manage.py client


# Create Tenant Superuser
$ python manage.py create_tenant_superuser
```
## Libraries

  <a href="https://www.djangoproject.com">Django</a></br>
  <a href="http://www.django-rest-framework.org/">Django Rest Framework</a></br>
  <a href="http://django-tenants.readthedocs.io/en/latest/">Django-Tenants</a></br>


