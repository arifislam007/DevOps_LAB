Here’s a step-by-step guide to installing Grafana on Rocky Linux 9:

### Step 1: Update System Packages
Ensure your system packages are up-to-date.

```bash
sudo dnf update -y
```

### Step 2: Add Grafana Repository
Create a new repository file for Grafana.

```bash
sudo nano /etc/yum.repos.d/grafana.repo
```

Add the following content to the file:

```ini
[grafana]
name=grafana
baseurl=https://rpm.grafana.com
repo_gpgcheck=1
enabled=1
gpgcheck=1
gpgkey=https://rpm.grafana.com/gpg.key
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
exclude=*beta*
```

### Step 3: Install Grafana
Now, install Grafana using the following command:

```bash
sudo dnf install grafana -y
```

### Step 4: Start and Enable Grafana Service
After the installation is complete, start the Grafana service and enable it to run at boot.

```bash
sudo systemctl start grafana-server
sudo systemctl enable grafana-server
```

### Step 5: Configure Firewall (if necessary)
If you have a firewall enabled, open port `3000` for Grafana.

```bash
sudo firewall-cmd --zone=public --add-port=3000/tcp --permanent
sudo firewall-cmd --reload
```

### Step 6: Access Grafana Web Interface
Grafana runs on port `3000` by default. Open a web browser and go to:

```
http://<your_server_ip>:3000
```

### Step 7: Log in to Grafana
The default login credentials are:
- **Username:** `admin`
- **Password:** `admin`

You will be prompted to change the password upon the first login.

### Step 8: Verify Installation
Once logged in, you can verify that Grafana is running properly and start configuring your dashboards and data sources.

That's it! You now have Grafana installed and running on Rocky Linux 9.
