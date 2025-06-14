<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: lingfra.system.bootstrap_arch_linux

Meta-role for bootstrapping Arch Linux in a chroot.

## Supported Platforms

Not specified.

## Entrypoint `main` - Main entry point for lingfra.system.bootstrap_arch_linux role

This is a meta role, which is used to install an Arch Linux system.
It imports other roles of this collection, but sets the necessary variables to install them in a chroot.

### Options for `main`

#### `bootstrap_arch_linux_chroot_path`

Type: `str`, Default: `/target`.

The path of the chroot.

#### `bootstrap_arch_linux_device`

Type: `str`, **required**.

The device, on which the system should be installed.

#### `bootstrap_arch_linux_hostname`

Type: `str`, **required**.

The hostname of the new host.

#### `bootstrap_arch_linux_root_authorized_ssh_key`

Type: `str`, **required**.

SSH key, which is added to the authorized_keys file of the root user.

#### `bootstrap_arch_linux_network_device`

Type: `str`, Default: `en*`.

Name of the network device of the target host. The default of `en*` should match most devices. This variable can be used to either customize the matching if it does not work or hardcode a network device name.

#### `bootstrap_arch_linux_pacstrap_packages`

Type: `list of 'str'`, Default: `['linux', 'linux-firmware', 'base', 'btrfs-progs', 'cryptsetup', 'e2fsprogs', 'efibootmgr', 'grub', 'lvm2', 'man-db', 'man-pages', 'neovim', 'openssh', 'python', 'qemu-guest-agent', 'reflector', 'sudo', 'tmux']`.

List of packages to be installed in the new system. The default contains the most common packages. You may want to specify your own list containing only packages needed for your installation.

#### `bootstrap_arch_linux_static_ip`

Type: `dict of 'bootstrap_arch_linux_static_ip' options`, optional.

Static IP for the newly bootstrapped host. When this option is undefined DHCP is activated. If an IP is provided DHCP will be deactivated.

**Options:**

- **`address`** (Type: `str`, **required**).

  The static IP itself, e. g. 192.168.1.55/24

- **`gateway`** (Type: `str`, **required**).

  Gateway of the network, e. g. 192.168.1.1

## Dependencies

None.

## Project Information

This role is part of the Ansible collection [lingfra.system][collection_url].
For more information, see the collections [README](../../README.md) file.

[collection_url]: https://codeberg.org/lingfra/ansible-collection-lingfra-system
<!-- END_ANSIBLE_DOCS -->
