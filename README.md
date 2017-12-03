# project overview
  * You will develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. 

_________________________________________________________

# the steps of project to run.
	
   * Download python3 and install it.

   * create new project  and name it project2

   * go to (https://console.developers.google.com/project) and login with Google.

   * Select "API's and Auth Credentials

   * Create a new OAuth client ID" from the project menu

   * On the Terminal
         ** type in a product name and save.

   * In Authorized javascript origins add:
         ** http://0.0.0.0:5000
         ** http://localhost:5000 

   * Click create client ID

   * Click download JSON and save it into the project which i create. 

   * Rename the JSON file (client_secrets.json)

   * the "login.html" replace data-clientid="13140951618-15nik769cellkubaqnjk5facdib2dh4d.apps.googleusercontent.com"
     use to sign in google
# create database

   * Download Vagrant and install it   

   * Create file (item_database_cat.py) and put in it three tabe of database.

         ** categories_menu the table of categories have.
           *** id of it.
           *** name of each  Category.

         ** user the table of user have.
           *** id of each  user.
           *** name of each  user.
           *** img_user of each  user.
           *** email of each  user.

         ** items_menu the table of items have.
           *** id of each  item.
           *** name of each  item.
           *** description of each  item.
           *** cat_id of each  item.
           *** user_id of each  item.


   * Make sure vagrant install by vagrant --version ( `Vagrant 1.8.1` )

   * Open terminal and go to path file vagrant 

   * write vagrant up
   
   * write vagrant ssh

   * write cd  /vagrant/project2
   
   * then write python item_database_cat.py
   
   * Create file (DB_operation.py) and put in it functions.
          
        **  adduser         : to add user in tabel user by Google. 
          
        **  GetUserBy       : to check if user in data or not to add.
          
        **  GetCategoryBy   : to get Category from data.
          
        **  GetAllCategoryBy: to get all Categories from data.
          
        **  GetItemBy       : to get item from data.
           
        **  Get_last_item   : to get all items from data.
 
        **  addDatabase     : to add item and upload in data.
      
        **  deleteDatabase  : to delete item from data.
  
   * then open Terminal and call it file by (DB_operation.py).

   * Create file (insted_categories_in_database.py) and use it to put the Categories in categories_menu tabel.
   
   * then open Terminal and call it file by (insted_categories_in_database.py).
   
   * the put client_secrets.json in the file and Vagrantfile.

   * then make folder templates and put in it 7 file. 
        
        ** login.html      : that page show all catalog and the sign in Google.  
         
        ** categoires.html : that page show all categoires and items of it after login.  

        ** cat.html        : that show each cateogry and all it's items.   

        ** itemShow.html   : login.html that show each item. 

        ** addItem.html    : that add item in database.

        ** delete_item.html: that delete item from database. 
 
        ** edite_item.html : that esite item in database.
   
   * Create file show.py that conected.
#JSON API
        ** the function catalogJSON that show json for categoires.
     
        ** the function catalogJSON that show json for categoires.
#connected in google     
        ** the function gconnect that use to sign in Google.
#login google     
        ** the function showLogin use to sign in Google.
#start Pages show   
        ** the function showCategories that show categoires.
# CRUD Operations     
        ** the function show_items_for_category that show for items.
     
        ** the function showItem that use to show item.
     
        ** the function addItemCat that use to add item.
     
        ** the function editItem tthat use to edit items.
     
        ** the function deleteItem that use to delete items.
#desconnectes in google     
        ** the function gdisconnect that use to sign up Google.

  
### Open in a webpage
   * Now you can open in a webpage by going to either:
         ** http://0.0.0.0:8080
         ** http://localhost:8080 
         ** then open Terminal and call it file by (show.py).

