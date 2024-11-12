# Nginx On Centos 7 
Installing Nginx on CentOS 7 involves several steps, including adding the EPEL repository, installing the Nginx package, starting the service, and ensuring it starts automatically upon system reboot. Here's a step-by-step guide to get you started:

### Step 1: Add EPEL Repository

The Extra Packages for Enterprise Linux (EPEL) repository contains additional packages that are not included in the default CentOS repositories. Nginx is available in the EPEL repository.

First, install the `epel-release` package:

```bash
sudo yum install epel-release -y
```

### Step 2: Install Nginx

With the EPEL repository added, you can now install Nginx:

```bash
sudo yum install nginx -y
```

### Step 3: Start Nginx Service

After the installation is complete, start the Nginx service:

```bash
sudo systemctl start nginx
```

### Step 4: Enable Nginx to Start at Boot

To ensure that Nginx starts automatically whenever your system boots, enable it with the following command:

```bash
sudo systemctl enable nginx
```

### Step 5: Verify Nginx Installation

To verify that Nginx has been successfully installed and is running, open a web browser and navigate to `http://localhost`. You should see the default Nginx welcome page, indicating that the server is working correctly.

### Step 6: Secure Your Nginx Installation (Optional)

For production environments, it's highly recommended to secure your Nginx installation. One of the first steps is to disable the default welcome page and configure SSL/TLS for secure connections.

#### Disable Default Welcome Page

Edit the Nginx configuration file to disable the default welcome page:

```bash
sudo vi /etc/nginx/nginx.conf
```

Look for the `server` block that listens on port 80 and comment out or remove the `root` directive pointing to `/usr/share/nginx/html;`.

Save and close the file.

Restart Nginx to apply changes:

```bash
sudo systemctl restart nginx
```
