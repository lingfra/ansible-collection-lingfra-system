<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: lingfra.system.openssh_server

Configures OpenSSH server.

## Supported Platforms

Not specified.

## Entrypoint `main` - Main entry point for openssh_server role

Running the role from this entrypoint installs and configures the OpenSSH server.

### Options for `main`

#### `openssh_server_chroot_path`

Type: `str`, optional.

If specified, all actions of this role are executed in the chroot directory. Please note that some features do not work in a chroot.

#### `openssh_server_conf_enable_drop_ins`

Type: `bool`, Default: `True`.

Whether or not to load drop in files.

#### `openssh_server_conf_enable_sftp`

Type: `bool`, Default: `True`.

Whether or not to enable SFTP (SSH File Transfer Protocol).

#### `openssh_server_conf_authentication_methods`

Type: `list of 'str'`, Default: `['publickey']`.

Please be sure to read and understand this options before modifying it, see [**sshd_config(5)** AuthenticationMethods](https://man.archlinux.org/man/sshd_config.5.en#AuthenticationMethods) You can disable this option by setting it to `null` or an empty string. To mimic the example from the man page, set this variable to `['publickey,password', 'publickey,keyboard-interactive']`.

#### `openssh_server_conf_allow_users`

Type: `list of 'str'`, optional.

A list of allowed users to connect to the OpenSSH server. Won't be configured if omitted.

#### `openssh_server_conf_kex_algorithms`

Type: `list of 'str'`, optional.



#### `openssh_server_conf_ciphers`

Type: `list of 'str'`, optional.



#### `openssh_server_conf_macs`

Type: `list of 'str'`, optional.



#### `openssh_server_conf_host_key_algorithms`

Type: `list of 'str'`, optional.



#### `openssh_server_conf_ca_signature_algorithms`

Type: `list of 'str'`, optional.



#### `openssh_server_conf_hostbased_accepted_algorithms`

Type: `list of 'str'`, optional.



#### `openssh_server_conf_kbd_interactive_authentication`

Type: `bool`, Default: `False`.



#### `openssh_server_conf_listen_address_list`

Type: `list of 'str'`, optional.

List of addresses for OpenSSH to listen on. Will listen on all local addresses if unspecified.

#### `openssh_server_conf_max_auth_tries`

Type: `int`, Default: `3`.



#### `openssh_server_conf_password_authentication`

Type: `bool`, Default: `False`.



#### `openssh_server_conf_port`

Type: `int`, optional.

The port on which the OpenSSH server should be listen.

#### `openssh_server_conf_permit_empty_passwords`

Type: `bool`, Default: `False`.



#### `openssh_server_conf_permit_root_login`

Type: `bool`, Default: `False`.

Whether root is allowed to login over ssh or not.

#### `openssh_server_conf_pubkey_authentication`

Type: `bool`, Default: `True`.



#### `openssh_server_conf_pubkey_accepted_algorithms`

Type: `list of 'str'`, optional.



#### `openssh_server_conf_use_pam`

Type: `bool`, Default: `True`.



#### `openssh_server_drop_in_files`

Type: `list of dicts of 'openssh_server_drop_in_files' options`, optional.

List of drop-in files.

**Options:**

- **`name`** (Type: `str`, **required**).

  Name of the drop-in file, e. g. `30-auth

- `content` (Type: `str`, optional).

  Content of the drop-in file.

- `state` (Type: `str`, optional).

  Whether the file should be present or not.

  *Choices:* `absent`, `present`


#### `openssh_server_host_key_types`

Type: `list of 'str'`, Default: `['ed25519']`.



*Choices:* `ecdsa`, `ed25519`, `rsa`


#### `openssh_server_host_key_reset`

Type: `bool`, Default: `False`.

Setting this to true will delete all host keys. Use with care!

#### `openssh_server_install`

Type: `bool`, Default: `True`.

Whether the OpenSSH system packages should be installed or not.

#### `openssh_server_systemd_service_enable`

Type: `bool`, Default: `True`.

Whether the OpenSSH systemd service should be enabled or not. If the service is already running and this variable is set to `false` it disables the service. This option has no effect if [`openssh_server_chroot_path`](#openssh_server_chroot_path) is defined.

#### `openssh_server_systemd_service_restart`

Type: `bool`, Default: `True`.

Whether the OpenSSH systemd service should be (re-)started or not. This option has no effect if [`openssh_server_chroot_path`](#openssh_server_chroot_path) is defined.

### Examples for `main`

```yaml
# Showing some generic options
- name: Import role lingfra.system.openssh_server
  ansible.builtin.import_role:
    name: lingfra.system.openssh_server
  vars:
    # Limit listen address to one specific interface
    openssh_server_conf_listen_address_list:
      - 192.168.1.20
    # Changing port
    openssh_server_conf_port: 12345

# Configure OpenSSH server in a new chroot
- name: "Import role lingfra.system.openssh_server"
  ansible.builtin.import_role:
    name: lingfra.system.openssh_server
  vars:
    # If you configure your system in a chroot (e. g. when installing from live ISO or building an image)
    openssh_server_chroot_path: /target
    # For security root isn't allowed to login over SSH by default, but in this case we enable this
    openssh_server_conf_permit_root_login: true
    # Deleting possible pre-generated host keys, so new keys will be generated at first start (important for images)
    openssh_server_host_key_reset: true
    # The OpenSSH server package maybe is pre-installed and it could cause problems
    openssh_server_install: false

# Showing hardening
- name: "Import role lingfra.system.openssh_server"
  ansible.builtin.import_role:
    name: lingfra.system.openssh_server
  vars:
    # Hardening cryptography
    # Source: https://www.sshaudit.com/hardening_guides.html (2025)
    openssh_server_conf_ca_signature_algorithms:
      - sk-ssh-ed25519@openssh.com
      - ssh-ed25519
      - rsa-sha2-512
      - rsa-sha2-256

    openssh_server_conf_ciphers:
      - aes256-gcm@openssh.com
      - aes256-ctr
      - aes192-ctr
      - aes128-gcm@openssh.com
      - aes128-ctr

    openssh_server_conf_hostbased_accepted_algorithms:
      - sk-ssh-ed25519-cert-v01@openssh.com
      - ssh-ed25519-cert-v01@openssh.com
      - rsa-sha2-512-cert-v01@openssh.com
      - rsa-sha2-256-cert-v01@openssh.com
      - sk-ssh-ed25519@openssh.com
      - ssh-ed25519
      - rsa-sha2-512
      - rsa-sha2-256

    openssh_server_conf_host_key_algorithms:
      - sk-ssh-ed25519-cert-v01@openssh.com
      - ssh-ed25519-cert-v01@openssh.com
      - rsa-sha2-512-cert-v01@openssh.com
      - rsa-sha2-256-cert-v01@openssh.com
      - sk-ssh-ed25519@openssh.com
      - ssh-ed25519
      - rsa-sha2-512
      - rsa-sha2-256

    openssh_server_conf_kex_algorithms:
      - sntrup761x25519-sha512@openssh.com
      - curve25519-sha256
      - curve25519-sha256@libssh.org
      - diffie-hellman-group18-sha512
      - diffie-hellman-group-exchange-sha256
      - diffie-hellman-group16-sha512

    openssh_server_conf_macs:
      - hmac-sha2-512-etm@openssh.com
      - hmac-sha2-256-etm@openssh.com
      - umac-128-etm@openssh.com

    openssh_server_conf_pubkey_accepted_algorithms:
      - sk-ssh-ed25519-cert-v01@openssh.com
      - ssh-ed25519-cert-v01@openssh.com
      - rsa-sha2-512-cert-v01@openssh.com
      - rsa-sha2-256-cert-v01@openssh.com
      - sk-ssh-ed25519@openssh.com
      - ssh-ed25519
      - rsa-sha2-512
      - rsa-sha2-256
```

## Dependencies

None.

## Project Information

This role is part of the Ansible collection [lingfra.system][collection_url].
For more information, see the collections [README](../../README.md) file.

[collection_url]: https://codeberg.org/lingfra/ansible-collection-lingfra-system
<!-- END_ANSIBLE_DOCS -->
