## Description
This is a Django test project using SQLite, Docker and ['The Star Wars API'](https://swapi.dev/).


## Launch instructions
_____

1. Clone repository to your local folder;
2. *Install all packages from requirements.txt: ```pip install -r requirements.txt```;
3. *Insatll all packages from package.json: ```cd ./static && npm install```;
4. For this step you should already have installed Docker and docker-compose on your PC:
- make sure You are in project folder: ```cd 'root project folder' ```;
- Run docker-compose: ```docker-compose up --build```;
- Installation can take some time, it depends on your PC resources;
- After the installation is completed, the server will start automatically on 0.0.0.0:8800;
- Open app using http://0.0.0.0:8800/ in your browser;
5. The superuser does not exist;
- You can manually create superuser for Your own purpose: ```cd 'root project folder' && python3 manage.py createsuperuser``` ;
6. Note that DataBase - sqlite3;
7. To stop the server: ```Ctrl+C```;
8. To completely remove all created docker containers, images and volumes: ```docker-compose down --volumes```.

_____
*p.s. points № 3 and 2 are not necessary* 