<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: lingfra.system.sd_resolved

Configures systemd-resolved.

## Supported Platforms

Not specified.

## Entrypoint `main` - Main entry point for sd_resolved role

This is the main entrypoint for the lingfra.system.sd_resolved role.

### Options for `main`

#### `sd_resolved_chroot_path`

Type: `str`, optional.

If specified, all actions are executed inside the chroot.

#### `sd_resolved_conf_llmr`

Type: `bool`, optional.



## Dependencies

None.

## Project Information

This role is part of the Ansible collection [lingfra.system][collection_url].
For more information, see the collections [README](../../README.md) file.

[collection_url]: https://codeberg.org/lingfra/ansible-collection-lingfra-system
<!-- END_ANSIBLE_DOCS -->
