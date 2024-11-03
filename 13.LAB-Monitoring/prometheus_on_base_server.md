# step-by-step guide to installing and configuring Prometheus on Rocky Linux 9:

### Step 1: Update System Packages
Update the system packages to ensure everything is up-to-date.

```bash
sudo dnf update -y
```

### Step 2: Create a Prometheus User
Create a dedicated user to run Prometheus without root privileges.

```bash
sudo useradd --no-create-home --shell /bin/false prometheus
```

### Step 3: Download Prometheus
Go to the [Prometheus download page](https://prometheus.io/download/) and get the latest stable version URL. Download it using `wget`.

```bash
cd /tmp
wget https://github.com/prometheus/prometheus/releases/download/v2.41.0/prometheus-2.41.0.linux-amd64.tar.gz
```

### Step 4: Extract the Downloaded Archive
Extract the downloaded tar file.

```bash
tar xvf prometheus-*.tar.gz
```

Rename the extracted folder for easier management:

```bash
mv prometheus-2.41.0.linux-amd64 prometheus
```

### Step 5: Move Prometheus Binaries and Set Permissions
Move the Prometheus binaries to `/usr/local/bin` and set the correct ownership.

```bash
sudo mv prometheus/prometheus /usr/local/bin/
sudo mv prometheus/promtool /usr/local/bin/
```

Create necessary directories and move configuration files.

```bash
sudo mkdir /etc/prometheus
sudo mkdir /var/lib/prometheus
sudo mv prometheus/consoles /etc/prometheus
sudo mv prometheus/console_libraries /etc/prometheus
sudo mv prometheus/prometheus.yml /etc/prometheus
```

Set ownership for the Prometheus directories:

```bash
sudo chown -R prometheus:prometheus /etc/prometheus /var/lib/prometheus
sudo chown prometheus:prometheus /usr/local/bin/prometheus /usr/local/bin/promtool
```

### Step 6: Configure Prometheus
Open the main configuration file, `prometheus.yml`, to define targets and other settings.

```bash
sudo nano /etc/prometheus/prometheus.yml
```

By default, Prometheus will scrape itself. You can add targets here if needed, for example:

```yaml
# Example Prometheus configuration
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'node_exporter'
    static_configs:
      - targets: ['localhost:9100']
```

Save and close the file.

### Step 7: Create a Systemd Service for Prometheus
Create a service file for Prometheus so it can run as a system service.

```bash
sudo nano /etc/systemd/system/prometheus.service
```

Add the following configuration:

```ini
[Unit]
Description=Prometheus Monitoring
Wants=network-online.target
After=network-online.target

[Service]
User=prometheus
Group=prometheus
Type=simple
ExecStart=/usr/local/bin/prometheus \
  --config.file=/etc/prometheus/prometheus.yml \
  --storage.tsdb.path=/var/lib/prometheus/ \
  --web.console.templates=/etc/prometheus/consoles \
  --web.console.libraries=/etc/prometheus/console_libraries

[Install]
WantedBy=multi-user.target
```

Save and close the file.

### Step 8: Start and Enable the Prometheus Service
Reload systemd to recognize the new service, then start and enable Prometheus.

```bash
sudo systemctl daemon-reload
sudo systemctl start prometheus
sudo systemctl enable prometheus
```

### Step 9: Verify Prometheus is Running
Check the status of the Prometheus service.

```bash
sudo systemctl status prometheus
```

### Step 10: Access Prometheus Web Interface
By default, Prometheus runs on port `9090`. Open a web browser and go to:

```
http://<your_server_ip>:9090
```

### Step 11: Configure Firewall (if necessary)
If you have a firewall enabled, open port `9090` for Prometheus.

```bash
sudo firewall-cmd --zone=public --add-port=9090/tcp --permanent
sudo firewall-cmd --reload
```

Prometheus should now be accessible, and you can start monitoring metrics!
