<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: lingfra.system.apt_source

Configure APT sources on Deb-based systems.

## Supported Platforms

Not specified.

## Role Arguments

### Entrypoint `main` - Main entry point for apt_source role

This is a simple role, which deploys APT data sources based on the contents of `apt_source_repo_list`. Afterwards it updates the APT cache.

#### `apt_source_repo_list`

Type: `list of dicts of 'apt_source_repo_list' options`, Default: `[]`.

List of repositories (_data sources_) to add for APT. See [**sources.list(5)**](https://manpages.debian.org/stable/apt/sources.list.5.en.html) for an explanation of the options.

**Options:**

- `architectures` (Type: `str`, optional).

- `components` (Type: `list of 'str'`, optional).

- `enabled` (Type: `bool`, optional).

- **`name`** (Type: `str`, **required**).

- `signed_by` (Type: `str`, optional).

- `suites` (Type: `str`, optional).

- `types` (Type: `list of 'str'`, optional).

  **Choices:**

  - `deb`
  - `deb-src`

- `uris` (Type: `str`, optional).

## Dependencies

None.

## Example Playbook

```yaml
- name: Configure apt sources
  hosts: all
  tasks:
    - name: Import role lingfra.system.apt_source
      ansible.builtin.import_role:
        name: lingfra.system.apt_source
      vars:
        apt_source_repo_list:
          # add the backports suite for bookworm
          - name: bookworm-backports
            enabled: true
            types:
              - deb
              - deb-src
            uris:
              - https://deb.debian.org/debian
            suites: bookworm-backports
            components:
              - main
              - contrib
              - non-free
              - non-free-firmware

          # the postgresql upstream repository is signed by an external signature
          - name: postgres-upstream
            enabled: true
            types: deb
            signed_by: https://www.postgresql.org/media/keys/ACCC4CF8.asc
            architectures: amd64
            uris: https://apt.postgresql.org/pub/repos/apt
            suites: bookworm-pgdg
            components: main
```

## Project Information

This role is part of the Ansible collection [lingfra.system][collection_url].
For more information, see the collections [README](../../README.md) file.

[collection_url]: https://codeberg.org/lingfra/ansible-collection-lingfra-system
<!-- END_ANSIBLE_DOCS -->
