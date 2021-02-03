# zeppos_pypi_template

## Template project for pypi package projects
Creating a new pypi project should not be complicated. A few steps should be needed after you have 
setup your pypi account in either test pypi or production pypi.

## I. Get Started
### A. Dev environment
For the ease of use and development this project assume the following:
1. Windows 10 OS
2. PyCharm Dev environment

Note: This project documentation and scripts might have to be slightly adjusted for other:
 - OS  
 - dev environments
      
The intention is to add them as the user base might grow.

### B. Virtual Environment
To get started with this project and build it, you will need a virtual environment.
Execute the one of the scripts below. For now there is only the windows OS command script.
The intention is to add Linux and Mac/OS as we progress.

#### Windows 10
from the project root run in a windows CMD prompt type:
```
script\windows\build_virtual_env.bat
```

### C. PyPi-test
#### a. Create your account
Goto https://test.pypi.org/ and create your account

#### b. Create the token
- Login to https://test.pypi.org/ and create your token
- Click the down arrow next to your username on the right upper corner
- Select Account Settings
- Scroll down to the bottom of the account settings page. You will api_token area
- Create one.
- Save it in a secure place.

#### c. set the pypi.rc file
 
##### Windows 10
- Navigate to C:\windows\users\{your_user_account_name}\
- open or create the .pypirc
- it should look like this
```
distutils]
index-servers=
    testpypi

[testpypi]
repository: https://test.pypi.org/legacy/
username: __token__
password: pypi-AgEsN231dGVzd
```
- replace the "pypi-AgEsN231dGVzd" with your token you created at the pypi sight.
Note: this is a config for the "test pypi". You will need to adjust for production pypi.

## II. Deploy 
Deploying this project should not be hard. 


### 1. Change the ".env_project"
Change the .env_project content to meet your new project values

### 2. Deploy It
The intention is to use this command in a Jenkins "Freestyle project"

For now you will be deploying from your local dev environment executing the following command. 
Don't forget to do an other git check in of the ".env_package" after deployment as it will increment
the package version no.

### Windows Command Line
```
pipenv run python deploy.py
```

### PyCharm
Terminal Windows type:
```
python deploy.py
```

## II. Reference Material
PyPi Tutorial: https://packaging.python.org/tutorials/packaging-projects/