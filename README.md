## 📍 About

This is a quick project, just to learn a little about the Django Rest Framework.

## 🚀 Installing the project

To install the project, please follow this few steps:

Windows |
--------|
 * Make sure that you have Python3 on your device, I'm using 3.10 version. 
 * If u don't, you can download it [here](https://www.python.org/downloads/)  
 * Or use Chocolatey to do it. 
 * To use choco, paste this on your prompt cli : 
 ```
  Set-ExecutionPolicy Bypass -Scope Process -Force; `iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1')) 
  ```
 * Then:
 ```
 choco install python3 --pre 
 ```
 
 * Once you have completed this steps, you can navigate to the folder. And now just create a venv:
 
 ```
 python3 -m venv venv
 ```
 ```
 .\venv\Scripts\activate
 ```
 ```
 (venv)python3 -m pip install -r requirements.txt
 ```
 ```
 (venv)cd api
 ```
 ```
 (venv)python manage.py runserver
 ```

Linux & MacOs |
--------------|
* If u dont have Python3, please install following this steps:
```
$ sudo apt-get install python3
```
(Optional install with pip)
```
$ sudo apt-get install python3-pip
```

* Then navigate to the folder location, and create a venv to install the requirements and run the project:

```
python3 -m venv ./venv
```
```
source venv/bin/activate
```
```
(venv)python3 -m pip install -r requirements.txt
```
```
(venv)python manage.py runserver
```
##

Thanks for downloading the project, you can find the Postman collection to test the endpoints on project folder.

<i>May the duck be with you!</i>
<br>
<img width=250px height=250px src="https://s.keepmeme.com/files/en_posts/20200831/duck-with-gun-meme-5e2345d374d15d9b1f65c0b99e9b66a1.jpg">

