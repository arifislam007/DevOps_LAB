### Step 1: Update the System
Before installing any software, ensure your system is up-to-date.

```bash
sudo dnf update -y
```

### Step 2: Install AWS CLI using `dnf`

The AWS CLI version 2 is available directly from the AWS official repository and can be installed using a package from Amazon.

1. **Download the AWS CLI installation package:**

   ```bash
   curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
   ```

2. **Unzip the downloaded file:**

   Install the `unzip` package if it's not already installed, and then unzip the AWS CLI package.

   ```bash
   sudo dnf install unzip -y
   unzip awscliv2.zip
   ```

3. **Run the installation script:**

   ```bash
   sudo ./aws/install
   ```

4. **Verify the installation:**

   After the installation completes, you can verify the AWS CLI version to confirm the installation.

   ```bash
   aws --version
   ```

   The output should show something like:
   ```
   aws-cli/2.x.x Python/3.x.x Linux/x86_64
   ```

### Step 3: Configure AWS CLI

Once installed, configure the AWS CLI with your credentials and default region.

```bash
aws configure
```

It will prompt you for:

- **AWS Access Key ID**
- **AWS Secret Access Key**
- **Default region name** (e.g., `us-west-2`)
- **Default output format** (e.g., `json`, `text`, or `table`)

### Step 4: Confirm Installation

Run the following command to check if the AWS CLI is properly configured:

```bash
aws s3 ls
```

This should return a list of your S3 buckets if your credentials and configuration are correct.

### Optional: Uninstall AWS CLI

If you ever need to uninstall the AWS CLI:

```bash
sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update
```

