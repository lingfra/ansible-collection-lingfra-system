<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: lingfra.system.genfstab

Generates an fstab on a target directory.

## Supported Platforms

Not specified.

## Entrypoint `main` - Main entry point for genfstab role

This role runs `genfstab` and writes the fstab file.

Refer to [**genfstab(8)**](https://man.archlinux.org/man/genfstab.8) and [genfstab (ArchWiki)](https://wiki.archlinux.org/title/Genfstab) for more information.

### Options for `main`

#### `genfstab_chroot_path`

Type: `str`, **required**.

This path is used as parameter _root_ for `genfstab`. The `/etc/fstab` file will be placed under this path. For example: `genfstab_chroot_path=/mnt` will write the fstab file to `/mnt/etc/fstab`.

## Dependencies

None.

## Project Information

This role is part of the Ansible collection [lingfra.system][collection_url].
For more information, see the collections [README](../../README.md) file.

[collection_url]: https://codeberg.org/lingfra/ansible-collection-lingfra-system
<!-- END_ANSIBLE_DOCS -->
