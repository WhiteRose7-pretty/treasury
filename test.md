# How to test website
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

## Add 404, 500 error page
    we need to 404, 500 error page matched with template in production. 
    
## workbench page.
