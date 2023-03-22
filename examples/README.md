# About

This document contains usage examples for individual roles from `community.fdo` Ansible Collection.
A copy-paste Ansible playbook snippets are listed below.

# Preparation

You need to install Ansible and `community.fdo` & `ansible.posix` collections.

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
  vars:
    - aio_configuration_serviceinfo_api_auth_token: "token_1" # to be changed
    - aio_configuration_serviceinfo_api_admin_token: "token_2" # to be changed
  tasks:
    # Role updates FDO AIO Server config files and restarts the services.
    # In case ports are changed, it also enables newly configured ports.
    - import_role:
        name: configure_aio_server
```

## Install Manufacturing, Owner & Rendezvous Servers

In case of the specific use-case where Manufacturing Server is located in different network than Owner and Rendezvous Servers - and the latter can't access the former, `copy_manufacturer_certs` variable has to be set to `false` (for Owner & Rendezvous Servers installation).

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
  vars:
  #  - copy_manufacturer_certs: false
  tasks:
    # Role installs required packages, copies required keys and certificates from Manufacturing Server,
    # starts services and enables required ports for FDO Owner Server.
    - import_role:
        name: setup_owner_server

- name: Install Rendezvous Server
  hosts: rendezvous_server
  become: true
  gather_facts: true
  vars:
  #  - copy_manufacturer_certs: false
  tasks:
    # Role installs required packages, copies required keys and certificates from Manufacturing Server,
    # starts services and enables required ports for FDO rendezvous Server.
    - import_role:
        name: setup_rendezvous_server
```

> Note: server components are not configured as a part of `setup` roles. To successfully complete installation run `configure` roles.

## Configure Manufacturing, Owner & Rendezvous Servers

In case of the specific use-case where Manufacturing Server is located in different network than Owner and Rendezvous Servers - and the latter can't access the former, `update_keys_certs` variable has to be set to `false` (for Owner & Rendezvous Servers configuration).

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
  vars:
  #  - update_keys_certs: false
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
  vars:
  #  - update_cert: false
  tasks:
    # Role updates FDO Rendezvous Server config files and restarts the services.
    # If not configured otherwise it also updates installed Manufacturing Server keys and certificates .
    # In case ports are changed, it also enables newly configured ports.
    - import_role:
        name: configure_rendezvous_server
```

## Copy Manufacturing Server Certificates and Keys to Owner/Rendezvous Servers via localhost

```yaml
---
- name: Fetch Manufacturing Server Certs and Keys to localhost
  hosts: manufacturing_server
  become: true
  gather_facts: true
  tasks:
    # Role copies Server Certificates and Keys from Manufacturing Server to localhost.
    # This role should be delegated only to Manufacturing Server.
    - import_role:
        name: fetch_manufacturing_server_certs_to_localhost

- name: Copy Manufacturing Server Certs and Keys to Owner Server
  hosts: owner_server
  become: true
  gather_facts: true
  tasks:
    # Role copies Manufacturing Server Certificates and Keys from localhost to Owner Server.
    # This role should be delegated only to Owner Server.
    - import_role:
        name: copy_manufacturing_server_certs_to_owner_server

- name: Copy Manufacturing Server Certs to Rendezvous Server
  hosts: rendezvous_server
  become: true
  gather_facts: true
  tasks:
    # Role copies Manufacturing Server Certificate from localhost to Rendezvous Server.
    # This role should be delegated only to Rendezvous Server.
    - import_role:
        name: copy_manufacturing_server_certs_to_rendezvous_server
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
    # This role should be delegated only to Owner Server.
    - import_role:
        name: copy_ownership_vouchers
```

## Copy Manufacturing Server Ownership Vouchers via localhost

```yaml
---
- name: Fetch Ownership Vouchers from Manufacturer server to localhost
  hosts: manufacturing_server
  become: true
  gather_facts: true
  tasks:
    # Role copies Device Ownership Vouchers from Manufacturing Server to localhost.
    # This role should be delegated only to Manufacturing Server.
    - import_role:
        name: fetch_ownership_vouchers_to_localhost

- name: Copy Ownership Vouchers from localhost to Owner server
  hosts: owner_server
  become: true
  gather_facts: true
  tasks:
    # Role copies Device Ownership Vouchers from localhost to Owner Server.
    # This role should be delegated only to Owner Server.
    - import_role:
        name: copy_ownership_vouchers_from_localhost
```

## Use Custom FDO Keys and Certificates

In cases where manufacturing and owner servers belong to different entities, it is possible to use custom
keys and certificates instead of having them generated by the manufacturing server. The following examples
show how to disable the automatic generation, and distribute locally stored keys and certificates to FDO servers.

```yaml
---
- name: Install Manufacturing Server with Custom Keys and Certificates
  hosts: manufacturing_server
  become: true
  gather_facts: true
  vars:
    manufacturing_server_generate_keys_and_certificates: false
  tasks:
    # Role installs packages required for FDO manufacturing server, copies required configuration and opens firewall ports
    - import_role:
        name: setup_manufacturing_server
    # Role copies keys and certificates required for FDO manufacturing server from localhost
    - import_role:
        name: copy_manufacturing_server_certs_to_manufacturing_server

- name: Install Rendezvous Server with Custom Keys and Certificates
  hosts: rendezvous_server
  become: true
  gather_facts: true
  vars:
    copy_manufacturer_certs: false
  tasks:
    # Role installs packages required for FDO rendezvous server, copies required configuration and opens firewall ports
    - import_role:
        name: setup_rendezvous_server
    # Role copies keys and certificates required for FDO rendezvous server from localhost
    - import_role:
        name: copy_manufacturing_server_certs_to_rendezvous_server

- name: Install Owner Server with Custom Keys and Certificates
  hosts: owner_server
  become: true
  gather_facts: true
  vars:
    copy_manufacturer_certs: false
  roles:
    # Role installs packages required for FDO owner server, copies required configuration and opens firewall ports
    - import_role:
        name: setup_owner_server
    # Role copies keys and certificates required for FDO owner server from localhost
    - import_role:
        name: copy_manufacturing_server_certs_to_owner_server
```

A custom location for keys and certificates can be specified via the `localhost_manufacturing_server_certs_dir` variable.

## Generate Keys and Certificates on Local Host

The collection also includes a role for generating all or a subset of keys and certificates if needed.

```yaml
---
- name: Generate FDO Keys and Certificates
  hosts: localhost
  become: true
  gather_facts: true
  tasks:
    # Role generates keys and certificates of FDO types
    - import_role:
        name: generate_keys_and_certificates
```
