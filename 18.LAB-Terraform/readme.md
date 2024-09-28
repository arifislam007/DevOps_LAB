# Terraofrm on Rocky Linux-9 or Fedora

```bash
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
sudo yum update
sudo yum -y install terraform
```
---

# Install Terraform in Debian, Ubuntu & Mint
```bash
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update 
sudo apt install terraform
```
---

# Check if Terrafor is installed and which version 

```bash
terraform version
```


https://github.com/arifislam007/terraform_aws_vpc_ec2/blob/main/ec2_launch.tf
