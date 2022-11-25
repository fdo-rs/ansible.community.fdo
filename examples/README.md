# About

The `examples` directory contains usage examples for individual roles.
A copy-paste Ansible playbook snippets are listed below.

# Preparation

You need to install ansible and the `community.fdo` collection.

# Examples

## Install FDO AIO Server

```yaml
---
- name: Install FDO AIO Server
  hosts: aio_server
  become: true
  gather_facts: true
  tasks:
    # Role installs required packages, starts services & 
    # enables required ports for FDO AIO Server.
    - import_role:
        name: setup_aio_server
```

## Configure FDO AIO Server

```yaml
---
- name: Configure FDO AIO Server
  hosts: aio_server
  become: true
  gather_facts: true
  tasks:
    # Role updates FDO AIO Server config files and restarts the services.
    # In case ports are changed, it also enables newly configured ports.
    - import_role:
        name: configure_aio_server
```

## Install Manufacturing, Owner & Rendezvous Servers

```yaml
---
- name: Install Manufacturing Server
  hosts: manufacturing_server
  become: true
  gather_facts: true
  tasks:
    # Role installs required packages, starts services & 
    # enables required ports for FDO Manufacturing Server.
    - import_role:
        name: setup_manufacturing_server

- name: Install Owner Server
  hosts: owner_server
  become: true
  gather_facts: true
  tasks:
    # Role installs required packages, copies required keys and certificates from Manufacturing Server,
    # starts services and enables required ports for FDO Owner Server.
    - import_role:
        name: setup_owner_server

- name: Install Rendezvous Server
  hosts: rendezvous_server
  become: true
  gather_facts: true
  tasks:
    # Role installs required packages, copies required keys and certificates from Manufacturing Server,
    # starts services and enables required ports for FDO rendezvous Server.
    - import_role:
        name: setup_rendezvous_server
```

> Note: server components are not configured as a part of `setup` roles. To successfully complete installation run `configure` roles.

## Configure Manufacturing, Owner & Rendezvous Servers

```yaml 
---
- name: Configure Manufacturing Server
  hosts: manufacturing_server
  become: true
  gather_facts: true
  tasks:
    # Role updates FDO Manufacturing Server config files and restarts the services.
    # In case ports are changed, it also enables newly configured ports.
    - import_role:
        name: configure_manufacturing_server

- name: Configure Owner Server
  hosts: owner_server
  become: true
  gather_facts: true
  tasks:
    # Role updates FDO Owner Server config files and restarts the services.
    # If not configured otherwise it also updates installed Manufacturing Server keys and certificates .
    # In case ports are changed, it also enables newly configured ports.
    - import_role:
        name: configure_owner_server

- name: Configure Rendezvous Server
  hosts: rendezvous_server
  become: true
  gather_facts: true
  tasks:
    # Role updates FDO Rendezvous Server config files and restarts the services.
    # If not configured otherwise it also updates installed Manufacturing Server keys and certificates .
    # In case ports are changed, it also enables newly configured ports.
    - import_role:
        name: configure_rendezvous_server
```

## Copy Manufacturing Server Ownership Vouchers

```yaml
---
- name: Copy Ownership Vouchers
  hosts: owner_server
  become: true
  gather_facts: true
  tasks:
    # Role copies Device Ownership Vouchers from Manufacturing Server to Owner Server.
    - import_role:
        name: copy_ownership_vouchers
```

> Note: this role should be delegated to Owner Server.