# Postgres on Ubuntu-22.04

Installing PostgreSQL on Ubuntu 22.04 involves several steps, including importing the official signing key, adding the PostgreSQL repository, installing the PostgreSQL package, and starting the service. Here's a step-by-step guide to get you started:

### Step 1: Import the Official Signing Key

First, import the official PostgreSQL signing key. This ensures that the packages you install are authentic and come directly from PostgreSQL.

```bash
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```

### Step 2: Add PostgreSQL Repository

Add the PostgreSQL repository to your system. This repository contains the latest stable releases of PostgreSQL.

```bash
RELEASE=$(lsb_release -cs)
echo "deb http://apt.postgresql.org/pub/repos/apt/ ${RELEASE}"-pgdg main | sudo tee /etc/apt/sources.list.d/pgdg.list
```

This command adds the PostgreSQL repository for Ubuntu 22.04 (Jammy Jellyfish) to your system's list of repositories.

### Step 3: Update Package Lists

Update your package lists to include the newly added PostgreSQL repository:

```bash
sudo apt update
```

### Step 4: Install PostgreSQL

Now, install PostgreSQL along with the client tools:

```bash
sudo apt install postgresql postgresql-contrib -y
```

### Step 5: Start PostgreSQL Service

Once the installation is complete, start the PostgreSQL service:

```bash
sudo systemctl start postgresql
```

### Step 6: Enable PostgreSQL to Start at Boot

To ensure that PostgreSQL starts automatically whenever your system boots, enable it with the following command:

```bash
sudo systemctl enable postgresql
```

### Step 7: Verify PostgreSQL Installation

To verify that PostgreSQL has been successfully installed and is running, execute the following command:

```bash
sudo systemctl status postgresql
```

You should see output indicating that the service is active (running).

### Step 8: Access PostgreSQL

By default, PostgreSQL creates a superuser named `postgres` during installation. You can switch to this user and access the PostgreSQL prompt:

```bash
sudo su - postgres
psql
```

From here, you can start creating databases, tables, and users according to your application's requirements.

### Step 9: Exit PostgreSQL Prompt

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
