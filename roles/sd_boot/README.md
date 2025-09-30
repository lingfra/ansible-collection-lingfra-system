<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: lingfra.system.sd_boot

Configures systemd-boot for UEFI systems.

## Supported Platforms

Not specified.

## Entrypoint `main` - Main entry point for lingfra.system.sd_boot role

Configures systemd boot

### Options for `main`

#### `sd_boot_chroot_path`

Type: `str`, optional.

If specified, all actions are executed inside the chroot.

## Dependencies

None.

## Project Information

This role is part of the Ansible collection [lingfra.system][collection_url].
For more information, see the collections [README](../../README.md) file.

[collection_url]: https://codeberg.org/lingfra/ansible-collection-lingfra-system
<!-- END_ANSIBLE_DOCS -->
