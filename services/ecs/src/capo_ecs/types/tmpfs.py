"""Generated from Smithy shape ``com.amazonaws.ecs#Tmpfs``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.integer
    import capo_ecs.types.string
    import capo_ecs.types.string_list


class Tmpfs(TypedDict, closed=True):
    container_path: "capo_ecs.types.string.String"
    """<p>The absolute file path where the tmpfs volume is to be mounted.</p>"""
    size: "capo_ecs.types.integer.Integer"
    """<p>The maximum size (in MiB) of the tmpfs volume.</p>"""
    mount_options: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The list of tmpfs volume mount options.</p> <p>Valid values: <code>"defaults" | "ro" | "rw" | "suid" | "nosuid" | "dev" | "nodev" | "exec" | "noexec" | "sync" | "async" | "dirsync" | "remount" | "mand" | "nomand" | "atime" | "noatime" | "diratime" | "nodiratime" | "bind" | "rbind" | "unbindable" | "runbindable" | "private" | "rprivate" | "shared" | "rshared" | "slave" | "rslave" | "relatime" | "norelatime" | "strictatime" | "nostrictatime" | "mode" | "uid" | "gid" | "nr_inodes" | "nr_blocks" | "mpol"</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tmpfs) -> dict:
    out: dict = {}
    out["containerPath"] = value["container_path"]
    out["size"] = value.get("size", 0)
    if "mount_options" in value:
        import capo_ecs.types.string_list

        out["mountOptions"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["mount_options"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Tmpfs:
    out: Tmpfs = {}  # type: ignore[typeddict-item]
    if data.get("containerPath") is not None:
        out["container_path"] = data["containerPath"]
    else:
        raise DeserializationError("Tmpfs.container_path required")
    if data.get("size") is not None:
        out["size"] = data["size"]
    else:
        out["size"] = 0
    if data.get("mountOptions") is not None:
        import capo_ecs.types.string_list

        out["mount_options"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["mountOptions"]
        )
    return out
