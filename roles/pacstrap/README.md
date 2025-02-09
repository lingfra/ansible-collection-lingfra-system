<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: lingfra.system.pacstrap

Runs pacstrap on a target folder.

## Supported Platforms

Not specified.

## Entrypoint `main` - Main entry point for pacstrap role

This is a rather simple role, which executes [**pacstrap(8)**](https://man.archlinux.org/man/pacstrap.8) on a folder.
The roles makes checks, so the result is idempotent and pacstrap is not executed on an already pacstrapped folder.

### Options for `main`

#### `pacstrap_chroot_path`

Type: `str`, **required**.

This is the target path for the pacstrap installation.

#### `pacstrap_packages`

Type: `list of 'str'`, Default: `['linux-firmware', 'reflector', 'man-db', 'man-pages', 'neovim', 'sudo', 'e2fsprogs', 'lvm2', 'grub', 'python', 'tmux', 'qemu-guest-agent']`.

List of packages, which should be installed by pacstrap. The packages `base` and `linux-firmware` need not to be specified, they are installed by default.

## Dependencies

None.

## Project Information

This role is part of the Ansible collection [lingfra.system][collection_url].
For more information, see the collections [README](../../README.md) file.

[collection_url]: https://codeberg.org/lingfra/ansible-collection-lingfra-system
<!-- END_ANSIBLE_DOCS -->
