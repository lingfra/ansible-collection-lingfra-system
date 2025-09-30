from pathlib import Path
import re
from ansible_collections.lingfra.system.plugins.filter.chroot import get_chrooted_path
from ansible.errors import AnsibleFilterError


def get_partition_block_device_names(parted_result):
    """
    This filter plugin parses the parted output and returns a dict with the
    partition name as key and the block device as value.
    """
    if not isinstance(parted_result, dict):
        raise AnsibleFilterError(
            "Input variable need the registered result from a parted module execution, which is of type dict."
        )

    result = {}

    device = parted_result["disk"]["dev"]

    for partition in parted_result["partitions"]:
        partition_key = partition.get("name", None)
        if not partition_key:
            partition_key = partition.get("num")
        if re.match("[a-z]", device[-1]):
            result[partition_key] = f"{device}{partition['num']}"
        elif re.match("[0-9]", device[-1]):
            result[partition_key] = f"{device}p{partition['num']}"
        else:
            raise AnsibleFilterError("An unexpected error occured.")

    return result


def get_partition_uuids(ansible_devices):

    result = {}

    for device_key in ansible_devices.keys():
        if len(ansible_devices[device_key]['links']['uuids']) > 0:
            result[f"/dev/{device_key}"] = ansible_devices[device_key]['links']['uuids']

        if ansible_devices[device_key]['partitions']:
            for partition_key in ansible_devices[device_key]['partitions'].keys():
                if len(ansible_devices[device_key]['partitions'][partition_key]['links']['uuids']) > 0:
                    result[f"/dev/{partition_key}"] = ansible_devices[device_key]['partitions'][partition_key]['links']['uuids']

    return result


def parse_lvs(lv_list, vg_name, chroot_path: None | str = None):
    """
    This filter plugin is used to parse the logical volume data structure from
    the role lingfra.system.partitions.
    """
    if not isinstance(lv_list, list):
        raise AnsibleFilterError(
            "Input variable for this filter need to be of type list."
        )
    if not isinstance(vg_name, str):
        raise AnsibleFilterError(
            "Input variable 'vg_name' for this filter need to be of type str."
        )

    result = []

    for lv in lv_list:
        if not isinstance(lv, dict):
            raise AnsibleFilterError(
                "Items of input list for this filter need to be of type dict."
            )

        volume = {
            "dev": f"/dev/mapper/{vg_name}-{lv['name']}",
            "fs_opts": None,
            "fs_type": lv.get("fstype", None),
            "swap": False,
            "lv": lv["name"],
            "mount_path": get_chrooted_path(lv.get("path", None), chroot_path),
            "name": lv["name"],
            "size": lv["size"],
            "vg": vg_name,
        }

        if lv.get("fstype", False) == "ext4":
            volume["fs_opts"] = f"-L lv-{lv['name']}"

        if lv.get("fstype", False) == "swap":
            volume["swap"] = True

        result.append(volume)

    return result


# Register the filters
class FilterModule(object):
    def filters(self):
        return {
            "parse_lvs": parse_lvs,
            "get_partition_block_device_names": get_partition_block_device_names,
            "get_partition_uuids": get_partition_uuids,
        }
