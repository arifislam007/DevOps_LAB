# Postgres on centos-7 

Installing PostgreSQL on CentOS 7 involves several steps, including adding the PostgreSQL repository, installing the PostgreSQL package, initializing the database, and starting the service. Here's a step-by-step guide to get you started:

### Step 1: Add PostgreSQL Repository

PostgreSQL provides a YUM repository for CentOS/RHEL systems. First, you need to add the PostgreSQL repository to your system. You can do this by downloading and installing the repository RPM package:

```bash
wget https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
sudo rpm -ivh pgdg-redhat-repo-latest.noarch.rpm
```

### Step 2: Install PostgreSQL

After adding the repository, you can install PostgreSQL:

```bash
sudo yum install postgresql13 postgresql-server -y
```

Note: The version number (`13` in this example) may vary depending on the latest available version of PostgreSQL. You can check the available versions by looking at the repository or visiting the PostgreSQL website.

### Step 3: Initialize the Database

Before starting the PostgreSQL service, you need to initialize the database cluster. This step creates the necessary directories and sets up the initial database configuration:

```bash
sudo /usr/bin/postgresql-setup --initdb
```

### Step 4: Start PostgreSQL Service

Once the initialization is complete, start the PostgreSQL service:

```bash
sudo systemctl start postgresql
```

### Step 5: Enable PostgreSQL to Start at Boot

To ensure that PostgreSQL starts automatically whenever your system boots, enable it with the following command:

```bash
sudo systemctl enable postgresql
```

### Step 6: Verify PostgreSQL Installation

To verify that PostgreSQL has been successfully installed and is running, execute the following command:

```bash
sudo systemctl status postgresql
```

You should see output indicating that the service is active (running).

### Step 7: Access PostgreSQL

By default, PostgreSQL creates a superuser named `postgres` during installation. You can switch to this user and access the PostgreSQL prompt:

```bash
sudo su - postgres
psql
```

From here, you can start creating databases, tables, and users according to your application's requirements.

### Step 8: Exit PostgreSQL Prompt

To exit the PostgreSQL prompt, type `\q` and press Enter. Then, exit the `postgres` user session by typing `exit` and pressing Enter.

---
Testing a database with sample data is a common practice to ensure that your database schema works as expected and to validate the functionality of your application. Below is a general approach to creating a simple database with sample data using SQL. This example assumes you are using a SQL-based database system like PostgreSQL, MySQL, or SQLite. The exact syntax might vary slightly depending on the database system you're using.

### Step 1: Create a Database

First, you need to create a database where your tables and sample data will reside. Connect to your database system and execute the following SQL command:

```sql
CREATE DATABASE test_db;
```

### Step 2: Switch to the New Database

Switch to the newly created database:

```sql
\c test_db
```

### Step 3: Create a Sample Table

Let's create a simple table named `employees` with a few columns:

```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100)
);
```

### Step 4: Insert Sample Data

Insert some sample data into the `employees` table:

```sql
INSERT INTO employees (first_name, last_name, email) VALUES 
('John', 'Doe', 'john.doe@example.com'),
('Jane', 'Doe', 'jane.doe@example.com'),
('Alice', 'Smith', 'alice.smith@example.com');
```

### Step 5: Query the Sample Data

Query the `employees` table to verify that the data was inserted correctly:

```sql
SELECT * FROM employees;
```

This command retrieves all records from the `employees` table and displays them.


