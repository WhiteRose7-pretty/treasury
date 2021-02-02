# Deployment to production server
## System condition
- ubuntu 16.04 and higher

## package condition
- python: 3.5 and higher
- rabbitMQ

## python package (requirements.txt)  
- Django: 2.2 adn higher
- TQapis: latest
- Celery: 4.4.0rc2 and higher
- gunicorn: latest

## Updating package
    sudo apt-get update
    sudo apt-get -y upgrade

## NGINX to handle static resources and to start the server
    sudo apt-get -y install nginx

## The Supervisor installation starts and manages the application server in the event of a failure or restart
    sudo apt-get -y install supervisor

    sudo systemctl enable supervisor
    
    sudo systemctl start supervisor

## Installation of a virtual environment (for python 3)
    sudo apt install -y python3-pip

    sudo apt install build-essential libssl-dev libffi-dev python3-dev

## Application user configuration
    adduser app

    gpasswd -a app sudo


## Virtual environment configuration
  "python3.5 -m venv." - (this should be done in the user's home directory / home / app)
  ( if you cannot enter the directory, restart PUTTY) (if premision denide should be used before python3.5 'sudo'
  
   Please check python version by command " python3 --version "

   if you are using python 3.6, use "python3.6 -m venv."

    cd /home/app

    #install package for create virtual environment
    apt-get install python3-venv

    #create virtual environment
    python3.6 -m venv .
    
    #activate venv
    source bin/activate

## Installing the application
    su app
  'cd name-repository' - project specific, in our case, web_daria
   project-name, in our case, treasury 
   if you didn't intall git, install git by "apt install git"

    git clone https://github.com/shahram-alavian/web_daria.git
    
    cd name-repository/project-name
    
    pip install -r requirements.txt

## confirm STATIC_ROOT in settings.py
    STATIC_ROOT = os.path.join(BASE_DIR, '..', '..' ,'static')

## Create - gunicorn_start
  (I need to be in / home / app to run this)
  We create a file called gunicorn_start in the bin folder
    cd /home/app
    vim bin/gunicorn_start

## gunicorn_start FILE
  I create a file with the following VIM content I close with ': wq!'
  (you can use other editor what you prefer.)

    #!/bin/sh
    
    NAME="app"
    DIR=/home/app/web_daria/treasury
    USER=app
    GROUP=app
    WORKERS=3
    TIMEOUT=600
    BIND=unix:/home/app/run/gunicorn.sock
    DJANGO_SETTINGS_MODULE=app_rama.settings
    DJANGO_WSGI_MODULE=app_rama.wsgi
    LOG_LEVEL=error
    
    cd $DIR
    source ../../bin/activate
    
    export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
    export PYTHONPATH=$DIR:$PYTHONPATH
    
    exec ../../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
      --name $NAME \
      --workers $WORKERS \
      --timeout $TIMEOUT \
      --user=$USER \
      --group=$GROUP \
      --bind=$BIND \
      --log-level=$LOG_LEVEL \
      --log-file=-

## We make gunicorn_start customizable
    chmod u+x bin/gunicorn_start

## We create a directory called run
    # create as su app !!!
    mkdir run

## Configuring Supervisor to take care of starting the gunicorn server
  (in the / home / app folder if I am 'app' in the current location)

    mkdir logs
    touch logs/gunicorn-error.log

## We create a new super configuration file
    sudo vim /etc/supervisor/conf.d/app.conf

## app.conf FILE

    [program:app]
    command =sh /home/app/bin/gunicorn_start
    user = app
    autostart = true
    autorestart = true
    redirect_stderr = true
    stdout_logfile = /home/app/logs/gunicorn-error.log

## Refreshing the supervisor configuration file and making the new program available
  If everything is ok, then we check the application status (the result is like the RUNNING pid 20195 app, uptime 0:00:29).

  If the application refreshes all the time, delete the entire run folder and create it again as NOT SUDO, e.g. as 'su - app'
  
  If you want to update your app's source code with a new version, you can download the code from GitHub and then restart the process:
  sudo supervisorctl restart app

    sudo supervisorctl reread
    sudo supervisorctl update
    
    sudo supervisorctl status app

## NGINX configuration
    sudo vim /etc/nginx/sites-available/app 
   Adding a new file called app in / etc / nginx / sites-available /

    upstream app_server {
        server unix:/home/app/run/gunicorn.sock fail_timeout=0;
    }
    
    server {
        listen 80;
    
        # add here the ip address of your server
        # or a domain pointing to that ip (like example.com or www.example.com)
        server_name 213.171.210.28;
    
        keepalive_timeout 5;
        client_max_body_size 4G;
    
        access_log /home/app/logs/nginx-access.log;
        error_log /home/app/logs/nginx-error.log;
    
        location /static/ {
            alias /home/app/static/;
        }
    
        # checks for static file, if not found proxy to app
        location / {
            try_files $uri @proxy_to_app;
        }
    
        location @proxy_to_app {
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          proxy_set_header Host $http_host;
          proxy_redirect off;
          proxy_pass http://app_server;
        }
    }   
    
   
  
## Symbolic link to a directory of enabled sites

    sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/app
  
## Removing the default NGINX page

    sudo rm /etc/nginx/sites-enabled/default

## Restarting NGINX
  In order to verify that everything is working, you can restart the remote computer

    sudo service nginx restart
    
    sudo reboot

## Static File
    
    cd /home/app/web_daria/treasury

    source ../../bin/activate

    python manage.py makemigrations

    python manage.py collectstatic

    sudo supervisorctl restart app
    
## Confirm if site is working in browser

## Install RabbitMq
    apt-get install rabbitmq

## Run RabbitMq
    rabbitmq-server

##  app-celery-beat.conf
  We create a new file in the folder 'etc / supervisor / conf.d /' called 'app-celery-beat.conf'. May change logs to 'app-Rama-beat.log
  
    [program:app-celery-beat]
    command=/home/app/bin/celery beat -A app_rama -l INFO
    directory=/home/app/web_daria/treasury
    user=app
    numprocs=1
    stdout_logfile=/home/app/logs/app-rama-beat.log
    stderr_logfile=/home/app/logs/app-rama-beat.log
    autostart=true
    autorestart=true
    startsecs=10
    stopwaitsecs = 600
    killasgroup=true
    priority=998


## app-celery-worker.conf
Create a new file in the folder 'etc / supervisor / conf.d /' called 'app-celery-worker.conf'

    [program:app-celery-worker]
    command=/home/app/bin/celery worker -A app_rama -l INFO
    directory=/home/app/web_daria/treasury
    user=app
    numprocs=1
    stdout_logfile=/home/app/logs/app-rama-worker.log
    stderr_logfile=/home/app/logs/app-rama-worker.log
    autostart=true
    autorestart=true
    startsecs=10
    stopwaitsecs = 600
    killasgroup=true
    priority=998


## bash (after enabling the virtual environment)

    source /home/app/bin/activate
    sudo supervisorctl reread     
    sudo supervisorctl update     
    
    sudo supervisorctl restart app     
    sudo supervisorctl status app
    sudo service nginx restart 
    
    sudo supervisorctl start app-celery-worker
    sudo supervisorctl stop app-celery-worker
    sudo supervisorctl status app-celery-worker 
    
    sudo supervisorctl start app-celery-beat 
    sudo supervisorctl stop app-celery-beat
    sudo supervisorctl status app-celery-beat


