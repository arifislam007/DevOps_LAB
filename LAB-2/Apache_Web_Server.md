## Apache Web Server On Linux
**Configure Apache Web Server on Centos-7**

- Setting up Apache Web Server on CentOS 7 involves several steps, including updating your system, installing Apache, starting the service, and ensuring it starts automatically upon system reboot. Below is a step-by-step guide tailored for beginners.

### Step 1: Update Your System

Before installing new software, it's a good practice to update your system's package list and upgrade all existing packages to their latest versions.

```bash
sudo yum update -y
```

### Step 2: Install Apache

CentOS uses `yum` as its package manager. You can install Apache by executing the following command:

```bash
sudo yum install httpd -y
```

### Step 3: Start Apache Service

After the installation is complete, you need to start the Apache service. This can be done with the following command:

```bash
sudo systemctl start httpd
```

### Step 4: Enable Apache to Start at Boot

To ensure that Apache starts automatically whenever your system boots, run:

```bash
sudo systemctl enable httpd
```

### Step 5: Verify Apache Installation

To verify that Apache has been successfully installed and is running, open a web browser and navigate to `http://localhost`. You should see the default Apache test page indicating that the server is working correctly.

### Step 6: Secure Your Apache Installation (Optional)

For production environments, it's highly recommended to secure your Apache installation. One of the first steps is to disable the default test page and change the default port if necessary.

#### Disable Default Test Page

Edit the Apache configuration file to disable the default test page:

```bash
sudo vi /etc/httpd/conf/httpd.conf
```

Find the line that says `Include conf.modules.d/*.conf` and add `LoadModule rewrite_module modules/mod_rewrite.so` below it if you plan to use URL rewriting.

Then, find the section `<Directory "/var/www/html">` and set `Options Indexes FollowSymLinks` and `AllowOverride All`.

Save and close the file.

Restart Apache to apply changes:

```bash
sudo systemctl restart httpd
```

#### Change Default Port (Optional)

If you want to change the default port (e.g., to 8080), edit the `httpd.conf` file again:

```bash
sudo vi /etc/httpd/conf/httpd.conf
```

Find the line that says `Listen 80` and change it to `Listen 8080`.

Also, adjust any firewall rules accordingly to allow traffic on the new port.

### Conclusion

You now have a basic Apache web server setup on CentOS 7. From here, you can start exploring more advanced configurations, such as setting up virtual hosts for different domains, enabling SSL/TLS for secure connections, and optimizing performance. Remember to regularly update your server and monitor its security to keep it safe and efficient.

Citations:

