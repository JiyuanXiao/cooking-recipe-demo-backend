# cooking-recipe-demo-backend

This is a demo backend of cooking recipe web app built on Django framework

## Setup

1. Update the system and install required packages:

```bash
sudo apt update
sudo apt install nginx gunicorn python3 python3-pip pytohn3-venv -y
```

2. Clone the repo and open the working directory:

```bash
git clone https://github.com/JiyuanXiao/cooking-recipe-demo-backend.git
cd cooking-recipe-demo-backend
```

3. Activate python environment and install denpendencies:

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

4. Migrate models:

```bash
python manage.py migrate
```

5. Start testing the server:

```bash
python menage.py runserver
```

This will launch the server on http://127.0.0.1:8000/ for local testing.

## Deploy on AWS EC2

If the server runs on AWS EC2 instance, connect to your EC2 instance and do the step 1-4 in the Setup section first.

In order to make the server connect to port 80 and keep the server running in background, we need to use Gunicorn and Nginx for the deployment.

### Setup Gunicorn

1. Create a systemd service file for Gunicorn:

```bash
sudo nano /etc/systemd/system/gunicorn.service

```

Add the following content (adjust paths as needed):

```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/path/to/your/django/project
ExecStart=/path/to/your/django/project/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/run/gunicorn.sock cooking_recipe_backend.wsgi:application

[Install]
WantedBy=multi-user.target
```

2. Give this user permission to write to the /run directory and other permission to project:

```bash
sudo chown ubuntu:ubuntu /run
sudo chmod 755 /run
sudo chown -R ubuntu:ubuntu /path/to/your/django/project
```

3. Start and enable the Gunicorn service:

```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

4. Check the Gunicorn service status:

```bash
sudo systemctl status gunicorn
```

You should see the sevrer is active (running)

### Config Nginx

1. Create an Nginx server block configuration file

```bash
sudo nano /etc/nginx/sites-available/django
```

Add the following content (adjust paths and server public IP address as needed):

```
server {
    listen 80;
    server_name 123.456.789.123; # Enter your EC2 IP address

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /path/to/your/django/project;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```

2. Enable the Nginx configuration:

```bash
sudo ln -s /etc/nginx/sites-available/django /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

### Config Django project allowed host

1. Open project setting file:

```bash
nano /path/to/your/django/project/your_project/settings.py
```

2. Add your IP to ALLOWED_HOSTS:

```bash
ALLOWED_HOSTS = ['your EC2 IP address']
```

### Restart Gunicorn

```bash
sudo systemctl restart gunicorn
```

Now, the application should be accessible at EC2's IP address and will continue running even after you disconnect from the EC2 instance.
