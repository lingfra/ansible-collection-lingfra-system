<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: lingfra.system.mkinitcpio_sd_tool

Installs and configures mkinitcpio-systemd-tool for remote root device decryption over SSH.

## Supported Platforms

Not specified.

## Entrypoint `main` - Main entry point for mkinitcpio_sd_tool role

This role makes the necessary preparations for using [mkinitcpio-systemd-tool](https://github.com/random-archer/mkinitcpio-systemd-tool).
The main scope is to configure networking for root device decryption over SSH in early initramfs.
Note that this role is intended to be imported by lingfra.system.mkinitcpio.
Therefore, this role does not rebuild the initramfs, which is done by [lingfra.system.mkinitcpio](https://github.com/lingfra/ansible-collection-lingfra-system/tree/main/roles/mkinitcpio/README.md).
However, this role does set the variable `mkinitcpio_sd_tool_changed`, which can be used for subsequent action after this role has finished.
This variable is taken into account by [lingfra.system.mkinitcpio](https://github.com/lingfra/ansible-collection-lingfra-system/tree/main/roles/mkinitcpio/README.md).

Note following limitation:
By default, the timeout for the password entry is 90 seconds.
It is possible to add the `timeout=` parameter in the `options` field of the crypttab configuration.
While [**systemd-cryptsetup-generator(8)**](https://man.archlinux.org/man/core/systemd/systemd-cryptsetup-generator.8.en) respects this and sets the timeout in the resulting `systemd-cryptsetup@root.service` in the initramfs, this works only partially.
If the timeout is less than 90 seconds, the timeout takes effect then.
But setting a timeout higher than 90 seconds will have not effect.
This can be fixed by setting `rootflags=x-systemd.device-timeout=0` (0 disables the timeout) at the kernel command line.
This role does not modify kernel parameters, so this must be done manually if desired.
See also <https://wiki.archlinux.org/title/Dm-crypt/System_configuration#Timeout>.

### Options for `main`

#### `mkinitcpio_sd_tool_chroot_dir`

Type: `str`, optional.

If configured, all actions (e.g. file templates, commands) will be executed in the chroot.  **Warning**: In my experiments, I haven't been able to built a working initramfs image in a chroot with systemd-tool configured. Be careful when using this option.

#### `mkinitcpio_sd_tool_crypttab_entries`

Type: list of dicts of `mkinitcpio_sd_tool_crypttab_entries` [options](#options-for-main--mkinitcpio_sd_tool_crypttab_entries), **required**.

A list of entries for the crypttab of systemd-tool, which is located at `/etc/mkinitcpio-systemd-tool/config/crypttab`. Refer to [**crypttab(5)**](https://man.archlinux.org/man/crypttab.5.en) for details on the options. It is **required** to specify your device(s) here.

#### `mkinitcpio_sd_tool_fstab_entries`

Type: list of `str`, Default: `[{'device': '/dev/mapper/root', 'dir': '/sysroot'}]`.

Entries for the fstab of systemd-tool for the early initramfs, which is located at `/etc/mkinitcpio-systemd-tool/config/fstab`. The arguments are just standard [**fstab(5)**](https://man.archlinux.org/man/fstab.5) options. If you only have one device to decrypt on boot, and you have named this `root` in your [`mkinitcpio_sd_tool_crypttab_entries`](#mkinitcpio_sd_tool_crypttab_entries), you can leave this variable at its default.

#### `mkinitcpio_sd_tool_ssh_pub_key`

Type: `str`, **required**.

SSH public keys for early userspace unlocking access. The keys are copied to an `authorized_keys` file in a custom location. Any keys not specified in this variable will be removed from the custom `authorized_keys` file! Add multiple keys by separating them with newlines. Since [mkinitcpio-systemd-tool](https://github.com/random-archer/mkinitcpio-systemd-tool) uses tinysshd as its SSH server, the keys must be of the type ed25519. Refer to [**tinysshd(8)**](https://man.archlinux.org/man/extra/tinyssh/tinysshd.8.en) for more information and to [**ssh-keygen(1)**](https://man.archlinux.org/man/ssh-keygen.1.en) if you need to generate a new key.

### Options for `main` > `mkinitcpio_sd_tool_crypttab_entries`

- **`name`** (Type: `str`, **required**).

  Name of the mapped device.

- **`uuid`** (Type: `str`, **required**).

  Device ID of the encrypted partition.

- `password` (Type: `str`, Default: `none`).

  Should be `none` to trigger password prompt.

- `options` (Type: `str`, Default: `luks`).

  Options for the crypttab entry.

- `state` (Type: `str`, Default: `present`).

  The state of the crypttab entry for mkinitcpio_sd_tool. If `absent`, the line with the matching `name` will be removed.

  _Choices:_ `present`, `absent`

### Options for `main` > `mkinitcpio_sd_tool_fstab_entries`

- **`device`** (Type: `str`, **required**).

- **`dir`** (Type: `str`, **required**).

- `type` (Type: `str`, Default: `auto`).

- `options` (Type: `str`, Default: `x-systemd.device-timeout=9999h`).

- `dump` (Type: `int`, Default: `0`).

- `fsck` (Type: `int`, Default: `0`).

## Entrypoint `internal` - General internal role variables

This is a synthetic entry point, which is used for custom argument validation and documentation. Your playbook will fail if you use this entry point.

### Options for `internal`

#### `mkinitcpio_sd_tool_authorized_keys_path`

Type: `str`, **required**.

Path to the authorized_key file for mkinitcpio-systemd-tool.

#### `mkinitcpio_sd_tool_crypttab_path`

Type: `str`, **required**.

Path to the crypttab file for mkinitcpio-systemd-tool.

#### `mkinitcpio_sd_tool_fstab_path`

Type: `str`, **required**.

Path to the fstab file for mkinitcpio-systemd-tool.

#### `mkinitcpio_sd_tool_packages`

Type: list of `str`, **required**.

Package dependencies needed for systemd-tool to work.

#### `mkinitcpio_sd_tool_units`

Type: list of `str`, **required**.

List of units that will be enabled for mkinitcpio-systemd-tool.

## Dependencies

None.

## Example Playbook

See the [Example Playbook section of lingfra.system.mkinitcpio](https://github.com/lingfra/ansible-collection-lingfra-system/tree/main/roles/mkinitcpio#example-playbook).

## Project Information

This role is part of the Ansible collection [lingfra.system][collection_url].
For more information, see the collections [README](../../README.md) file.

[collection_url]: https://github.com/lingfra/ansible-collection-lingfra-system
<!-- END_ANSIBLE_DOCS -->
