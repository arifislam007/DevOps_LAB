# step-by-step guide to installing and configuring **PostgreSQL 16** on **AlmaLinux** with a custom data directory at `/data/pgdata/16/data`.

---

## **Step 1: Update System Packages**
```bash
sudo dnf update -y
```

---

## **Step 2: Install PostgreSQL 16**
1. Enable the PostgreSQL repository:
   ```bash
   sudo dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-9-x86_64/pgdg-redhat-repo-latest.noarch.rpm
   ```
2. Disable the built-in PostgreSQL module:
   ```bash
   sudo dnf -qy module disable postgresql
   ```
3. Install PostgreSQL 16:
   ```bash
   sudo dnf install -y postgresql16 postgresql16-server
   ```

---

## **Step 3: Create a Custom Data Directory**
1. Create the new directory:
   ```bash
   sudo mkdir -p /data/pgdata/16/data
   ```
2. Set the correct permissions:
   ```bash
   sudo chown -R postgres:postgres /data/pgdata/16
   sudo chmod 700 /data/pgdata/16/data
   ```

---

## **Step 4: Initialize PostgreSQL with the Custom Directory**
1. Switch to the PostgreSQL user:
   ```bash
   sudo su - postgres
   ```
2. Initialize the database:
   ```bash
   /usr/pgsql-16/bin/initdb -D /data/pgdata/16/data
   ```
3. Exit the `postgres` user:
   ```bash
   exit
   ```

---

## **Step 5: Configure PostgreSQL to Use the New Data Directory**
1. Edit the **systemd** service file:
   ```bash
   sudo nano /usr/lib/systemd/system/postgresql-16.service
   ```
2. Find the following line:
   ```
   Environment=PGDATA=/var/lib/pgsql/16/data/
   ```
   Change it to:
   ```
   Environment=PGDATA=/data/pgdata/16/data
   ```
3. Reload the systemd daemon:
   ```bash
   sudo systemctl daemon-reload
   ```

---

## **Step 6: Start and Enable PostgreSQL**
```bash
sudo systemctl enable --now postgresql-16
```

---

## **Step 7: Verify PostgreSQL**
1. Check the status:
   ```bash
   sudo systemctl status postgresql-16
   ```
2. Connect to PostgreSQL:
   ```bash
   sudo -u postgres psql
   ```
   Run the following query to confirm:
   ```sql
   SHOW data_directory;
   ```
   It should return `/data/pgdata/16/data`.

---

## **Step 8: Allow Remote Connections (Optional)**
1. Edit the **PostgreSQL configuration file**:
   ```bash
   sudo nano /data/pgdata/16/data/postgresql.conf
   ```
   Find `listen_addresses` and set:
   ```
   listen_addresses = '*'
   ```
2. Edit **pg_hba.conf** to allow remote access:
   ```bash
   sudo nano /data/pgdata/16/data/pg_hba.conf
   ```
   Add the following line at the end:
   ```
   host    all             all             0.0.0.0/0               md5
   ```
3. Restart PostgreSQL:
   ```bash
   sudo systemctl restart postgresql-16
   ```

---

### **PostgreSQL 16 is now running with the custom data directory `/data/pgdata/16/data` on AlmaLinux! 🚀**
