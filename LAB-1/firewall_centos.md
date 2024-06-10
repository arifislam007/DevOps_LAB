## Firewalld Management Commands

Firewalld is a powerful firewall management tool commonly used in modern Linux distributions. It provides a dynamic and zone-based approach to configuring firewall rules. Here's a breakdown of essential commands for working with firewalld:

**Checking Status:**

* **`sudo firewall-cmd --get-default-zone`:** Shows the default firewall zone (e.g., `public`, `internal`).
* **`sudo firewall-cmd --get-active-zones`:** Lists all active firewall zones.
* **`sudo firewall-cmd --list-all`:** Displays all firewall rules for all zones.

**Managing Zones:**

* **`sudo firewall-cmd --zone ZONE_NAME --list-all`:** Lists all rules for a specific zone (replace `ZONE_NAME` with the actual zone name).
* **`sudo firewall-cmd --zone ZONE_NAME --get-services`:** Shows services allowed in a zone.
* **`sudo firewall-cmd --zone ZONE_NAME --get-ports`:** Displays open ports in a zone.

**Adding Rules (**permanent vs. runtime**):**

* **`sudo firewall-cmd --permanent --zone ZONE_NAME --add-service SERVICE`:** Permanently adds a service (like SSH) to the specified zone.
* **`sudo firewall-cmd --zone ZONE_NAME --add-service SERVICE`:** Adds a service to the zone for the current session only (not persistent).
* **`sudo firewall-cmd --permanent --zone ZONE_NAME --add-port PORT/PROTOCOL`:** Permanently adds a port and protocol combination (e.g., `80/tcp` for web traffic) to the zone.
* **`sudo firewall-cmd --zone ZONE_NAME --add-port PORT/PROTOCOL`:** Adds a port/protocol to the zone temporarily (not persistent).

**Important Considerations:**

* Use `--permanent` to save rule changes for future sessions. Remember to reload the firewall with `sudo firewall-cmd --reload` after making permanent modifications.
* Choose the appropriate zone for your rules (e.g., `public` for external access, `internal` for trusted networks).
* Modifying firewall rules can impact system security. Make changes carefully and understand the implications before applying them.

**Additional Commands:**

* **`sudo firewall-cmd --delete-service SERVICE --zone ZONE_NAME`:** Removes a service from a zone (permanent or runtime).
* **`sudo firewall-cmd --delete-port PORT/PROTOCOL --zone ZONE_NAME`:** Deletes a port/protocol rule from a zone (permanent or runtime).
* **`sudo firewall-cmd --help`:** Provides detailed help information for firewalld commands.
