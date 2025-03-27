<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: lingfra.system.sd_timesyncd

Configures systemd-timesyncd.

## Supported Platforms

Not specified.

## Entrypoint `main` - Main entry point for sd_timesyncd role

This role configures systemd-timesyncd on the target hosts.
The options will be set in drop-in files under `/etc/systemd/timesyncd.conf.d`.
Please refer to [**timesyncd.conf(5)**]() for details on the `sd_timesyncd_conf_*` variables.

### Options for `main`

#### `sd_timesyncd_conf_ntp`

Type: `list of 'str'`, Default: `['0.pool.ntp.org', '1.pool.ntp.org', '2.pool.ntp.org', '3.pool.ntp.org']`.



#### `sd_timesyncd_conf_fallback_ntp`

Type: `list of 'str'`, optional.



## Dependencies

None.

## Project Information

This role is part of the Ansible collection [lingfra.system][collection_url].
For more information, see the collections [README](../../README.md) file.

[collection_url]: https://codeberg.org/lingfra/ansible-collection-lingfra-system
<!-- END_ANSIBLE_DOCS -->
