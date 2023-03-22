===========================
Community.Fdo Release Notes
===========================

.. contents:: Topics

v2.0.0
======

Release Summary
---------------

This release fixes ansible-lint violations in the roles.

Name of the `aio_configuration_contact_addresses_IpAddr` variable changes to `aio_configuration_contact_addresses_ipaddr`,
which breaks backward compatibility.

Other changes
-------------

- Added explicit empty options to argument specifications without options
- Fixed too long lines
- Specified FQCNs for builtin and posix module actions
- Fixed variable names according to the naming conventions
- Explicitly specified permissions for files when using file/copy/template/...
- Replaced relative paths with absolute ones
- Replaced `yes/no` with `true/false`
- Removed comparing to literal `true/false` when the value is already a boolean
- Replaced the `systemctl status` command with `ansible.builtin.systemd` module for checking the status of a systemd service
- Added `changed_when` to commands for indicating when a command causes changes
- Used `present` instead of `latest` for packages to avoid inadvertent upgrades
- Added support for Simple Content Access (SCA) subscriptions on RHEL
- Allowed running the roles on non-RHEL systems that include the FDO packages
- Enabled a user to generate FDO keys and certificates locally and use them or custom ones with FDO servers

v1.0.0
======

Release Summary
---------------

Initial release

New Roles
---------

- community.fdo.check_rhel_subscription - Check Red Hat Subscription
- community.fdo.configure_aio_server - (Re)Configure FDO AIO Server
- community.fdo.configure_manufacturing_server - (Re)Configure FDO Manufacturing Server
- community.fdo.configure_owner_server - (Re)Configure FDO Owner Server
- community.fdo.configure_rendezvous_server - (Re)Configure FDO Rendezvous Server
- community.fdo.copy_manufacturing_server_certs_to_owner_server - Copy Manufacturing Server Certificates from localhost to Owner Server
- community.fdo.copy_manufacturing_server_certs_to_rendezvous_server - Copy Manufacturing Server Certificates from localhost to Rendezvous Server
- community.fdo.copy_ownership_vouchers - Copy Device Ownership Vouchers from Manufacturing Server to Owner Server
- community.fdo.copy_ownership_vouchers_from_localhost - Copy Device Ownership Vouchers from localhost to Owner Server
- community.fdo.fetch_manufacturing_server_certs_to_localhost - Fetch Manufacturing Server Certificates to localhost
- community.fdo.fetch_ownership_vouchers_to_localhost - Fetch Device Ownership Vouchers to localhost
- community.fdo.setup_aio_server - Setup FDO AIO Server
- community.fdo.setup_manufacturing_server - Setup FDO Manufacturing Server
- community.fdo.setup_owner_server - Setup FDO Owner Server
- community.fdo.setup_rendezvous_server - Setup FDO Rendezvous Server
