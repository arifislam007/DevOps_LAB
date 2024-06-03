# LAMP on Centos -7 for a custom Application

##To set up a PHP repository on CentOS 7 and install PHP along with its dependencies, follow these steps, incorporating guidance from the provided sources:

### Step 1: Install Required Packages

First, you need to install the `yum-utils` package and enable the EPEL (Extra Packages for Enterprise Linux) repository, which provides additional packages beyond what is available in the default CentOS repositories.

```bash
sudo yum install yum-utils -y
sudo yum install epel-release -y
```

### Step 2: Add Remi's Repository

Remi's repository offers newer versions of PHP compared to the default CentOS repositories. To add Remi's repository, execute the following command:

```bash
sudo yum install http://rpms.remirepo.net/enterprise/remi-release-7.rpm
```

### Step 3: Enable PHP Repository

Choose the PHP version you want to install. For example, to enable PHP 7.2, use the following command:

```bash
sudo yum-config-manager --enable remi-php72
```

If you prefer another version, replace `remi-php72` with `remi-php71` for PHP 7.1 or `remi-php73` for PHP 7.3.

### Step 4: Install PHP and Common Extensions

Now, install PHP along with some common extensions. Adjust the command based on the PHP version you chose in the previous step.

```bash
sudo yum install php php-common php-opcache php-mcrypt php-cli php-gd php-curl php-mysql -y
```

### Step 5: Verify PHP Installation

Check the installed PHP version to ensure the installation was successful:

```bash
php -v
```

---
**Now Configure Mysql and Apache**

### Step 1: Update Package Repository Cache

Before beginning, ensure your CentOS 7 server's package repository cache is up to date:

```bash
sudo yum update
```

### Step 2: Install the Apache Web Server

Apache serves as the web server component of the LAMP stack.

1. Install Apache:

```bash
sudo yum install httpd
```

2. Start the Apache service:

```bash
sudo systemctl start httpd.service
```

3. Enable Apache to start at boot:

```bash
sudo systemctl enable httpd.service
```

### Step 3: Install MySQL (MariaDB) and Create a Database

MariaDB acts as the database component, serving as a drop-in replacement for MySQL.

1. Install MariaDB:

```bash
sudo yum install mariadb-server mariadb
```

2. Start the MariaDB service:

```bash
sudo systemctl start mariadb
```

### Step 4: Secure Your MySQL Installation

It's crucial to secure your MariaDB installation by running the security script.

```bash
sudo mysql_secure_installation
```

Follow the prompts to set a root password, remove anonymous users, disallow root login remotely, remove the test database, and reload privilege tables.

### Step 6: Import Demo Database Schema 
- Create a database name demo
```bash
mysql -u root -p
create database demo;
quit
```

- Improt database schama
``` bash
mysql -u root -p demo < ./mysql-db/dump.sql

```
- Restart the Apache service to enable PHP processing:

```bash
sudo systemctl restart httpd.service
```

### Step 6: Test PHP Processing

To verify PHP is working correctly, create a simple PHP file.

1. Install the Nano text editor if it's not already installed:

```bash
sudo yum install nano
```

2. Create a PHP info file:

```bash
sudo vi /var/www/html/info.php
```

Paste the following PHP code into the file:

```php
<?php
phpinfo();
?>
```


3. Access the file from your web browser by navigating to `http://your_server_ip/info.php`. Replace `your_server_ip` with your server's actual IP address. If PHP is configured correctly, you'll see a webpage displaying PHP information.

### Step 8: Keep Code In Appache Defalut Location
``` bash
cp php-code /var/www/html/app
```

### Step 9: Restart Apache

After installing new PHP modules or making significant changes, restart Apache to apply them:

```bash
sudo systemctl restart httpd.service
```

