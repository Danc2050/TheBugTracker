# AutoBugTracker (Server Side)
> Updated: 7/25/2020

> NOTE: AutoBugTracker currently exists as two separate and distinct repositories. One, for the [client side](https://github.com/Danc2050/AutoBugLocal) and the other for the [server side](https://github.com/Danc2050/TheBugTracker). You're currently on the server side :smirk: :sunny: :ocean:.

## Contents
* [Description](#description)
	* [What is AutoBugTracker?](#what-is-autobugtracker)
	* [Why use AutoBugTracker?](#why-use-autobugtracker)
	* [Who should use AutoBugTracker?](#who-should-use-autobugtracker)
* [Instructions](#instructions)
    * [Client Side](#client-side-setup)
	    * [Setup](#setup-1)
	    * [Usage](#usage-1)
    * [Server Side](#server-side-setup)
        * [Setup](#setup-2)
        * [Usage](#usage-2)
* [Features](#features)
	* [Current](#current)
	* [Planned](#planned)
	* [Stretch Goals](#stretch-goals)
* [Contributors](#contributors)
	* [Product Owners / Sponsors](#product-owners--sponsors)
	* [Development Team](#development-team)

## Description
### What is AutoBugTracker?
AutoBugTracker is a python program that executes a client program, detects bugs, and filters bugs of your choosing. It then sends any bugs it encounters to a server where it, records, and reports the bugs to Github. AutoBugTracker utilizes a PostgreSQL database to help keep things organized and keeps team members updated on the status of bugs via email.

### Why use AutoBugTracker?
AutoBugTracker facilitates an efficient workflow for programmers, making it a great addition to any development suite.

### Who should use AutoBugTracker?
AutoBugTracker is valuable to developers working in large teams, that need the ability to accumulate a large quantity of debug information from their customers. AutoBugTracker is highly configurable and can be tailored for your teams specific needs.

## Instructions
### Client Side
#### Setup
Currently the AutoBugTracker client side repository can be cloned [here](https://github.com/Danc2050/AutoBugLocal).  
  
_Eventually we would like to set this up as a pip package._

#### Usage
AutoBugTracker can be run by using the command `python3 AutoBugLocal.py client-program`

---

### Server Side
#### Setup
1. Setting up a google vm instance:
    1. f1 micro 
    2. Allow http requests

2. Reserve a static IP address for the newly created VM instance

3. Open SSH command line for the newly create VM instance and enter the following commands
    1. `sudo apt-get install python-setuptools python-dev build-essential`
    2. `sudo apt-get install python3-pip`
    3. `sudo passwd` (set a new root password)
    4. `su root` (log into root with the password created from the step before)
    5. `sudo apt-get install docker.io`
    6. `docker run --rm --name postgresContainer -e POSTGRES_PASSWORD=my_secret_password -d -p 5432:5432 postgres`
    7. set environment variables in your `.bashrc` file
        1. `USERNAME=[EMAIL]`
        2. `PASSWORD=[PASSWORD]`
        3. `PYTHONPATH=[path-to-src]`
    8. install dependencies
        1. `pip3 install PyGithub`  
        2. `pip3 install psycopg2-binary`  
        3. `pip3 install yagmail`
    9. Run program with `python3 src/Server.py`
    10. Shut down server, update your config file located at `/root .autobug.ini`
    11. Start server back up with `python3 src/Server.py`

4. You should now be able to clone the server side [repo](https://github.com/Danc2050/TheBugTracker) to the VM instance via SSH.

##### Relevant Database Info

Database Name: `bug_tracker`  
Database Username: `postgres`  
Database Password: `my_secret_password`

##### Example (Default) Configuration File

```
{
    "first": "John",
    "last": "Doe",
    "email": "johndoe@doe.com",
    "create_debug_log": true,
    "overwrite_previous_entry": false,
    "log_file": "log.txt",
    "github_integration": false,
    "github_access_token": "",
    "github_repo_name": "",
    "send_email": true,
    "send_github_issue": false
}
```

##### Example Log File
If `create_debug_log` is set to true, AutoBugTracker will create a file for debugging purposes with a filename of `log_file`  
  
log.txt:  
```
2020-07-15 16:05:07 DEBUG    Error while connecting to PostgreSQL Section postgres_server not found on the C:\Users\*****\PycharmProjects\resource\Database.ini file 
2020-07-15 16:05:07 DEBUG    Could not create table connect() argument after ** must be a mapping, not NoneType
```

#### Usage
The **_server side_** is mostly automated! However, you can login to the server via SSH and:  
* Run the AutoBugTracker server side program with `python3 src/Server.py`.
* Update the configuration file at `/root .autobug.ini`.
* Manipulate the database.
* and end the program / shut the server down with `CTRL + C`.

## Features
### Current
* Execute client program and capture output of bugs (Client Side).
* Black-list filtering (Client Side).
* Allow customization of program settings via the use of configuration file/s (Server Side).
* Send emails (Server Side).
* Instantiate a PostgreSQL database (Server Side).
* Communicate with Github (Server Side).

### Planned
* Notify team members that bugs have been resolved via email automatically from remote server.

### Stretch Goals
* Alter config options at program execution via command line arguments.
* Capture bugs from programs written in more languages.
* Pip package.
* Formalize project. (Give it more professional layout features, i.e. `__main__.py`, `-help` command, etc.)
* Record user input to see what they did specifically when a bug occurred.

## Contributors
### Product Owners / Sponsors
> [:grin: Daniel Connelly](https://www.linkedin.com/in/dconnelly2/)  
> [:sweat_smile: Teal Dulcet](https://www.tealdulcet.com/)

### Development Team
#### Team Lead
> :joy: Antonio DiMaggio

#### Software Engineers
> :smirk: Ryan Campbell  
> :laughing: Ramon Guarnes  
> :grinning: Dana Khoshnaw  
> :blush: Princess Kim  
> :wink: Armando Lajara  
> :sunglasses: Mahmoud Al Robiai
