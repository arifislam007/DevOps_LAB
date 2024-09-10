# Install RabitMQ on RokeyLinux-9 
```bash
dnf install -y epel-release
curl -s https://packagecloud.io/install/repositories/rabbitmq/rabbitmq-server/script.rpm.sh | sudo bash
curl -1sLf 'https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-erlang/setup.rpm.sh' | sudo -E bash
dnf install -y rabbitmq-server
systemctl start rabbitmq-server
rabbitmq-plugins enable rabbitmq_management
```

# Create and give user permission 
```bash
rabbitmqctl add_user test test
rabbitmqctl set_user_tags test administrator
rabbitmqctl set_permissions -p / test ".*" ".*" ".*"
```
