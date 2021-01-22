
# Todo


## Code Refactoring
- rename account_cycle to account_lifecycle
- move/rename treasury.app.modules to treasury.lib  
- Move all codes not explicitly needed for each app away from that app and place them in various and relevant files inside treasury.lib
- Remove account_api from app.views.py
- move treasury.app.media.currency_data to treasury.app.markets.grid_data 
- create a file  called site_functions.py inside each app
- move all functions (that are called from js from html) from views.py to inside site_functions.py for each app 
- views.py to only hold functions for loading.
- update README 
