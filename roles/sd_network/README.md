<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: lingfra.system.sd_network

Configure systemd-network to create VLANs and bridge devives.

## Supported Platforms

Not specified.

## Entrypoint `main` - Main entry point for sd_network role

This role is used to interpret tagged VLANs on (multiple) network devices (interfaces). To accomplish this, multiple concepts of [systemd-network](https://www.freedesktop.org/software/systemd/man/latest/systemd.network.html) are stacked.
This results in five levels of configuration:

1. Bind interface to VLAN networks.
2. Define the VLAN networks.
3. Define a bridge for every VLAN.
4. Bind VLAN network to corresponding bridge.
5. Configure the bridge. Currently, the only option is to enable or disable DHCP.

Starting from this entry point, the tasks [`device.yaml`](./tasks/device.yaml) are included. This is done for every list item in [`sd_network_device_vlan_list`](#sd_network_device_vlan_list). The tasks in [`device.yaml`](./tasks/device.yaml) make the basic configuration for the corresponding network device and create an accumulated VLAN list, which is needed in the next step. The next step is to include the [`vlan.yaml`](./tasks/vlan.yaml) for every specified VLAN.

### Options for `main`

#### `sd_network_device_vlan_list`

Type: `list of dicts of 'sd_network_device_vlan_list' options`, Default: `[]`.

This list of dictionaries is the main configuration interface for this role. Every list item consists of a device name and a list of VLANs, which should be interpreted from this device. When this list is empty (the default) no actions are done.

**Options:**

- `config_dir` (Type: `str`, Default: `/etc/systemd/network`).

  Specifies the configuration parent directory for the network configuration files.

- **`device`** (Type: `str`, **required**).

  The device the VLANs should be bound to. Need to be present on the target host.

- **`vlan_list`** (Type: `list of dicts of 'vlan_list' options`, **required**).

  List of VLANs associated with the device.

  **Options:**

  - **`id`** (Type: `int`, **required**).

    Specifies the VLAN ID. This should be the same as configured in the router on the port.

  - `address` (Type: `str`, optional).

    A static address for the interface. It is required to specify a gateway too, if an address is specified.

  - `create_bridge` (Type: `bool`, optional).

    Whether a bridge device for this VLAN should be created or not. If unspecified the value of `sd_network_create_bridge_default` is used. When this is set to `false`, the bridge configuration files (`30-bridge.netdev` and `50-bridge.network`) are not created . However, the filenames are still composed and used to delete possible leftover configuration from previous executions.

  - `dhcp` (Type: `bool`, optional).

    Whether DHCP should be activated on the resulting interface or not. If unspecified the value of [`sd_network_dhcp_default`](#sd_network_dhcp_default) is used. Depending if a bridge for this VLAN is created or not, DHCP is activated at different places. When a bridge is assigned to the VLAN, then DHCP is specified in `50-bridge.network`. If the VLAN has no corresponding bridge DHCP is activated in `40-vlan.network`.

  - `dns` (Type: `str`, optional).

    DNS server, useful for static configuration or to overwrite the server provided by DHCP.

  - `gateway` (Type: `str`, optional).

    If an address is specified it is required to specify a gateway too.

  - `ipv6_accept_ra` (Type: `bool`, optional).

    Whether IPv6 Router Announcements (RA) should be accepted or not (need to be true to get an IPv6 address).

#### `sd_network_create_bridge_default`

Type: `bool`, Default: `True`.

This variable defines a fallback for the field `sd_network_device_vlan_list.vlan_list.create_bridge`, refer to the documentation of that option for more information. By default this is `true`. This leads to the creation of a bridge for every VLAN.

#### `sd_network_dhcp_default`

Type: `bool`, Default: `False`.

This variable defines a fallback for the field `sd_network_device_vlan_list.vlan_list.dhcp`, refer to the documentation of that option for more information. By default this is `false` to avoid accidently adding the host to multiple networks.

### Examples for `main`

```yaml
- name: Import role lingfra.system.sd_network
  ansible.builtin.import_role:
    name: lingfra.system.sd_network
  vars:
    sd_network_device_vlan_list:
      - device: enp3s0
        vlan_list:
          - id: 101
            dhcp: true
            create_bridge: false
          - id: 102
            dhcp: false
          - id: 103
          - id: 104

      # Config for the same device, but in another directory.
      # E. g. for mkinitcpio-systemd-tool config.
      - device: enp3s0
        config_dir: /etc/mkinitcpio-systemd-tool/network
        vlan_list:
          - id: 101
            create_bridge: false
            dhcp: false
            address: 192.168.101.10/24
            gateway: 192.168.101.1
```

## Dependencies

None.

## Project Information

This role is part of the Ansible collection [lingfra.system][collection_url].
For more information, see the collections [README](../../README.md) file.

[collection_url]: https://github.com/lingfra/ansible-collection-lingfra-system
<!-- END_ANSIBLE_DOCS -->
