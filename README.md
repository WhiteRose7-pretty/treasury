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
This is the process we need to follow to ensure once the new package is released it will work seamlessly. This section should be able to answer the following questions:
- What packages do we depend on ?
- uat machine? uat branch?
- How do we ensure our stability when we roll into a new version of the above packages
- What testing procedure do we take to ensure the new changes in the website will be tested and are ready for release?
- what is the best way to maintain and provide release notes?

### Package/site structures: codes, files and folders
- explain the way the codes, files and folders are structured so someone new can start helping out on 
Production fix process

## Note to developers
All that one needs to get started with collaboration on development.

### Coding Standard
Small coding standards so (python, js) different people write the same way.

### Collaboration Process
How to clone, pull request, ...

     
## Maintenance
What are the steps we need to make sure the site continues to work in production?
# Common issues:
## Server not working:
Every once in a while the server suddenly stops and needs to be restarted. Use putty to login to the server using username and sudo password.
the IP for the server is defined inside app/modules/settings.py. Look for a line like 
    
    target_url = "http://77.68.119.98/"
    
### Go to /home/prod/bin/python/TQmain/
    cd /home/prod/bin/python/TQmain
### Check to ensure the server process is actually running.
    ps ax | grep python
This will filter out all the processes with 'python' in the process name/command line.
There usually is two instances of gateway.py script running using "python"
### Kill server processes
For each of the two instances above take a nore of their PID

    sudo kill -9 <PID 1>
    sudo kill -9 <PID 2>
## Restart the server
    sudo nohup python3 gateway.py shahramalavian > gateway.out &   
The above line ensures the process resides in the background even after the Putty session is closed.

## next Issue (add here)
      