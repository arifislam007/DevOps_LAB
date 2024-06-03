# LAMP on Centos-7 Linux
This is a simple LAMP Stack for understandin application
**Now Follow the process:**
- Install apache 
``` bash
    yum install -y httpd
    systemctl start httpd
    systemctl enable httpd
```

#Install PHP:
yum install -y php php-fpm php-cli php-curl php-mysqlnd php-mbstring php-devel
systemctl restart httpd
#Download code from this git repository and keep the code /var/www/html/ #Change db server address from config.php file

Create EC2 for Mariadb Server with Amazon Linux 2
#Install Mariadb server on it.
yum install mariadb-server -y
systemctl start mariadb
systemctl status mariadb
systemctl enable mariadb

#Set your mariadb root passowrd and user for your databases
#Run the following command and go as per guide:
mysql_secure_installation
#Now login to database with root and run the following command
create database demo
GRANT ALL PRIVILEGES ON demo.* TO 'admin'@'%%' identified by 'admin123';

#create file name demo.sql with the following sql content: CREATE TABLE employees (
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(100) NOT NULL,
address VARCHAR(255) NOT NULL,
salary INT(10) NOT NULL );
#Now import Mysql dump file that you created demo.sql
mysql -u admin -p demo < dump.sql

#All set for databse.

#After create 2 VM now download this git code to Web Ec2
