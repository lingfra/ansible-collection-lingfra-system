<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: lingfra.system.partitions

Configures partitions for a device.

## Supported Platforms

Not specified.

## Entrypoint `main` - Main entry point for partitions role

This entry point creates the partitions on a device.

In the current state the role creates the following structure:

- part1: 1 MB bios boot
- part2: LVM root with 100% of free space

Afterwards logical volumes are created.
These are specified in [`partitions_logical_volumes`](#partitions_logical_volumes).

### Options for `main`

#### `partitions_chroot_path`

Type: `str`, optional.

If specified, all mounted paths will be subpaths of this.

#### `partitions_device`

Type: `str`, **required**.

The device, which partitions should be managed

#### `partitions_esp_mount_point`

Type: `str`, Default: `/boot`.

The mount point of the EFI system partition (EFI). Only applicable for UEFI systems. Please be sure to understand what you are doing before changing this value. Refer to [EFI system partition (ArchWiki)](https://wiki.archlinux.org/title/EFI_system_partition) for an overview.

#### `partitions_logical_volumes`

Type: `list of dicts of 'partitions_logical_volumes' options`, Default: `[{'name': 'root', 'fstype': 'ext4', 'path': '/', 'size': '10G'}, {'name': 'log', 'fstype': 'ext4', 'size': '2G', 'path': '/var/log'}, {'name': 'home', 'fstype': 'ext4', 'size': '2G', 'path': '/home'}, {'name': 'swap', 'fstype': 'swap', 'size': '2G'}]`.

List of logical volumes to be created on the device.

**Options:**

- `fstype` (Type: `str`, optional).

  The filesystem type. If ommited, the partitions won't be formatted. The choices are copied from [community.general.filesystem](https://docs.ansible.com/ansible/latest/collections/community/general/filesystem_module.html#parameter-fstype) module. Please open an if a newly added filesystem is missing.

  *Choices:* `bcachefs`, `btrfs`, `ext2`, `ext3`, `ext4`, `ext4dev`, `f2fs`, `lvm`, `ocfs2`, `reiserfs`, `xfs`, `vfat`, `swap`, `ufs`


- **`name`** (Type: `str`, **required**).

  Name of the logical volume.

- `path` (Type: `str`, optional).

  If provided, the logical volume will be mounted at this path. If [`partitions_chroot_path`](#partitions_chroot_path) is proveded, the paths will be mounted as subpaths of this.

- **`size`** (Type: `str`, **required**).

  Size of the logical volume, e. g. 10G, 250M or '100%FREE'. Refer to [**lvcreate(8)**](https://manpages.debian.org/jessie/lvm2/lvcreate.8.en.html) for more information on size notation. The suffixes are described for the `--size` option and the percent notation for `--extents`, repectivetaly.

#### `partitions_activate_swap`

Type: `bool`, Default: `False`.

Whether swap should be activated during runtime.

#### `partitions_system_type`

Type: `str`, Default: `bios`.

Depending if the system has a BIOS or an UEFI different partitions need to be created.

*Choices:* `bios`, `uefi`


#### `partitions_volume_group_name`

Type: `str`, Default: `vg0`.

Name of the volume group.

## Dependencies

None.

## Project Information

This role is part of the Ansible collection [lingfra.system][collection_url].
For more information, see the collections [README](../../README.md) file.

[collection_url]: https://codeberg.org/lingfra/ansible-collection-lingfra-system
<!-- END_ANSIBLE_DOCS -->
