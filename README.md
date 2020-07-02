# AutoBugTracker
> Updated: 7/1/2020

## Contents
* [Description](#description)
	* [What is AutoBugTracker?](#what-is-autobugtracker)
	* [Why use AutoBugTracker?](#why-use-autobugtracker)
	* [Who should use AutoBugTracker?](#who-should-use-autobugtracker)
* [Instructions](#instructions)
	* [Installation](#installation)
	* [Usage](#usage)
* [Features](#features)
	* [Current](#current)
	* [Planned](#planned)
	* [Stretch Goals](#stretch-goals)
* [Contributors](#contributors)
	* [Product Owners / Sponsors](#product-owners--sponsors)
	* [Development Team](#development-team)

## Description
### What is AutoBugTracker?
AutoBugTracker is a python program that executes a client program and reports any bugs it encounters to a server, it then filters, records, and reports the bugs to Github. AutoBugTracker utilizes a PostgreSQL database to help keep things organized and keeps team members updated on the status of bugs via email.

### Why use AutoBugTracker?
AutoBugTracker facilitates an efficient workflow for programmers, making it a great addition to any development suite.

### Who should use AutoBugTracker?
AutoBugTracker is valuable to developers of a variety of team sizes with an emphasis on solo devs and small teams. Regardless of team size, AutoBugTracker is highley configurable and can be tailored for your specific needs.

## Instructions
### Installation
Currently the AutoBugTracker repository can be [cloned](https://github.com/ismustachio/TheBugTracker.git).
_Eventually we would like to setup a pip package._

### Usage
AutoBugTracker can be run by using the command `python3 AutoBugTracker.py client-program`

Database Name: `bug_tracker`
Database Username: `postgres`
Database Password: `my_secret_password`

## Features
### Current
* Execute client program and capture output of bugs.
* Allow customization of program settings via the use of configuration file/s.
* Send emails.
* Instantiate a PostgreSQL database.
* Communicate with Github.
* Black-list filtering.

### Planned
* Black-list filtering from remote server.
* Update team Github repository from remote server.
* Notify team members that bugs have been submitted or resolved via email automatically from remote server.
* Transfer database to remote server.

### Stretch Goals
* Alter config options at program execution via command line arguments.
* Capture bugs from programs written in more languages.
* Pip package.
* Formalize project. (Give it more professional layout features, i.e. `__main__.py`, `-help` command, etc.)
* Record user input to see what they did specifically when a bug occured.

## Contributors
### Product Owners / Sponsors
> [Daniel Connelly](https://www.linkedin.com/in/dconnelly2/)
> [Teal Dulcet](https://www.tealdulcet.com/)

### Development Team
#### Team Lead
> Antonio DiMaggio

#### Software Engineers
> Ryan Campbell
> Ramon Guarnes
> Dana Khoshnaw
> Princess Kim
> Armando Lajara
> Mahmoud Al Robiai
