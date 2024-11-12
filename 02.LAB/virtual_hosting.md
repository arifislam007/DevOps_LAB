# Apache Virtual Hosting on Rocky Linux 9

In this guide, we'll assume that Apache is already installed on your Rocky Linux 9 system. If you haven’t done so, install Apache first. Then, we'll walk through creating Apache Virtual Hosts, configuring root directories, adjusting firewall settings, and modifying the Listen port.

## Prerequisites

- Apache HTTP Server is already installed on your system.
- You have `sudo` privileges.
- Basic knowledge of using Linux commands.

## Step 1: Create Virtual Host Configuration Files

### **Create a Virtual Host Configuration File**

The Apache configuration files for virtual hosts are usually stored in the `/etc/httpd/conf.d/` directory. Let’s start by creating a configuration file for each website you want to host.

For example, let’s create a configuration file for the domain `example1.com`.

Run the following command to create the virtual host configuration file:

```bash
sudo nano /etc/httpd/conf.d/example1.com.conf
```

Inside this file, add the following content:

```apache
Listen 81
<VirtualHost *:81>
    ServerAdmin webmaster@example1.com
    DocumentRoot /var/www/example1.com/public_html
    ServerName example1.com
    ErrorLog /var/log/httpd/example1.com_error.log
    CustomLog /var/log/httpd/example1.com_access.log combined
</VirtualHost>
```

In this configuration:
- **ServerAdmin**: Defines the email address of the website administrator.
- **DocumentRoot**: Specifies the root directory for the website files.
- **ServerName**: The domain name that Apache will listen for (e.g., `example1.com`).
- **ErrorLog and CustomLog**: Log files to store errors and access logs for this virtual host.

### **Create Another Virtual Host for a Second Domain**

Repeat the above steps to create another virtual host for `example2.com` by running:

```bash
sudo nano /etc/httpd/conf.d/example2.com.conf
```

Add the following content:

```apache
Listen 82
<VirtualHost *:82>
    ServerAdmin webmaster@example2.com
    DocumentRoot /var/www/example2.com/
    ServerName example2.com
    ErrorLog /var/log/httpd/example2.com_error.log
    CustomLog /var/log/httpd/example2.com_access.log combined
</VirtualHost>
```

## Step 2: Create Document Root Directories

Each website needs its own document root directory, where the site files will be stored. Let's create directories for both `example1.com` and `example2.com`.

```bash
sudo mkdir -p /var/www/example1.com
sudo mkdir -p /var/www/example2.com
```

### Set Permissions for the Document Root Directories

Ensure the Apache user has the appropriate permissions to access these directories:

```bash
sudo chown -R apache:apache /var/www/example1.com
sudo chown -R apache:apache /var/www/example2.com
```

Now, you can place your website files (e.g., `index.html`) inside the respective `public_html` directories.

## Step 3: Adjust Firewall to Allow HTTP Traffic

If your server uses `firewalld`, you need to allow HTTP traffic (port 80) through the firewall. Use the following commands:

```bash
firewall-cmd --permanent --add-port=81/tcp
firewall-cmd --permanent --add-port=81/tcp
firewall-cmd --permanent --add-port=82/tcp
firewall-cmd --permanent --add-port=82/tcp.
firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```
This will allow incoming connections on both HTTP Port 80, 81, 82

## Step 5: Create Test HTML Files

For each domain, create a simple HTML file to confirm everything is working.

For `example1.com`, create a test page:

```bash
echo "<html><body><h1>Welcome to example1.com</h1></body></html>" | sudo tee /var/www/example1.com/index.html
```

For `example2.com`, create a test page:

```bash
echo "<html><body><h1>Welcome to example2.com</h1></body></html>" | sudo tee /var/www/example2.com/index.html
```

## Step 6: Restart Apache to Apply Changes

After making all the changes, restart Apache to apply the virtual host configurations:

```bash
sudo systemctl restart httpd
```

## Step 7: Test the Configuration

Finally, test the configuration by opening your browser and visiting:

- `http://<serverIP>:81`
- `http://<serverIP>:81`

If everything is set up correctly, you should see the test pages for both sites.
