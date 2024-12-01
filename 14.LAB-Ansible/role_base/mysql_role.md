# Ansible Role: MySQL Database

## Description

A specialized Ansible role for installing and configuring MySQL on Rocky Linux (RHEL 8/9 compatible). This role provides a comprehensive solution for MySQL database management, optimized for Rocky Linux system architecture and security model.

## Key Features

- MySQL 8.0+ installation
- Rocky Linux 8 and 9 compatibility
- DNF package management
- SELinux integration
- Firewalld configuration
- System performance optimization
- Secure database configuration

## System Requirements

### Rocky Linux Versions
- Rocky Linux 8.x
- Rocky Linux 9.x

### Minimum System Specifications
- CPU: 2 cores
- RAM: 2 GB
- Disk: 20 GB free space
- Network: Internet connection for package installation

## Prerequisites

### Control Node
- Ansible 2.14+
- Python 3.8+
- `ansible-collection-community-mysql`

### Managed Nodes
- Rocky Linux 8 or 9
- Root or sudo access
- SELinux enabled
- Firewalld active

## Role Variables

### MySQL Installation Parameters

| Variable | Default | Description |
|----------|---------|-------------|
| `mysql_version` | `8.0` | MySQL version |
| `mysql_datadir` | `/var/lib/mysql` | MySQL data directory |
| `mysql_port` | `3306` | MySQL server port |
| `mysql_bind_address` | `0.0.0.0` | Binding IP address |
| `mysql_root_password` | `null` | MySQL root password |

### Rocky Linux Specific Configuration

```yaml
# Rocky Linux MySQL configuration
mysql_rocky_specific:
  use_appstream: true
  selinux_mode: enforcing
  firewalld_zone: public
```

### Database Creation Example

```yaml
mysql_databases:
  - name: myapp_database
    encoding: utf8mb4
    collation: utf8mb4_unicode_ci

mysql_users:
  - name: myapp_user
    host: "%"
    password: "SecurePassword123!"
    priv: "myapp_database.*:ALL"
```

## Installation Dependencies

```bash
# Install required collections
ansible-galaxy collection install \
  community.mysql \
  ansible.posix \
  community.general
```

## Example Playbook

```yaml
- hosts: rocky_mysql_servers
  become: true
  vars:
    mysql_root_password: "ComplexRootPassword!"
    mysql_databases:
      - name: rockycms
    mysql_users:
      - name: rockyadmin
        password: "AdminUserPassword"
        priv: "rockycms.*:ALL"
  roles:
    - rocky_mysql_role
```

## Security Configurations

### Rocky Linux Security Features
- SELinux policy management
- Firewalld port configuration
- System-wide crypto policy compliance
- Package signature verification

### Recommended Security Settings

```yaml
mysql_security_settings:
  remove_anonymous_users: true
  disallow_root_login_remotely: true
  remove_test_database: true
```

## Performance Optimization

### Rocky Linux Tuned Profiles
- Automatically selects appropriate system tuning profile
- Configures MySQL for optimal performance
- Adjusts kernel parameters

## Firewall Configuration

Automatically configures firewalld:
- Opens MySQL port
- Configures service rules
- Supports custom zone configurations

## Backup Strategy

### Integrated Backup Options
- Mysqldump
- Percona XtraBackup support
- Automated backup scheduling

```yaml
mysql_backup:
  enabled: true
  directory: "/backup/mysql"
  retention_days: 7
```

## Troubleshooting

### Common Diagnostic Commands
```bash
# Check MySQL service status
sudo systemctl status mysqld

# Verify SELinux context
sudo sestatus

# Check firewall rules
sudo firewall-cmd --list-all
```

## Molecule Testing

```bash
# Prepare test environment
pip install molecule[docker] ansible
molecule test --scenario-name rocky
```

## Compatibility Matrix

| MySQL Version | Rocky Linux 8 | Rocky Linux 9 |
|--------------|--------------|--------------|
| 8.0          | ✓            | ✓            |
| 8.1          | ✓            | ✓            |
| 8.2          | ✓            | ✓            |

## Contributing

1. Fork Repository
2. Create Feature Branch
3. Write Molecule Tests
4. Implement Changes
5. Run Comprehensive Tests
6. Submit Pull Request

## License

Apache License 2.0

## Author

Rocky MySQL Role Maintainer
- Email: maintainer@example.com
- GitHub: @rockylinux_ansible_maintainer

## Changelog

### v1.1.0
- Added Rocky Linux 9 support
- Improved SELinux integration
- Enhanced firewalld configuration
```

This README provides a comprehensive guide for an Ansible MySQL role specifically designed for Rocky Linux. It covers installation, configuration, security, and performance optimization tailored to Rocky Linux's ecosystem.

Key highlights:
- Specific Rocky Linux considerations
- Comprehensive security configuration
- Firewalld and SELinux integration
- Performance optimization
- Detailed troubleshooting guide

Would you like me to elaborate on any specific aspect of MySQL configuration for Rocky Linux?
