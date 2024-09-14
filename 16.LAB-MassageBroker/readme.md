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
# Declare Queue and topic in RabitMq
```bash
wget http://localhost:15672/cli/rabbitmqadmin
chmod +x rabbitmqadmin
./rabbitmqadmin declare exchange name=logstash_exchange type=direct
./rabbitmqadmin declare queue name=logstash_queue durable=true
./rabbitmqadmin declare binding source=logstash_exchange destination=logstash_queue routing_key=logstash_key

```

# Install logstash on log endpoint
```bash
curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
sudo apt update
sudo apt install logstash
```
- Then Create a data processing configuration file on the directory /etc/logstash/conf.d/rabitmq.conf
- Make sure that source log file has permission to read like /var/log/syslog

# Manually consuem logs if you have any issue with Logs consumeing
```bash
./rabbitmqadmin get queue=logstash_queue
```


