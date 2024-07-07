---
- name: Install Apache
  hosts:
  tasks:
  - name: Install apache package
  apt:
    name: apache2
    state: present
    update_cache: yes

- name: Ensure Apache is enabled and started
  systemd:
    name: apache2
    enabled: yes
    state: started
- name: Deploy custom index.html
  template:
    src: index.html.j2
    dest: /var/www/html/index.html
    mode: '0644'
