# HAProxy Configuration Guide

## Overview

HAProxy (High Availability Proxy) is a free, open-source software that provides a high availability load balancer and proxy server for TCP and HTTP-based applications. This guide will help you understand and configure HAProxy effectively.

## Configuration File Structure

The HAProxy configuration file is typically located at `/etc/haproxy/haproxy.cfg`. It is divided into several main sections:

### 1. Global Section

The global section defines process-wide parameters that affect HAProxy's overall behavior.

```
global
    # Process management
    user haproxy
    group haproxy
    daemon

    # Logging
    log 127.0.0.1 local0
    log 127.0.0.1 local1 notice

    # Performance tuning
    maxconn 4096
    nbproc 1
    spread-checks 5

    # SSL/TLS settings
    ssl-default-bind-ciphers PROFILE=SYSTEM
    ssl-default-server-ciphers PROFILE=SYSTEM
```

Key global parameters:
- `user` and `group`: Defines the user and group under which HAProxy runs
- `daemon`: Runs HAProxy in background
- `log`: Configures logging destinations
- `maxconn`: Maximum number of concurrent connections
- `nbproc`: Number of processes to spawn
- `spread-checks`: Spreads health checks to prevent simultaneous checks

### 2. Defaults Section

The defaults section sets default parameters for all other configurations.

```
defaults
    mode http                  # Default mode (can be tcp)
    log global                 # Use global logging configuration
    option httplog             # Log HTTP requests
    option dontlognull         # Don't log health check requests
    option forwardfor          # Add X-Forwarded-For header
    option http-server-close   # Enable keep-alive
    
    # Timeouts
    timeout connect 10s
    timeout client 30s
    timeout server 30s

    # Retry configuration
    retries 3
    maxconn 3000
```

Important default parameters:
- `mode`: Defines the proxy mode (HTTP or TCP)
- `timeout` settings: Control connection and request timeouts
- `retries`: Number of connection attempts
- `maxconn`: Maximum connections per backend

### 3. Frontend Configuration

Frontends define how incoming connections are received and processed.

```
frontend http-frontend
    bind *:80
    bind *:443 ssl crt /path/to/certificate.pem
    
    # ACL and routing rules
    acl is_web_domain hdr(host) -i www.example.com
    acl is_api_domain hdr(host) -i api.example.com

    # Routing rules
    use_backend web-servers if is_web_domain
    use_backend api-servers if is_api_domain
    default_backend web-servers
```

Frontend configuration components:
- `bind`: Specifies IP and port to listen on
- `acl`: Access Control Lists for routing
- `use_backend`: Directs traffic to specific backend servers

### 4. Backend Configuration

Backends define server pools that handle requests.

```
backend web-servers
    balance roundrobin
    option httpchk HEAD / HTTP/1.1\r\nHost:\ www.example.com
    
    server web1 10.0.0.1:8080 check
    server web2 10.0.0.2:8080 check backup
    server web3 10.0.0.3:8080 check

backend api-servers
    balance leastconn
    option httpchk GET /health HTTP/1.1\r\nHost:\ api.example.com
    
    server api1 10.0.0.4:8080 check
    server api2 10.0.0.5:8080 check backup
```

Backend configuration key points:
- `balance`: Load balancing algorithm
- `option httpchk`: Health check method
- `server`: Individual server configurations
- `check`: Enable health checks
- `backup`: Backup server configuration

### 5. Health Checks

HAProxy supports various health check methods:

```
backend app-servers
    option httpchk GET /health
    http-check expect status 200
    
    server app1 10.0.0.1:8080 check inter 5s rise 2 fall 3
```

Health check parameters:
- `inter`: Check interval
- `rise`: Consecutive successful checks to mark server up
- `fall`: Consecutive failed checks to mark server down

## Best Practices

1. Always use SSL/TLS for production
2. Implement proper logging
3. Configure health checks
4. Use ACLs for advanced routing
5. Implement timeouts
6. Monitor HAProxy performance

## Debugging and Monitoring

Use these tools for HAProxy management:
- `haproxy -c -f /etc/haproxy/haproxy.cfg`: Configuration check
- `systemctl status haproxy`: Service status
- `socat /var/run/haproxy.stats stdio`: Runtime stats

## Example Complete Configuration

A minimal working configuration combining all sections:

```
global
    user haproxy
    group haproxy
    daemon

defaults
    mode http
    timeout connect 10s
    timeout client 30s
    timeout server 30s

frontend http-in
    bind *:80
    default_backend servers

backend servers
    balance roundrobin
    server server1 10.0.0.1:8080 check
    server server2 10.0.0.2:8080 check
```
