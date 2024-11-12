Setting up virtual hosting on NGINX in Rocky Linux allows multiple websites to be hosted on a single server with different domain names. Here’s a step-by-step guide to help you configure it.

### Step 1: Install NGINX
If not already installed, you can install NGINX with the following command:
```bash
sudo dnf install nginx -y
```

### Step 2: Configure NGINX for Virtual Hosting

1. **Create Directory Structures for Each Site**  
   Create separate directories for each site. For example:
   ```bash
   sudo mkdir -p /var/www/site1
   sudo mkdir -p /var/www/site2
   ```

2. **Set Ownership and Permissions**  
   Assign ownership of the directories to the NGINX user for security:
   ```bash
   sudo chown -R nginx:nginx /var/www/site1
   sudo chown -R nginx:nginx /var/www/site2
   ```
   Also, set the necessary permissions:
   ```bash
   sudo chmod -R 755 /var/www
   ```

3. **Create Sample Index Pages for Each Site**  
   For testing, you can create sample HTML files for each website:
   ```bash
   echo "<h1>Welcome to site1.com!</h1>" | sudo tee /var/www/site1/index.html
   echo "<h1>Welcome to site2.com!</h1>" | sudo tee /var/www/site2/index.html
   ```

4. **Configure Server Blocks (Virtual Hosts)**  
   Now, create configuration files for each site in `/etc/nginx/conf.d/`.

   For **site1.com**:
   ```bash
   sudo nano /etc/nginx/conf.d/site1.conf
   ```
   Add the following configuration:
   ```nginx
   server {
       listen 8081;
       server_name site1.com www.site1.com;

       root /var/www/site1;
       index index.html;

       location / {
           try_files $uri $uri/ =404;
       }
   }
   ```

   For **site2.com**:
   ```bash
   sudo nano /etc/nginx/conf.d/site2.conf
   ```
   Add the following configuration:
   ```nginx
   server {
       listen 8082;
       server_name site2.com www.site2.com;

       root /var/www/site2;
       index index.html;

       location / {
           try_files $uri $uri/ =404;
       }
   }
   ```

5. **Test the NGINX Configuration**  
   Check for any syntax errors in the NGINX configuration:
   ```bash
   sudo nginx -t
   ```
   If the configuration test is successful, you should see a message like "syntax is ok" and "test is successful."

6. **Reload NGINX**  
   Apply the new configuration:
   ```bash
   sudo systemctl restart nginx
   ```

### Step 4: Test Your Setup
After DNS propagation, you should be able to visit `http://ServerIP:8081` and `http://ServerIP:8081` and see the respective content.
