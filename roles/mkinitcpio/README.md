<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: lingfra.system.mkinitcpio

Configures mkinitcpio and builds the initramfs.

The original motivation for this role was to define the
[**mkinitcpio(8)**](https://man.archlinux.org/man/mkinitcpio.8.en) configuration
in Ansible `host_vars`. Especially for the `HOOKS=` array, it is important that
the required hooks are loaded in the correct order. I ended up repeatedly
reading the [mkinitcpio ArchWiki
entry](https://wiki.archlinux.org/title/Mkinitcpio) to validate my configuration
on various hosts. With this role, it is possible to manage all mkinitcpio
configurations in one central location: the Ansible inventory. The bash arrays
contained in `/etc/mkinitcpio.conf` can be configured using YAML lists, which
are much more reader friendly. In addition, the YAML lists allow for clearer
comments on individual modules.

## Features

- Template `mkinitcpio.conf`. Any configuration value can be templated, see
[templates/mkinitcpio.conf.j2](./templates/mkinitcpio.conf.j2).
- Customizable path to `mkinitcpio.conf` with the variable
[`mkinitcpio_conf_path`](#mkinitcpio_conf_path).
- Support for chrooted environment, see
[`mkinitcpio_chroot_path`](#mkinitcpio_chroot_path).
- Build the initramfs.
  - Restores previous configuration and rebuilds in case of failure.
- Optionally import
[lingfra.system.mkinitcpio_sd_tool](https://codeberg.org/lingfra/ansible-collection-lingfra-system/src/branch/main/roles/mkinitcpio_sd_tool/README.md)
to configure remote root device unlocking over SSH. See
[`mkinitcpio_sd_tool_enable`](#mkinitcpio_sd_tool_enable).

## Requirements

A system that uses
[mkinitcpio](https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio/) for
initramfs generation. This properly is the case when using [Arch
Linux](https://archlinux.org/).

This role has only been tested on Arch Linux machines.

## Supported Platforms

Not specified.

## Entrypoint `main` - Main entry point for mkinitcpio role

The main scope of this role's entrypoint is to template the `mkinitcpio` configuration and then build the initramfs.
If it is not desired to build the initramfs, it is possible to disable it by setting [`mkinitcpio_build_initramfs`](#mkinitcpio_build_initramfs) to `false`.
Note that it is not recommended to disable the building of the initramfs, because this role has error handling and restoring mechanisms built in.

All available fields for `mkinitcpio.conf` are available as template variables.
The bash arrays are defined here as YAML lists and converted to bash arrays in the template.
Refer to [**mkinitcpio.conf(5)**](https://man.archlinux.org/man/mkinitcpio.conf.5) for a description of the options.
Another useful resource is the example `mkinitcpio.conf` in the [upstream repository](https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio/-/blob/master/mkinitcpio.conf).

See [`mkinitcpio_sd_tool_enable`](#mkinitcpio_sd_tool_enable) to install and configure mkinitcpio-systemd-tool for remote root device unlocking over SSH.

### Options for `main`

#### `mkinitcpio_build_initramfs`

Type: `bool`, Default: `True`.

Whether initramfs should be build or not.

#### `mkinitcpio_chroot_path`

Type: `str`, optional.

If you are configuring mkinitcpio in a chroot, set this variable to the directory where the chroot is located. This path will then prepended to the [`mkinitcpio_conf_path`](#mkinitcpio_conf_path) and the initramfs image will be built in the chroot.

#### `mkinitcpio_conf_path`

Type: `str`, Default: `/etc/mkinitcpio.conf`.

Path of the mkinitcpio configuration file.

#### `mkinitcpio_conf_binaries`

Type: `list of 'str'`, Default: `[]`.

Refer to [**mkinitcpio.conf(5)**](https://man.archlinux.org/man/mkinitcpio.conf.5) variable `BINARIES`.

#### `mkinitcpio_conf_compression`

Type: `str`, optional.

Refer to [**mkinitcpio.conf(5)**](https://man.archlinux.org/man/mkinitcpio.conf.5) variable `COMPRESSION`.

#### `mkinitcpio_conf_compression_options`

Type: `str`, optional.

Refer to [**mkinitcpio.conf(5)**](https://man.archlinux.org/man/mkinitcpio.conf.5) variable `COMPRESSION_OPTIONS`.

#### `mkinitcpio_conf_files`

Type: `list of 'str'`, Default: `[]`.

Refer to [**mkinitcpio.conf(5)**](https://man.archlinux.org/man/mkinitcpio.conf.5) variable `FILES`.

#### `mkinitcpio_conf_hooks`

Type: `list of 'str'`, Default: `['base', 'udev', 'autodetect', 'microcode', 'modconf', 'kms', 'keyboard', 'keymap', 'consolefont', 'block', 'filesystems', 'fsck']`.

Refer to [**mkinitcpio.conf(5)**](https://man.archlinux.org/man/mkinitcpio.conf.5) variable `HOOKS`. In addition, see the [Common Hooks](https://wiki.archlinux.org/title/Mkinitcpio#Common_hooks) section of the [Mkinitcpio article in the Arch Wiki](https://wiki.archlinux.org/title/Mkinitcpio).

#### `mkinitcpio_conf_modules`

Type: `list of 'str'`, Default: `[]`.

Refer to [**mkinitcpio.conf(5)**](https://man.archlinux.org/man/mkinitcpio.conf.5) variable `MODULES`.

#### `mkinitcpio_conf_modules_decompress`

Type: `str`, optional.

Refer to [**mkinitcpio.conf(5)**](https://man.archlinux.org/man/mkinitcpio.conf.5) variable `MODULES_DECOMPRESS`.

#### `mkinitcpio_force_build`

Type: `bool`, Default: `False`.

Build / rebuild the new initramfs regardless of change state.

#### `mkinitcpio_sd_tool_enable`

Type: `bool`, Default: `False`.

Whether or not to install and configure [mkinitcpio-systemd-tool](https://github.com/random-archer/mkinitcpio-systemd-tool). If set to `true`, the role [lingfra.system.mkinitcpio_sd_tool](https://codeberg.org/lingfra/ansible-collection-lingfra-system/src/branch/main/roles/mkinitcpio_sd_tool/README.md) will be imported.

## Entrypoint `internal` - General internal role variables

This is a synthetic entry point, which is used for custom argument validation and documentation. Your playbook will fail if you use this entry point.

### Options for `internal`

#### `mkinitcpio_built_command_argv`

Type: `list of 'str'`, **required**.

The command to built the initramfs image.

## Dependencies

None.

## Example Playbook

```yaml
- name: Import playbook lingfra.system.mkinitcpio
  ansible.builtin.import_playbook: lingfra.system.mkinitcpio
  vars:
    mkinitcpio_conf_hooks:
      - "base"
      - "systemd"
      - "autodetect"
      - "microcode"
      - "modconf"
      - "kms"
      - "keyboard"
      - "sd-vconsole"
      - "block"
      - "filesystems"
      - "fsck"
      - "systemd-tool"
    mkinitcpio_sd_tool_enable: true
    mkinitcpio_sd_tool_crypttab_entries:
      - name: root
        uuid: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    mkinitcpio_sd_tool_ssh_pub_key: ssh-ed25519 AAAAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX your key comment
```

## Project Information

This role is part of the Ansible collection [lingfra.system][collection_url].
For more information, see the collections [README](../../README.md) file.

[collection_url]: https://codeberg.org/lingfra/ansible-collection-lingfra-system
<!-- END_ANSIBLE_DOCS -->
