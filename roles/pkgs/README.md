<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: lingfra.system.pkgs

Install and remove system packages.

## Supported Platforms

Not specified.

## Entrypoint `main` - Main entry point for pkgs role

This role installs and removes packages on the system.

It provides multiple scopes to define packages, which are merged.
The first scope is `pkgs_present__host` as the most specific scope for a single host.
It is recommended to set this variable in `host_vars` only.
The second scope is `pkgs_present__global`.
This is a dictionary of lists.
The possible keys are a set of the possible combinations of the following Jinja2 expressions based on the Ansible facts `{{ ansible_distribution ~ ansible_distribution_major_version}}`, `{{ ansible_distribution }}` and the special key `all`.
All lists matching keys from the `pkgs_present__global` for the hosts are merged with `pkgs_present__host` to one list `pkgs_present`.
The same applies to the `pkgs_absent` variables, see [`vars/main.yaml`](./vars/main.yaml).

Start the role with verbosity level 2 (`-vv`) to get information on the used variables for the merged lists.

Please note that it is not allowed to define a package as both present and absent.
If this is the case, the role fails.

### Options for `main`

#### `pkgs_present__global`

Type: `dict`, optional.

Global dictionary specifying packages per distribution, which should be installed. It is recommended to set this variable only in `group_vars/all`.

#### `pkgs_present__host`

Type: list of `str`, Default: `[]`.

List of packages, which should be **present** (installed if missing) on the target host. It is recommended to set this variable only in `host_vars` for a single host.

#### `pkgs_absent__global`

Type: `dict`, optional.

Global dictionary specifying packages per distribution, which should be removed. It is recommended to set this variable only in `group_vars/all`.

#### `pkgs_absent__host`

Type: list of `str`, Default: `[]`.

List of packages, which should be **absent** (removed if installed) on the target host. It is recommended to set this variable only in `host_vars` for a single host.

## Dependencies

None.

## Project Information

This role is part of the Ansible collection [lingfra.system][collection_url].
For more information, see the collections [README](../../README.md) file.

[collection_url]: https://github.com/lingfra/ansible-collection-lingfra-system
<!-- END_ANSIBLE_DOCS -->
