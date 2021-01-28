# On going task
## Site Maintenance (£150 per month)
- Full ownership of stability of continuous functionality of the site (the most important)
- Perform all the steps needed for the release (if any) from uat/dev
- Ensure that the maintenance document remains up-to-date and it is adhered to.
- Small tactical bug fixes just to ensure smooth site operation.
- No new implementation.


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


# Website improvements
We will have ongoing improvements in stages.


## Code Improvement


### For Daria

How to (or should we) move web_api and all its dependencies to account app (the only api that app uses is the formatted_grid_swap_rates)?
Any error initiated from js from any front-end function will show up as "web cron error"
Change process_fatal_error signature to process_fatal_error (subject, error_message, is_development=False). 
Change post_message to post_message(subject, request)
Use source_caller as the subject argument from the front-end when calling post_message
Can we remove get_market_data and replace it with get_swap_rates_data (and remove files array)?

### For Shahram

modify process_fatal_error such that no more than one email is sent on the same each subject (source_caller) (Shahram)
rename account_api to api_gateway(Shahram)
rename apis_for_json to apis_gateway(Shahram)
rename cron_grids to crons(Shahram)


## Website Improvements 1
- In profile screen-> change IP, please populate the field with user's IP as default.
- In profile screen, replace "welcome, logout" with a new row on the top to show email.
- In profile screen, replace "welcome, logout" with a new row on the top to show email.
- View More in video section to redirect to about us page.
- the video object in video section reduces as the page size reduces but not the black screen that holds it.
- remove the default "test.account@treasuryquants.com" from all email entries.
- Currency in profile page should be rounded to two decimals.
- A simple cookie consent banner (do we need James for this?)
- Following text to be places at the bottom of the charts (in markets page) in italic, left justified:

    **Swap rates are shown in percentage points using market conventions for each currency market. The swap rate market data is sourced from various OTC clearing houses' closing settlement rates for the dates shown. FX rates are source directly from ECB, periodically.*

## Website Improvements 2
- In the navigation bar, replace About Us, Policy notice and Terms with "about" and place about us, policy notice and terms of service under about as sub-menu 
- View More in video section to redirect to about us page.
- Server status sign on the webpage (active/inactive, on/off, etc.)


## Code Refactoring 
- Provide a proposal to enhance the structure of the files/folders and coding improvements for both front-end and back-end.
- more exception handling/renaming the source-caller to unique strings


## New Implementation: Workbench 
- to be completed later

 
