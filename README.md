Log Analysis Project
### Done by Tirunagari Divya Sree



## About Project:

-->In this project we displays the required data by using sql queries.
-->In this we take data from the database.
-->We use `psycopg2` module to connect to the database.


## Required Tools:
        
		By using the links we can install the tools
1* Python
2* Vagrant (https://www.vagrantup.com/) , Vagrantfile (https://github.com/udacity/fullstack-nanodegree-vm)
3* VirtualBox (https://www.virtualbox.org/wiki/Downloads)


## Files in the project:

   This project consists for the following files:

a) newlog.py - main file to run this project.
b) View.sql - It contains views which we use in main(newlog.py) file.
c) README.md - step by step instructions.
d) newsdata.sql - database file from where we get data.
f) result.PNG-output of a project.




## How to Install
** Install Vagrant & VirtualBox
** Clone the Udacity Vagrantfile
** Go to Vagrant directory and either clone this repo or download and place zip here
** Next do (`vagrant up`)
** Next (`vagrant ssh`)
** Navigate to `cd /vagrant` as instructed in terminal

## How to Run Project

Download the project zip file and unzip the file then place.

  ##open the folder and type cmd in the url.it displays a command prompt.

  1: Now do (`Vagrant up`) 
  
  
  2: Next do (`vagrant ssh`)
  
  
  3: download database (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

  4: Unzip this file after downloading it. The file inside is called newsdata.sql.

  5: Copy the newsdata.sql file and place inside the folder.
`.

  6:Now change the directory:
			here are some steps:
			 ##cd ..
			 ##cd ..
			 ##cd vagrant
  7:Now check the list of files using `ls`	

  8: Load the data in local database using the command:

  ```
    $ psql -d news -f newsdata.sql
  ```
   8: Run newlog.py using:
  ```
    $ python newlog.py
  ```
 

