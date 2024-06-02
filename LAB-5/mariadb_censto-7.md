Installing MariaDB on CentOS 7 involves several steps, including adding the MariaDB repository, installing the MariaDB package, starting the service, and ensuring it starts automatically upon system reboot. Here's a step-by-step guide to get you started:

### Step 1: Add MariaDB Repository

MariaDB maintains its own repository for CentOS/RHEL systems. First, you need to download and install the MariaDB repository package:

```bash
wget https://downloads.mariadb.org/mariadb/repositories/CentOS_7/$basearch/maria/db/10.6/rpm/centos7-x86_64/mariadb100u-centos7-x86_64.rpm
sudo rpm -ivh mariadb100u-centos7-x86_64.rpm
```

Replace `$basearch` with your architecture (usually `x86_64`). This command downloads the MariaDB 10.6 repository RPM and installs it.

### Step 2: Install MariaDB

After adding the repository, you can install MariaDB:

```bash
sudo yum install MariaDB-server MariaDB-client -y
```

### Step 3: Start MariaDB Service

Once the installation is complete, start the MariaDB service:

```bash
sudo systemctl start mariadb
```

### Step 4: Enable MariaDB to Start at Boot

To ensure that MariaDB starts automatically whenever your system boots, enable it with the following command:

```bash
sudo systemctl enable mariadb
```

### Step 5: Secure MariaDB Installation (Recommended)

MariaDB comes with a script called `mysql_secure_installation` that helps you improve the security of your MariaDB installation. Run this script:

```bash
sudo mysql_secure_installation
```

Follow the prompts to set a password for the root account, remove anonymous users, disallow remote root login, remove the test database, and reload privilege tables.

### Step 6: Verify MariaDB Installation

To verify that MariaDB has been successfully installed and is running, execute the following command:

```bash
sudo systemctl status mariadb
```

You should see output indicating that the service is active (running).

### Step 7: Connect to MariaDB

You can connect to the MariaDB server using the MySQL client:

```bash
mysql -u root -p
```

Enter the password you set during the `mysql_secure_installation` process.

---
Creating a simple database and table in MariaDB involves several steps, including logging into the MariaDB shell, creating a database, and then creating a table within that database. Below is a step-by-step guide to accomplish this task.

### Step 1: Log into MariaDB

First, you need to log into the MariaDB shell. You can do this by running the following command in your terminal:

```bash
mysql -u root -p
```

You will be prompted to enter the password for the `root` user. Enter the password you set during the MariaDB installation or configuration process.

### Step 2: Create a Database

Once logged into the MariaDB shell, you can create a new database. For example, let's create a database named `mydatabase`:

```sql
CREATE DATABASE mydatabase;
```

### Step 3: Select the Database

Before creating a table, you need to select the database you just created:

```sql
USE mydatabase;
```

### Step 4: Create a Table

Now, you can create a table within the selected database. For instance, let's create a simple table named `employees` with columns for `id`, `first_name`, `last_name`, and `email`:

```sql
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100)
);
```

This SQL statement creates a table with four columns:
- `id`: An integer column that auto-increments and serves as the primary key.
- `first_name`: A variable character string column that can hold up to 50 characters.
- `last_name`: Another variable character string column that can hold up to 50 characters.
- `email`: A variable character string column that can hold up to 100 characters.

### Step 5: Insert Data into the Table

After creating the table, you can insert some sample data into it:

```sql
INSERT INTO employees (first_name, last_name, email) VALUES ('John', 'Doe', 'john.doe@example.com');
INSERT INTO employees (first_name, last_name, email) VALUES ('Jane', 'Doe', 'jane.doe@example.com');
```

These statements insert two rows into the `employees` table.

### Step 6: Query the Table

Finally, you can query the table to see the data you've inserted:

```sql
SELECT * FROM employees;
```

This command retrieves all records from the `employees` table and displays them.


