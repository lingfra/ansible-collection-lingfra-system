# Ansible Role: mkinitcpio

Installs and configures
[mkinitcpio](https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio/).


# Features


# Limitations


# Requirements

A system using
[mkinitcpio](https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio/) for
initramfs generation.


# Role Variables


## External Variables


## Public Role Variables


## Internal Role Variables


# Dependencies

None.


# Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Include role mkinitcpio
      ansible.builtin.include_role:
        name: mkinitcpio
```


# License

[UNLICENSE](./LICENSE)


# Author Information

lingling
