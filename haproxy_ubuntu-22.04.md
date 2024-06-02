# HAProxy on Ubuntu 22.04
Configuring HAProxy as a load balancer involves several steps, including installing HAProxy, editing its configuration file to define backend servers and load-balancing algorithms, and finally starting the HAProxy service. Below is a step-by-step guide to get you started on Ubuntu 22.04, but these steps are generally applicable to most Linux distributions with minor adjustments.

### Step 1: Update Your System

First, ensure your package lists and installed packages are up to date. Open a terminal and execute the following commands:

```bash
sudo apt update
sudo apt upgrade -y
```

### Step 2: Install HAProxy

Next, install the HAProxy package by running:

```bash
sudo apt install haproxy -y
```

### Step 3: Edit HAProxy Configuration File

HAProxy's main configuration file is typically located at `/etc/haproxy/haproxy.cfg`. Before making changes, it's a good idea to back up the original file:

```bash
sudo cp /etc/haproxy/haproxy.cfg /etc/haproxy/haproxy.cfg.bak
```

Now, open the configuration file with your preferred text editor, such as nano:

```bash
sudo nano /etc/haproxy/haproxy.cfg
```

Below is a basic example of what the configuration might look like for a simple load balancer setup:

```haproxy
global
    log /dev/log    local0
    log /dev/log    local1 notice
    daemon

defaults
    log     global
    mode    http
    option  httplog
    option  dontlognull
    timeout connect 5000ms
    timeout client  50000ms
    timeout server  50000ms

frontend http_front
    bind *:80
    stats uri /haproxy?stats
    default_backend http_back

backend http_back
    balance roundrobin
    server server1 192.168.1.101:80 check
    server server2 192.168.1.102:80 check
```

In this example:
- `bind *:80` tells HAProxy to listen on port 80 for incoming connections.
- `stats uri /haproxy?stats` enables the statistics page, accessible at `http://your-haproxy-ip/haproxy?stats`.
- `balance roundrobin` specifies the load-balancing algorithm. Other options include `leastconn` and `source`.
- `server server1 192.168.1.101:80 check` and `server server2 192.168.1.102:80 check` define the backend servers. Replace the IP addresses and ports with those of your actual backend servers.

### Step 4: Restart HAProxy

After editing the configuration file, restart HAProxy to apply the changes:

```bash
sudo systemctl restart haproxy
```

### Step 5: Verify HAProxy Configuration

You can verify that HAProxy is running and listening on the correct port with:

```bash
sudo netstat -tuln | grep :80
```

And you can access the HAProxy statistics page at `http://your-haproxy-ip/haproxy?stats` to see real-time information about the load balancing.
