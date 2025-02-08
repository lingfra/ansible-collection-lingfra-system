from pathlib import Path
from ansible.errors import AnsibleFilterError


def path_under_chroot(input_path, chroot_path: None | str):
    """
    This filter takes one input_path and a chroot_path. If the chroot_path is
    not None, the filter composes a new merged path, with the input_path as a
    child of chroot_path. Otherwise it returns just the input_path.

    Example invocation:

        {{ input_path | lingfra.system.path_under_chroot(chroot_path | default(none)) }}
    """
    if not isinstance(input_path, str):
        raise AnsibleFilterError(
            "Input variable for this filter need to be of type str."
        )

    if chroot_path:
        if input_path[0] == "/":
            # if Path encounter a "/" in the beginning of an path it discards
            # the previous components
            input_path = input_path[1:]
        return Path(chroot_path, input_path)
    else:
        return input_path

def arch_chroot_argv(input_argv, chroot_path: None | str):
    """
    This filter takes one input_path and a chroot_path. If the chroot_path is
    not None, the filter prepends arch-chroot and the chroot_path to the
    input_argv list. For example:

        input_argv: ['mkinitcpio', '-P']
        chroot_path: '/mnt'

    will return:

        ['arch-chroot', 'mnt', 'mkinitcpio', '-P']

    This is an easy way to dynamically adjust the command for running in a
    chroot. Recommended way to call this filter:

        {{ command_argv | lingfra.arch_chroot_argv(my_chroot_path_var | default(none)) }}
    """
    if not isinstance(input_argv, list):
        raise AnsibleFilterError(
            "Input variable for this filter need to be of type str."
        )

    if chroot_path:
        result_argv = ["arch-chroot", chroot_path]
        result_argv.extend(input_argv)
        return result_argv
    else:
        return input_argv
    
# Register the filters
class FilterModule(object):
    def filters(self):
        return {
            "arch_chroot_argv": arch_chroot_argv,
            "path_under_chroot": path_under_chroot,
        }
