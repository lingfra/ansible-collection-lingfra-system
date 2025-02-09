from pathlib import Path
from ansible.errors import AnsibleFilterError


def get_chrooted_path(
    input_path: None | str, chroot_path: None | str = None
) -> None | str:

    result: None | Path = None

    if not input_path:
        # no input path (e. g. an empty string or None)
        return result
    else:
        # input_path provided
        if chroot_path:
            if len(input_path) == 1 and input_path == "/":
                # input_path is root path
                result = Path(chroot_path)
            elif len(input_path) > 1 and input_path[0] == "/":
                # input path is an absolute path.

                # if Path encounter a "/" in the beginning of an path it
                # discards the previous components, therefore the first string
                # index is ommited.
                result = Path(chroot_path, input_path[1:])
            else:
                raise AnsibleFilterError(
                    "An unexpected error occured."
                    f"Input variables are input_path={input_path}, chroot_path={chroot_path}."
                )
        else:
            # no chroot_path provided, return input_path
            result = Path(input_path)

    return result.__str__()


def chrooted_path(input_path, chroot_path):
    """
    This filter takes one input_path and a chroot_path. If the chroot_path is
    not None, the filter composes a new merged path, with the input_path as a
    child of chroot_path. Otherwise it returns just the input_path.

    Example invocation:

        {{ input_path | lingfra.system.chrooted_path(chroot_path | default(none)) }}
    """
    if not isinstance(input_path, str):
        raise AnsibleFilterError("Input variable for this filter need to be a string.")
    if not isinstance(chroot_path, str) and chroot_path is not None:
        raise AnsibleFilterError("chroot_path need to be a string or None.")

    return get_chrooted_path(input_path, chroot_path)


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
            "chrooted_path": chrooted_path,
        }
