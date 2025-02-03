<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: lingfra.system.pacman

Configures the pacman package manager and its mirrors.

## Features

- Configure Pacman itself
- Configure custom mirrors for Pacman...
- ... or [Reflector](https://wiki.archlinux.org/title/Reflector)
- Configure [Paccache](https://man.archlinux.org/man/paccache.8) for regular
package cache cleanings
- Initialize Pacmans trust database

## Supported Platforms

Not specified.

## Entrypoint `main` - Main entry point for pacman role

This role configures the pacman package manager.
It has special handling for setting up an initial system with the options [`pacman_init_keyring`](#pacman_init_keyring) and [`pacman_upgrade_system`](#pacman_upgrade_system). Note that these options are not idempotent and should only be used for initial provisioning.
The other scope of this role is to maintain the pacman repositories and mirrors.
You can specify the available repositories in [`pacman_repos`](#pacman_repos).
For configuring the main mirror the variable [`pacman_server`](#pacman_server) is available and the `/etc/pacman.d/mirrorlist` can be configured by either [`pacman_mirrorlist`](#pacman_mirrorlist) or [`pacman_reflector`](#pacman_reflector). After configuring a mirrorlist you may want to set [`pacman_server`](#pacman_server) to `''`.

### Options for `main`

#### `pacman_contrib`

Type: `bool`, Default: `True`.

Whether the [pacman-contrib](https://archlinux.org/packages/extra/x86_64/pacman-contrib/) package should be present or not. [pacman-contrib](https://gitlab.archlinux.org/pacman/pacman-contrib) provides extra scripts for interacting with pacman.

#### `pacman_init_keyring`

Type: `bool`, Default: `False`.

Initialize the pacman keyring.

#### `pacman_mirrorlist`

Type: `list of 'str'`, Default: `[]`.

Custom list of mirrors for pacman. Mutually exclusive with [`pacman_reflector`](#pacman_reflector).

#### `pacman_paccache`

Type: `bool`, Default: `False`.

Installs paccache and enables the timer for regular pacman cache cleaning. Refer to [**paccache(8)**](https://man.archlinux.org/man/paccache.8) for more information. Paccache is part of [pacman-contrib](https://archlinux.org/packages/extra/x86_64/pacman-contrib/) and therefore [`pacman_contrib`](#pacman_contrib) need to be `true`.

#### `pacman_reflector`

Type: `bool`, Default: `False`.

Whether [reflector](https://wiki.archlinux.de/title/Reflector) should be installed and activated or not. Refer to [**reflector(1)**](https://man.archlinux.org/man/reflector.1) for more information. Mutually exclusive with [`pacman_mirrorlist`](#pacman_mirrorlist).

#### `pacman_reflector_country`

Type: `str`, optional.

The country (or countries) reflector should the mirrors limit to.

#### `pacman_repos`

Type: `list of 'str'`, Default: `['core', 'extra']`.

List of official Arch Linux repositories to be enabled.

**Choices:**

- `core`
- `core-testing`
- `extra`
- `extra-testing`
- `gnome-unstable`
- `kde-unstable`
- `multilib`
- `multilib-testing`
- `testing`

#### `pacman_server`

Type: `str`, Default: `https://mirror.rackspace.com/archlinux/$repo/os/$arch`.

The main mirror server for the official Arch Linux repositories. Will have precedence over the mirrors specified in `/etc/pacman.d/mirrorlist`. The default of this variable should be a worldwide available pacman mirror as returned by [Pacman Mirrorlist Generator](https://archlinux.org/mirrorlist/). If this mirror deprecated some day, please open an issue. This variable has a default primary for bootstraping reasons. If you do not want specify a main server for official pacman repositories set this variable to an empty string.

#### `pacman_upgrade_system`

Type: `bool`, Default: `False`.

Whether or a full system upgrade should be done. This is a non-idempotent action and therefore only recommended for the first provisioning. In the case of first provisioning this should be used together with `pacman_init=true`.

## Dependencies

None.

## Project Information

This role is part of the Ansible collection [lingfra.system][collection_url].
For more information, see the collections [README](../../README.md) file.

[collection_url]: https://codeberg.org/lingfra/ansible-collection-lingfra-system
<!-- END_ANSIBLE_DOCS -->
