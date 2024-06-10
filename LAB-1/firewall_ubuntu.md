## UFW Firewall Management

UFW (Uncomplicated Firewall) is a user-friendly interface built on top of iptables, simplifying firewall management in Linux. Here's a list of essential commands for working with UFW:

**Checking Status:**

* **`sudo ufw status`:** Displays the current UFW status, including active rules and the default policy (allow incoming, deny incoming).
* **`sudo ufw status verbose`:** Provides a more detailed view of the firewall configuration, including numbered rules.

**Enabling/Disabling:**

* **`sudo ufw enable`:** Activates the firewall and applies the default rules.
* **`sudo ufw disable`:** Deactivates the firewall, suspending all rules.

**Allowing Applications/Ports:**

* **`sudo ufw allow APPLICATION`:** Allows traffic for a specific application profile (e.g., `sudo ufw allow OpenSSH`).
* **`sudo ufw allow PORT/PROTOCOL`:** Opens a specific port for a particular protocol (e.g., `sudo ufw allow 80/tcp` for web traffic).

**Denying Traffic:**

* **`sudo ufw deny APPLICATION`:** Blocks traffic for an application profile (e.g., `sudo ufw deny http`).
* **`sudo ufw deny PORT/PROTOCOL`:** Closes a specific port for a protocol (e.g., `sudo ufw deny 22/tcp` to block SSH access).

**Deleting Rules:**

* **`sudo ufw delete RULE_NUMBER`:** Removes a rule identified by its number (use `sudo ufw status verbose` to find rule numbers).

**Advanced Options:**

* **`sudo ufw logging on/off`:** Enables or disables firewall logging.
* **`sudo ufw app list`:** Lists available application profiles.
* **`sudo ufw show raw`:** Displays the underlying iptables rules managed by UFW.

**Remember:**

* Use `sudo` for commands requiring administrative privileges.
* UFW offers a simpler approach compared to directly managing iptables rules.
* It's recommended to allow only the applications and ports you genuinely need for security purposes.
