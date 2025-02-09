from __future__ import absolute_import, division, print_function

__metaclass__ = type
from pathlib import Path

from ansible.plugins.action import ActionBase
from ansible.errors import AnsibleError


class ActionModule(ActionBase):
    """
    This action plugin is used to run pacstrap on a target path.

    The module makes some checks:

        - target path must exist, be a directory and be writable
        - target path must be a mounted folder
        - if the pacman binary is found in the target folder, it is assumed
          that the folder already has been bootstrapped and no action is done.

    When all checks succeed then pacstrap will be executed on the target
    folder.
    """

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        _, new_module_args = self.validate_argument_spec(
            argument_spec={
                "path": {"type": "str", "required": True},
                "init_keyring": {"type": bool, "default": True},
                "executable": {"type": "str", "default": "pacstrap"},
                "packages": {"type": "list", "elements": "str", "default": []},
            }
        )

        result = {"changed": False, **new_module_args}

        # ensure access to target path

        module_stat_target_path_result = self._execute_module(
            module_name="ansible.builtin.stat",
            module_args={"path": new_module_args["path"]},
            task_vars=task_vars,
        )

        stat_target_path = module_stat_target_path_result.get("stat", {})
        result["stat_target_path"] = stat_target_path

        if not stat_target_path.get("exists", False):
            result["msg"] = "Target path does not exist."
            result["failed"] = True
            return result
        if not stat_target_path.get("isdir", False):
            result["msg"] = "Target path is not directory."
            result["failed"] = True
            return result
        if not stat_target_path.get("writable", False):
            result["msg"] = "Target path is not writable."
            result["failed"] = True
            return result

        # ensure target path is a mounted folder

        try:
            ansible_mounts = task_vars["ansible_mounts"]
        except KeyError:
            raise AnsibleError("The Ansible fact 'ansible_mounts' is not available.")

        mounted_folders = [m["mount"] for m in ansible_mounts]

        if new_module_args["path"] not in mounted_folders:
            result["msg"] = "Target path need to be a mounted folder."
            result["failed"] = True
            return result

        # Test if target folder is already bootstrapped

        test_file_path = Path(new_module_args["path"], "usr/bin/pacman")

        module_stat_test_file_result = self._execute_module(
            module_name="ansible.builtin.stat",
            module_args={"path": test_file_path},
            task_vars=task_vars,
        )

        stat_test_file = module_stat_test_file_result.get("stat", {})

        if stat_test_file.get("exists", False):
            result["msg"] = "Target seems to be already installed."
            return result

        # Compose pacstrap command

        pacstrap_argv = [new_module_args["executable"]]

        if new_module_args["init_keyring"]:
            pacstrap_argv.append("-K")

        pacstrap_argv.append(new_module_args["path"])
        pacstrap_argv.extend(["base", "linux"])
        pacstrap_argv.extend(new_module_args["packages"])

        # Run pacstrap with command module

        module_command_pacstrap_result = self._execute_module(
            module_name="ansible.builtin.command",
            module_args={"argv": pacstrap_argv},
            task_vars=task_vars,
        )

        return {**result, **module_command_pacstrap_result}
