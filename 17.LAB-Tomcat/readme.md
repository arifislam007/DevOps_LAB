
```markdown
# Apache Tomcat Installation on Rocky Linux 9

## Environment Specification

We are using a minimal installed Rocky Linux 9 virtual machine with the following specifications:

- **CPU**: 3.4 GHz (2 cores)
- **Memory**: 2 GB
- **Storage**: 20 GB
- **Operating System**: Rocky Linux release 9

## Update Your Rocky Linux Server

1. **Log in** to your Linux server as `root` using an SSH client.
   
2. Set a Fully Qualified Domain Name (FQDN) for your server:
   ```bash
   # hostnamectl set-hostname tomcat.somthing.com
   ```

3. Refresh your `dnf` cache:
   ```bash
   # dnf makecache
   ```

4. Upgrade software packages:
   ```bash
   # dnf update -y
   ```

   > Note: If the kernel is upgraded, reboot the system:
   ```bash
   # reboot
   ```

5. Verify OS and kernel versions:
   ```bash
   # cat /etc/rocky-release
   Rocky Linux release 9.1 (Blue Onyx)

   # uname -r
   5.14.0-162.6.1.el9_1.0.1.x86_64
   ```

## Install Apache Tomcat Prerequisites

1. Install necessary tools:
   ```bash
   # dnf install -y wget tar gzip
   ```

2. Install OpenJDK 17:
   ```bash
   # dnf install -y java-17-openjdk
   ```

3. Verify Java installation:
   ```bash
   # java --version
   openjdk 17.0.8 2023-07-18 LTS
   OpenJDK Runtime Environment (Red_Hat-17.0.8.0.7-2.el9_1) (build 17.0.8+7-LTS)
   OpenJDK 64-Bit Server VM (Red_Hat-17.0.8.0.7-2.el9_1) (build 17.0.8+7-LTS, mixed mode, sharing)
   ```

## Install Apache Tomcat on Rocky Linux 9

1. Download and extract Apache Tomcat:
   ```bash
   # cd /tmp
   # wget https://dlcdn.apache.org/tomcat/tomcat-10/v10.0.27/bin/apache-tomcat-10.0.27.tar.gz
   # mkdir /opt/tomcat
   # tar xf apache-tomcat-10.0.27.tar.gz -C /opt/tomcat --strip-components=1
   ```

2. Create a `tomcat` user:
   ```bash
   # useradd -r -d /opt/tomcat/ -s /sbin/nologin -c "Tomcat User" tomcat
   # chown -R tomcat:tomcat /opt/tomcat/
   ```

## Configure Apache Tomcat

1. **Set up admin users**:
   ```bash
   # vi /opt/tomcat/conf/tomcat-users.xml
   ```
   Add the following:
   ```xml
   <role rolename="admin-gui"/>
   <role rolename="manager-gui"/>
   <user username="admin" password="admin" roles="admin-gui,manager-gui"/>
   ```

2. **Allow external access**:
   Edit the `context.xml` files in both `manager` and `host-manager` directories:
   ```bash
   # vi /opt/tomcat/webapps/manager/META-INF/context.xml
   # vi /opt/tomcat/webapps/host-manager/META-INF/context.xml
   ```
   Comment out the `RemoteAddrValve` to allow access from other machines.

## Create Systemd Service for Tomcat

1. Create a systemd unit file:
   ```bash
   # vi /usr/lib/systemd/system/tomcat.service
   ```

   Add the following content:
   ```ini
   [Unit]
   Description=Apache Tomcat Server
   After=syslog.target network.target

   [Service]
   Type=forking
   User=tomcat
   Group=tomcat
   Environment=CATALINA_PID=/opt/tomcat/temp/tomcat.pid
   Environment=CATALINA_HOME=/opt/tomcat
   Environment=CATALINA_BASE=/opt/tomcat
   ExecStart=/opt/tomcat/bin/catalina.sh start
   ExecStop=/opt/tomcat/bin/catalina.sh stop
   RestartSec=10
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

2. **Reload systemd**, enable and start Tomcat service:
   ```bash
   # systemctl daemon-reload
   # systemctl enable --now tomcat.service
   ```

3. Verify the status of Tomcat:
   ```bash
   # systemctl status tomcat.service
   ```

You now have Apache Tomcat running on Rocky Linux 9 with Java 17.
```
