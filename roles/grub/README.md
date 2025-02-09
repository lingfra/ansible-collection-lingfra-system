<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: lingfra.system.grub

Configures GRUB and generates its config.

## Supported Platforms

Not specified.

## Entrypoint `main` - Main entry point for grub role

This role templates the GRUB configuration file and generates the boot config.

Refer to the [grub upstream documentation](https://www.gnu.org/software/grub/manual/grub/html_node/Simple-configuration.html) for more information about the `grub_conf_*` variables.
Another useful resource for GRUB configuration is [GRUB (ArchWiki)](https://wiki.archlinux.org/title/GRUB).

### Options for `main`

#### `grub_chroot_path`

Type: `str`, optional.

If this variable is specified, the GRUB configuration file will be templated inside the chroot, aswell as the bootloader builded.

#### `grub_conf_cmdline_linux_default`

Type: `list of 'str'`, Default: `[]`.



#### `grub_conf_cmdline_linux`

Type: `list of 'str'`, Default: `[]`.



#### `grub_conf_default`

Type: `str`, Default: `0`.



#### `grub_conf_disable_os_prober`

Type: `bool`, Default: `True`.



#### `grub_conf_disable_recovery`

Type: `bool`, Default: `False`.



#### `grub_conf_distributor`

Type: `str`, Default: `Arch`.



#### `grub_conf_extra_options`

Type: `dict`, optional.

GRUB has many configuration options and supporting them would be to much work. This variable can be used to specify the options as key/value pairs.

#### `grub_conf_gfxmode`

Type: `str`, Default: `auto`.



#### `grub_conf_gfxpayload_linux`

Type: `str`, Default: `keep`.



#### `grub_conf_preload_modules`

Type: `list of 'str'`, Default: `['part_gpt', 'part_msdos']`.



#### `grub_conf_savedefault`

Type: `bool`, Default: `False`.



#### `grub_conf_terminal_input`

Type: `str`, Default: `console`.



#### `grub_conf_terminal_output`

Type: `str`, Default: `console`.



#### `grub_conf_timeout`

Type: `int`, Default: `5`.



#### `grub_conf_timeout_style`

Type: `str`, Default: `menu`.



*Choices:* `countdown`, `hidden`, `menu`


#### `grub_defaults_path`

Type: `str`, Default: `/etc/default/grub`.

Path to the GRUB configuration file.

#### `grub_mkconfig_output_path`

Type: `str`, Default: `/boot/grub/grub.cfg`.

Specifies output path for the generation of the GRUB configuration file.

#### `grub_install_target`

Type: `str`, **required**.

The target architecture of your computer.  - `i386-efi` for UEFI (32 bit) - `i386-pc` for BIOS - `x86_64-efi` for UEFI (64 bit)

*Choices:* `i386-efi`, `i386-pc`, `x86_64-efi`


#### `grub_install_path`

Type: `str`, **required**.

The path where GRUB should be installed.  For BIOS systems this is the block device. And for UEFI systems this is the EFI directory.

#### `grub_install_extra_args`

Type: `list of 'str'`, optional.

Extra arguments for the installation of GRUB.

## Dependencies

None.

## Project Information

This role is part of the Ansible collection [lingfra.system][collection_url].
For more information, see the collections [README](../../README.md) file.

[collection_url]: https://codeberg.org/lingfra/ansible-collection-lingfra-system
<!-- END_ANSIBLE_DOCS -->
