
---

#  Ansible Role: vSphere VM Deployment

This Ansible role automates the deployment of virtual machines in a VMware vSphere environment using a predefined template. It is structured for reusability and easy parameter management through external variable files.

---

##  Requirements

* **Ansible 2.10+**

* **Python packages:**

  ```bash
  pip install pyvmomi
  ```

* **Ansible collection:**

  ```bash
  ansible-galaxy collection install community.vmware
  ```

---

##  Role Structure

```
vsphere_vm_deploy_role/
├── defaults/
│   └── main.yml        # Default input parameters
├── tasks/
│   └── main.yml        # Task file to deploy VM
├── README.md           # You're here!
```

---

## 🔧 Default Variables

You can override these variables in your playbook or inventory.

```yaml
vcenter_hostname: "vcenter.example.com"
vcenter_username: "administrator@vsphere.local"
vcenter_password: "your_password"

datacenter_name: "Datacenter"
cluster_name: "Cluster"
datastore_name: "Datastore1"
vm_folder: "VMs"
vm_name: "TestVM"
template_name: "UbuntuTemplate"
vm_network: "VM Network"
vm_num_cpus: 2
vm_memory_mb: 2048
vm_guest_id: "ubuntu64Guest"

vm_ip_config:
  type: dhcp                      # Options: dhcp or static
  ip: "192.168.1.100"             # Required if type is static
  netmask: "255.255.255.0"
  gateway: "192.168.1.1"
  dns_servers:
    - "8.8.8.8"
    - "8.8.4.4"
```

>  **Security Tip:** Store credentials like `vcenter_password` in Ansible Vault or use environment variables.

---

##  Example Playbook

```yaml
---
- name: Deploy a VM to vSphere
  hosts: localhost
  gather_facts: no

  roles:
    - role: vsphere_vm_deploy_role
```

---

##  Notes

* The role uses the `community.vmware.vmware_guest` module.
* Ensure your vSphere template is properly sysprepped or cloud-init enabled.
* Modify `vm_ip_config` for static IP configurations.
* `wait_for_ip_address: yes` ensures deployment completes only after networking is active.

---


