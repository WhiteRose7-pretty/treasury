# Deployment to production server
## System condition
- ubuntu 16.04 and higher

## package condition
- python: 3.5 and higher
- rabbitMQ
- docker
- docker compose

## python package (requirements.txt)  
- Django: 2.2 adn higher
- TQapis: latest
- Celery: 4.4.0rc2 and higher
- gunicorn: latest
- other packages are in requirements.txt 

## Step by step

### 1. Updating package

     sudo apt-get update
     sudo apt-get -y upgrade

### 2. docker install

    curl -fsSL https://get.docker.com/ | sudo sh
    # confirm install
    docker --version
    
### 3. docker compose install

    sudo curl -L https://github.com/docker/compose/releases/download/1.25.0-rc2/docker-compose-`uname -`s`-uname -m` -o /usr/local/bin/docker-compose
    # confirm install
    docker-compose --version

### 4. Create folder for installation

    cd /home
    mkdir docker

### 5. Download project

    # if you didn't install git
    apt install git
    # for dev branch
    git clone -b dev https://github.com/shahram-alavian/web_daria.git
    # for master branch
    git clone https://github.com/shahram-alavian/web_daria.git

### 6. Move the project folder and copy config files, run docker

    cd web_daria
    cp -a treasury/app/media/. /opt/media/
    cp -a treasury/app/configs/. /opt/configs/
    docker-compose up --d

### 7. Check if docker image, containers created exactly

    docker-compose ps
        >>>>>>    
        celery_beat         sh -c celery -A app_rama b ...   Up
        celery_worker       bash -c celery -A app_rama ...   Up
        django              bash -c python manage.py m ...   Up      0.0.0.0:8000->8000/tcp
        rabbitmq            docker-entrypoint.sh rabbi ...   Up      15691/tcp, 15692/tcp, 25672/tcp, 4369/tcp, 5671/tcp, 0.0.0.0:5672->5672/tcp
        web_daria_nginx_1   /docker-entrypoint.sh ngin ...   Up      0.0.0.0:80->80/tcp

    docker image list
        >>>>>>
        app_image         latest          ad41c0ea678c   14 minutes ago   1.1GB
        web_daria_nginx   latest          dc6119c5ef5f   7 hours ago      21.3MB
        rabbitmq          latest          c05fdf32bdad   2 weeks ago      156MB
        python            3.8.5           28a4c88cdbbf   5 months ago     882MB
        nginx             1.19.0-alpine   7d0cdcc60a96   8 months ago     21.3MB
                
    docker container list
        >>>>>>
        CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS          PORTS                                                                    NAMES
        5dc9f6a2dd4c   app_image:latest   "sh -c 'celery -A ap…"   14 minutes ago   Up 14 minutes                                                                            celery_beat
        432ef853fcd3   web_daria_nginx    "/docker-entrypoint.…"   14 minutes ago   Up 14 minutes   0.0.0.0:80->80/tcp                                                       web_daria_nginx_1
        1007f3459e37   app_image:latest   "bash -c 'celery -A …"   14 minutes ago   Up 14 minutes                                                                            celery_worker
        9aa60ec60cc6   app_image:latest   "bash -c 'python man…"   14 minutes ago   Up 14 minutes   0.0.0.0:8000->8000/tcp                                                   django
        7dcffa4f56cd   rabbitmq:latest    "docker-entrypoint.s…"   14 minutes ago   Up 14 minutes   4369/tcp, 5671/tcp, 15691-15692/tcp, 25672/tcp, 0.0.0.0:5672->5672/tcp   rabbitmq
    

### 8. See log

    docker logs -f celery_beat
    docker logs -f celery_worker
    docker logs -f django
    docker logs -f nginx 


### 8. Update Ip of webmaster


## how to update server

### 1. Move to project folder and down server

    cd /home/docker/web_daria
    docker-compose down


### 2. Update source

    # for dev
    git pull origin dev
    
    # for master
    git pull origin master

### 3. Delete docker image

    docker image rm -f app_image
    
### 4. Restart docker compose

    docker-compose up --d




    
    
        

    
