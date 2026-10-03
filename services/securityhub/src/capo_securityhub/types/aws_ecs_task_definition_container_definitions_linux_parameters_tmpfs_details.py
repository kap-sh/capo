"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails(
    TypedDict, closed=True
):
    container_path: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The absolute file path where the tmpfs volume is to be mounted.</p>"""
    mount_options: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The list of tmpfs volume mount options.</p> <p>Valid values: <code>"defaults"</code> | <code>"ro"</code> | <code>"rw"</code> | <code>"suid"</code> | <code>"nosuid"</code> | <code>"dev"</code> | <code>"nodev"</code> |<code> "exec"</code> | <code>"noexec"</code> | <code>"sync"</code> | <code>"async"</code> | <code>"dirsync"</code> | <code>"remount"</code> | <code>"mand"</code> | <code>"nomand"</code> | <code>"atime"</code> | <code>"noatime"</code> | <code>"diratime"</code> | <code>"nodiratime"</code> | <code>"bind"</code> | <code>"rbind"</code> | <code>"unbindable"</code> | <code>"runbindable"</code> | <code>"private"</code> | <code>"rprivate"</code> | <code>"shared"</code> | <code>"rshared"</code> | <code>"slave"</code> | <code>"rslave"</code> | <code>"relatime"</code> | <code>"norelatime"</code> | <code>"strictatime"</code> | <code>"nostrictatime"</code> |<code> "mode"</code> | <code>"uid"</code> | <code>"gid"</code> | <code>"nr_inodes"</code> |<code> "nr_blocks"</code> | <code>"mpol"</code> </p>"""
    size: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The maximum size (in MiB) of the tmpfs volume.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails,
) -> dict:
    out: dict = {}
    if "container_path" in value:
        out["ContainerPath"] = value["container_path"]
    if "mount_options" in value:
        import capo_securityhub.types.non_empty_string_list

        out["MountOptions"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["mount_options"]
            )
        )
    if "size" in value:
        out["Size"] = value["size"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails:
    out: AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails = {}  # type: ignore[typeddict-item]
    if data.get("ContainerPath") is not None:
        out["container_path"] = data["ContainerPath"]
    if data.get("MountOptions") is not None:
        import capo_securityhub.types.non_empty_string_list

        out["mount_options"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["MountOptions"]
            )
        )
    if data.get("Size") is not None:
        out["size"] = data["Size"]
    return out
