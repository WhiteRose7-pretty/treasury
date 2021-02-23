# Deployment to production server
## System condition
- ubuntu 16.04 and higher

## package condition
- python: 3.5 and higher
- rabbitMQ
- docker
- docker compose

## python package (requirements.txt)  
- Django: 2.2 and higher
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

    sudo curl -L https://github.com/docker/compose/releases/download/1.25.0-rc2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    # confirm install
    docker-compose --version

### 4. Create folder for installation

    cd /home
    mkdir docker
    cd docker

### 5. Download project

    # if you didn't install git
    apt install git
    # for dev branch
    git clone -b dev https://github.com/shahram-alavian/web_daria.git
    # for master branch
    git clone https://github.com/shahram-alavian/web_daria.git

### 6. Move the project folder and copy config files, run docker

    cd web_daria
    cp -a treasury_quants/app/media/. /opt/media/
    cp -a treasury_quants/app/configs/. /opt/configs/
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

# How to test site in a new machine after install

   
## !Confirm development status and backend Api connection status(For Administrator)
    1. Confirm development status
        In development status, site doesn't working with full functions.
        So it is important to check if site is in development or production status.
        if site is development, you can see Large red text "This is development environment!".
    2. Confirm backend api server connection
        By some reason, server will not connect with Backend Api.
        Maybe reasons are backend down or internet connection between website and backend server.
## Market page(Home, main page)
    when input domain or ip, you can see market page.

## Create Account
  In this section, test create account page, account-activation page.

    1. You can click "create account" in navbar to open create account page.
    2. You input email and password.
        *Admin input wrong password and check error message.
    3. You check your mail box. And click activation link.
      If you have not any error, you have activated account, and can login.

## Login 
    1. You click "login" in navbar to open login.
    2. Input your email and passord.
        *Admin input wrong password and check error message.
    3. If your email and password are matched, will redirect profile page.
        

## Forgot password
  In this section, confirm confirm-email page to reset password, and password-reset-callback page.

    1. click 'forgot password' in login page.
    2. in page "confirm email for reset password", you input your email.
    3. Check your mail box, click activation link
    4. in page "Reset password", input new password and confirm.
        *Admin input wrong password and check error message.
    
## Profile page
    
    1. if you once login, redirect to profile page, or click profile in navbar.
    2. You confirm your personal information.

## Change Ip
    1. in profile page, you click "change Ip".
    2. in opened modal window, you input your new Ip, click confirm
    3. in profile page, you check if ip changed to new IP.

## Change password
    1. in profile page, you click "change password".
    2. in opened modal window, you input your new password, and confirm and click "change".
    3. and logout and login again to check new password.

## Invalid page.
    By input wrong url from mail box, you can check invalid page.


## Error processing in the case that api server is down
    1. Turn off api server by force
    2. Wait 5min and check if site represent api server status
    




    
    
        

    
