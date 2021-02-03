# Current machines

|Name|	IP|	User	|Password|	OS|
|---|:---:|---|---|---|
|web.ubuntu.A	|77.68.6.27	|root|	InV_@K4tX5|	ubuntu 18.0.4|
|web.ubuntu.B	|213.171.210.28|root|	k$#OKx2Jd*|	ubuntu 18.0.4|
|web.ubuntu.C	|77.68.28.47	|root|	O60i?$78Vm|	ubuntu 18.0.4|
77.68.7.117


# Current Task

## Preparations: Cron 
Cron to run not by individual tasks but by functions of different frequencies. Tasks will then be grouped under the desired time frequency functions.
#### functions_5_minutes
   - runs account_get_ip to check for the state of the server.
#### functions_30_minutes (00:00 and 30:00)
  -  runs download_fx_data 
#### functions_12_hours (04:00 and 16:00)
  -  runs download_rates_data
#### Failure in any of the functions should result an email to be sent to the webmaster with the appropirate information
#### Document the steps on how they work and how to run them etc. inside the README file.

## Preparations: Deployment to UAT 
- Deploy the pages onto a uat environment
- Document the steps on how to deploy including the installation of the packages and library needed (see the existing README file in the repository.)
- Perform all the testing necessary (various browsers, accounts functionalities, etc.)

## Preparations: Deployment to PROD (£300 for the three above, 3 days)
- Map our www.treasuryquants.com the new IP given the ip of the machine we have. (what does it take?)





# Next Task
- Unit Tests


# We are Live!


### For Shahram

## Code Improvement

modify process_fatal_error such that no more than one email is sent on the same each subject (source_caller) (Shahram)
rename account_api to api_gateway(Shahram)
rename apis_for_json to apis_gateway(Shahram)
rename cron_grids to crons(Shahram)



### For Daria

## Website Improvements 1 (Shahram)
- The video object in video section reduces as the page size reduces but not the black screen that holds it.
   

## Website Improvements 2 (Daria)
- A simple cookie consent popup (I have asked James to design one following your suggestion)
- In the navigation bar, replace About Us, Policy notice and Terms with "about" and place about us, policy notice and terms of service under about as sub-menu

## Website Improvements 3 (Daria)
- workbench design 


## Website Improvements 3 (?)
- Incorporate Google Analytics with the site.
 
## 




