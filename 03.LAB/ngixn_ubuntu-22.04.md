# Nginx on Ununtu 22.04
Installing Nginx on Ubuntu 22.04 is a straightforward process that involves updating your system, installing the Nginx package, and then starting the service. Here's a step-by-step guide to get you started:

### Step 1: Update Your System

First, ensure your package lists and installed packages are up to date. Open a terminal and execute the following commands:

```bash
sudo apt update
sudo apt upgrade -y
```

### Step 2: Install Nginx

Next, install the Nginx web server package by running:

```bash
sudo apt install nginx -y
```

During the installation, you might be asked to confirm the installation of some additional packages required by Nginx. Press `Y` and then `Enter` to proceed.

### Step 3: Start Nginx Service

Once the installation is complete, start the Nginx service to begin serving web pages:

```bash
sudo systemctl start nginx
```

### Step 4: Enable Nginx to Start at Boot

To ensure that Nginx starts automatically whenever your system boots, enable it with the following command:

```bash
sudo systemctl enable nginx
```

### Step 5: Check Nginx Status

Verify that Nginx is running properly by checking its status:

```bash
sudo systemctl status nginx
```

You should see output indicating that the service is active (running).

### Step 6: Access Nginx in a Web Browser

At this point, Nginx is configured to serve documents from its default document root, which is `/var/www/html`. To test that everything is working, open a web browser and go to `http://Server_IP`. You should see the default Nginx welcome page, which confirms that Nginx is running correctly.

