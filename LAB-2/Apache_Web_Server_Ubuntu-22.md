# Apache Web Server On Ubuntu-22.04

Installing and configuring Apache on Ubuntu 22.04 is a straightforward process that involves updating your system, installing the Apache package, and then starting the service. Here's a step-by-step guide to get you started:

### Step 1: Update Your System

First, ensure your package lists and installed packages are up to date. Open a terminal and execute the following commands:

```bash
sudo apt update
sudo apt upgrade -y
```

### Step 2: Install Apache

Next, install the Apache web server package by running:

```bash
sudo apt install apache2 -y
```

During the installation, you might be prompted to choose the default web server. Since you're installing Apache, you can select it.

### Step 3: Start Apache Service

Once the installation is complete, start the Apache service to begin serving web pages:

```bash
sudo systemctl start apache2
```

### Step 4: Enable Apache to Start at Boot

To ensure that Apache starts automatically whenever your system boots, enable it with the following command:

```bash
sudo systemctl enable apache2
```

### Step 5: Check Apache Status

Verify that Apache is running properly by checking its status:

```bash
sudo systemctl status apache2
```

You should see output indicating that the service is active (running).

### Step 6: Access Apache in a Web Browser

At this point, Apache is configured to serve documents from its default document root, which is `/var/www/html`. To test that everything is working, open a web browser and go to `http://Server_IP`. You should see the Apache Ubuntu default page, which confirms that Apache is running correctly.

