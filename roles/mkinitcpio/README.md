# Ansible Role: mkinitcpio

Installs and configures
[mkinitcpio](https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio/).
Optionally setup
[mkinitcpio-systemd-tool](https://github.com/random-archer/mkinitcpio-systemd-tool)
for remote root device decryption over SSH.

The initial motivation behind this role was to define mkinitcpio configuration
in Ansible `host_vars`. Especially for the `HOOKS=` array it is important that
the necessary hooks are loaded in the right order. I repeatedly ended up reading
the [mkinitcpio ArchWiki entry](https://wiki.archlinux.org/title/Mkinitcpio) to
validate my configuration on diverse hosts. With this role it is possible to
manage all mkinitcpio configurations in a central space: the Ansible playbook
directory. The bash arrays contained in `/etc/mkinitcpio.conf` can be configured
with YAML lists, which are much more reader-friendly. In addition the YAML lists
allow clearer comments to single modules.

## Features

- Template `mkinitcpio.conf`. Every configuration value can be templated, see
[templates/mkinitcpio.conf.j2](./templates/mkinitcpio.conf.j2).
- Customize path of `mkinitcpio.conf`. Useful when configuring within a chrooted
environment, e. g. when installing Arch Linux.
- Build the initramfs.
  - Restores previous configuration in case of an error.
- Install and configure `mkinitcpio-systemd-tool` for remote device decryption
over SSH.

## Limitations

- Does only re-create the initramfs when `mkinitcpio.conf` is changed. For
changes of the `mkinitcpio-systemd-tool` configuration you need to execute
`mkinitcpio -P` manually.
- `mkinitcpio-systemd-tool` specific: By default, the timeout for entering the
password takes effect after 90 seconds. It is possible to add the `timeout=`
parameter in the 4th field in the crypttab configuration. While
**[systemd-cryptsetup-generator(8)](https://man.archlinux.org/man/core/systemd/systemd-cryptsetup-generator.8.en)**
respects this and sets the timeout in the resulting
`systemd-cryptsetup@root.service` in the initramfs this does work only
partially. When defining a timeout less than 90 seconds the timeout takes effect
then. But setting a timeout higher than 90 seconds has not effect. A workaround
is to set `rootflags=x-systemd.device-timeout=0` (0 disables timeout) in the
kernel command line. This role does not modify kernel parameters and therefore
this need to be done manually if desired. See also
<https://wiki.archlinux.org/title/Dm-crypt/System_configuration#Timeout>.

## Requirements

A system using
[mkinitcpio](https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio/) for
initramfs generation. This properly is the case then using [Arch
Linux](https://archlinux.org/).

This role has been tested only on Arch Linux machines.

## Role Variables

### External Variables

None.

### Public Role Variables

Control flow and meta variables:

- `mkinitcpio_build_initramfs` (boolean), default `true`. Wether initramfs
should be build or not.
- `mkinitcpio_conf_path` (string), default `"/etc/mkinitcpio.conf"`. Path of the
mkinitcpio config file.
- `mkinitcpio_systemd_tool_setup` (boolean), default `false`. Wether
systemd-tool should be installed and configured or not.

The main scope of this role is to template the `mkinitcpio` configuration. All
available fields of `mkinitcpio.conf` are available as template variables. Refer
to **[mkinitcpio.conf(5)](https://man.archlinux.org/man/mkinitcpio.conf.5)** for
a description. Another useful resource is the example `mkinitcpio.conf` in the
[upstream repository](https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio/-/blob/master/mkinitcpio.conf).
For the sake of readability the bash arrays are defined as YAML lists here and
converted to bash arrays in the template. Following variables are available:

- `mkinitcpio_conf_binaries` (list), default `[]`.
- `mkinitcpio_conf_files` (list), default `[]`.
- `mkinitcpio_conf_hooks` (list), default `["base", "udev", "autodetect",
"microcode", "modconf", "kms", "keyboard", "keymap", "consolefont", "block",
"filesystems", "fsck"]`.
- `mkinitcpio_conf_modules` (list), default `[]`.
- `mkinitcpio_conf_compression` (string), default undefined.
- `mkinitcpio_conf_compression_options ` (string), default undefined.
- `mkinitcpio_conf_modules_decompress` (string), default undefined.

Following variables are for configuring systemd-tool. They only need to be
modified if you set `mkinitcpio_systemd_tool_setup` to `true`:

- `mkinitcpio_systemd_tool_crypttab_entry` (list): One entry for the crypttab of
systemd-tool, which lays under `/etc/mkinitcpio-systemd-tool/config/crypttab`. A
list with a maximum of 4 fields is expected. The four fields correspondent to
the fields of crypttab (name, device, password and options), see
**[crypttab(5)](https://man.archlinux.org/man/crypttab.5.en)** for details and
the [defaults](./defaults/main.yaml) for an example. Customizing this variable
**is mandatory** when using systemd-tool.
- `mkinitcpio_systemd_tool_fstab_entry` (list): One entry for the fstab of
systemd-tool, which lays under `/etc/mkinitcpio-systemd-tool/config/fstab`. A
list with 6 fields is expected. The six fields correspondent to fstab (device,
dir, type, options, dump, fsck), see
**[fstab(5)](https://man.archlinux.org/man/fstab.5)** for details and the
[defaults](./defaults/main.yaml) for an example. Customizing this variable **is
mandatory** if your mapped device has another name than `root`.
- `mkinitcpio_systemd_tool_ssh_pub_key` (string), default `id_ed25519`. SSH
public key for early userspace unlocking access. Need to exist under `~/.ssh/`
on the control host. As systemd-tool uses tinysshd as SSH server only keys of
type ed25519 are supported, see
**[tinysshd(8)](https://man.archlinux.org/man/tinysshd.8.en)**.

### Internal Role Variables

- `mkinitcpio_systemd_tool_packages` (list): Dependencies needed for
systemd-tool to work.

## Dependencies

None.
