<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: lingfra.system.time

Configures time information.

## Supported Platforms

Not specified.

## Entrypoint `main` - Main entry point for time role

Running the role form this entrypoint configures time information on the system.
Note that this role does not setup any (S)NTP daemon, there a separate roles for that.

### Options for `main`

#### `time_chroot_path`

Type: `str`, optional.

If specified, all actions of this role are executed in the chroot directory.

#### `time_zone`

Type: `str`, Default: `Etc/UTC`.

The time zone information. The notation is based on the tz database and is in the format _Region/City_. See [List of tz database time zone (Wikipedia)](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) for a list of possible values. The role will create a symlink from the corresponding entry in `/usr/share/zoneinfo/Region/City` to `/etc/localtime`.

#### `time_generate_adjtime`

Type: `bool`, Default: `False`.

If set to `true`, generates `/etc/adjtime` by running `hwclock --systohc`. Refer to [**hwclock(8)**](https://man.archlinux.org/man/hwclock.8) for more information.  As this role will run mostly on VMs the default is `false`. See [this servervault thread](https://serverfault.com/questions/28803/what-happens-when-you-sync-your-hardware-clock-in-a-vm) for more information about hardware clock in a VM.

## Dependencies

None.

## Project Information

This role is part of the Ansible collection [lingfra.system][collection_url].
For more information, see the collections [README](../../README.md) file.

[collection_url]: https://codeberg.org/lingfra/ansible-collection-lingfra-system
<!-- END_ANSIBLE_DOCS -->
