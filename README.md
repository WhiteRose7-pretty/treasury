# Keeping the Site Working and the Code up to Standard
This is a living document: It is continuously updated. It is a short and itemized text providing help and support as to how to interact with the code base / library.

## Our Approach
If left to itself, from the instant a unit of code is released into production, it begins to deteriorate. At best case, it will stay the same. The rate of this deterioration depends on the complexity of the code. The more complex the code unit, the faster it deteriorates.
**In Treasury Quants, we have a concept called 3-to-1**: On average, for every three units of work we do on new features, we need to spend one unit of work purely on ensuring the code has been brough up to the new design and it is up to the standard - and vice versa, for every unit of work on code improvements, we need to have three new features.
This document is to ensure we have a policy and procedure in place to achieve the above 3-to-1 concept, and at the same time, provide support and help for others.

## Installation Procedure
This section should be able to answer the following questions:
- what are the minimum requirements of the machine we need to get the site working on?
- what packages do we need (python, js, ...)?
- procedure for installing them?
- how to deploy?
- how to test the newly site?
- etc..

## Release procedure and policies
**Note**:  Do not touch the current server. This is our current production server that we might be reverting back to
- Rebuild server and update. This server was used as the previous production server
- Install packages
- Clone site
- Test (interactive operations as all unit tests should have passed before)
- Release (or Map domain to server's IP)




### Coding Standard
Small coding standards so (python, js) different people write the same way.

### Collaboration Process
How to clone, pull request, ...


## Maintenance
What are the steps we need to make sure the site continues to work in production?


# Common issues:
## Server not working:
## next Issue (add here)


# Structure
## project setting folder
app_rama/
## app structure
app, account_cycle
### app
   This app is main app of project. There are Market(Home), About us, Policy Notice, Terms of Service.
### account_cycle
   This app is for account management. This does the functions like django-allauth.
    
# Cron work

## How to test on a local host.

### Requirements
#### Celery's installation
    pip install celery

#### RabbitMQ installation
    1. Install in Windows
        1) https://www.youtube.com/watch?v=3sEPqKrFQf8
        2) Run the RabbitMQ service executable - start    
    2. Install in Ubuntu
        apt-get install rabbitmq
        rabbitmq-server
### How to test
    1. Open cmd and go to project folder, and run below command
        celery -A app_rama beat -l info
    2. Open other cmd and go to project folder, and run below command
        celery -A app_rama worker --pool=solo -l info
### How to add cron work
#### Confirm below files.
    app_rama/celery.py
    app_rama/__init__.py
    app_rama/settings.py
    
#### Add tasks.py in app folder
    for example, app/task.py
    
#### Add code in tasks.py
    from celery.task.schedules import crontab
    from celery.decorators import periodic_task
    
    @periodic_task(run_every=(crontab(minute='*/10')))
    def get_all_weather_data():
        print("See you in ten seconds!")
  
    
 
    
   
  