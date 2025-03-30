<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: lingfra.system.sd_networkd

Configures systemd-networkd.

## Supported Platforms

Not specified.

## Entrypoint `main` - Main entry point for lingfra.system.sd_networkd role

This is the main entrypoint for the lingfra.system.sd_networkd role.

### Options for `main`

#### `sd_networkd_chroot_path`

Type: `str`, optional.

If specified, all actions are executed inside the chroot.

#### `sd_networkd_conf_ipv6_privacy_extensions`

Type: `bool`, optional.



## Dependencies

None.

## Project Information

This role is part of the Ansible collection [lingfra.system][collection_url].
For more information, see the collections [README](../../README.md) file.

[collection_url]: https://codeberg.org/lingfra/ansible-collection-lingfra-system
<!-- END_ANSIBLE_DOCS -->
