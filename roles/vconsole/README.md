<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: lingfra.system.vconsole

Templates vconsole.conf.

## Supported Platforms

Not specified.

## Entrypoint `main` - Main entry point for vconsole role

Running the role from this entrypoint templates the `/etc/vconsole.conf` file.

Refer to [**vconsole(5)**](https://man.archlinux.org/man/core/systemd/vconsole.conf.5.en) for more information on the options.

### Options for `main`

#### `vconsole_chroot_path`

Type: `str`, optional.

If specified, all actions of this role are executed in the chroot directory.

#### `vconsole_conf_keymap`

Type: `str`, Default: `us`.



#### `vconsole_conf_font`

Type: `str`, optional.



## Dependencies

None.

## Project Information

This role is part of the Ansible collection [lingfra.system][collection_url].
For more information, see the collections [README](../../README.md) file.

[collection_url]: https://codeberg.org/lingfra/ansible-collection-lingfra-system
<!-- END_ANSIBLE_DOCS -->
