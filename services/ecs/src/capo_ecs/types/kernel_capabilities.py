"""Generated from Smithy shape ``com.amazonaws.ecs#KernelCapabilities``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string_list


class KernelCapabilities(TypedDict, closed=True):
    add: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The Linux capabilities for the container that have been added to the default configuration provided by Docker. This parameter maps to <code>CapAdd</code> in the docker container create command and the <code>--cap-add</code> option to docker run.</p> <note> <p>Tasks launched on Fargate only support adding the <code>SYS_PTRACE</code> kernel capability.</p> </note> <p>Valid values: <code>"ALL" | "AUDIT_CONTROL" | "AUDIT_WRITE" | "BLOCK_SUSPEND" | "CHOWN" | "DAC_OVERRIDE" | "DAC_READ_SEARCH" | "FOWNER" | "FSETID" | "IPC_LOCK" | "IPC_OWNER" | "KILL" | "LEASE" | "LINUX_IMMUTABLE" | "MAC_ADMIN" | "MAC_OVERRIDE" | "MKNOD" | "NET_ADMIN" | "NET_BIND_SERVICE" | "NET_BROADCAST" | "NET_RAW" | "SETFCAP" | "SETGID" | "SETPCAP" | "SETUID" | "SYS_ADMIN" | "SYS_BOOT" | "SYS_CHROOT" | "SYS_MODULE" | "SYS_NICE" | "SYS_PACCT" | "SYS_PTRACE" | "SYS_RAWIO" | "SYS_RESOURCE" | "SYS_TIME" | "SYS_TTY_CONFIG" | "SYSLOG" | "WAKE_ALARM"</code> </p>"""
    drop: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The Linux capabilities for the container that have been removed from the default configuration provided by Docker. This parameter maps to <code>CapDrop</code> in the docker container create command and the <code>--cap-drop</code> option to docker run.</p> <p>Valid values: <code>"ALL" | "AUDIT_CONTROL" | "AUDIT_WRITE" | "BLOCK_SUSPEND" | "CHOWN" | "DAC_OVERRIDE" | "DAC_READ_SEARCH" | "FOWNER" | "FSETID" | "IPC_LOCK" | "IPC_OWNER" | "KILL" | "LEASE" | "LINUX_IMMUTABLE" | "MAC_ADMIN" | "MAC_OVERRIDE" | "MKNOD" | "NET_ADMIN" | "NET_BIND_SERVICE" | "NET_BROADCAST" | "NET_RAW" | "SETFCAP" | "SETGID" | "SETPCAP" | "SETUID" | "SYS_ADMIN" | "SYS_BOOT" | "SYS_CHROOT" | "SYS_MODULE" | "SYS_NICE" | "SYS_PACCT" | "SYS_PTRACE" | "SYS_RAWIO" | "SYS_RESOURCE" | "SYS_TIME" | "SYS_TTY_CONFIG" | "SYSLOG" | "WAKE_ALARM"</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KernelCapabilities) -> dict:
    out: dict = {}
    if "add" in value:
        import capo_ecs.types.string_list

        out["add"] = capo_ecs.types.string_list.serialize_aws_json_1_1(value["add"])
    if "drop" in value:
        import capo_ecs.types.string_list

        out["drop"] = capo_ecs.types.string_list.serialize_aws_json_1_1(value["drop"])
    return out


def deserialize_aws_json_1_1(data: dict) -> KernelCapabilities:
    out: KernelCapabilities = {}  # type: ignore[typeddict-item]
    if data.get("add") is not None:
        import capo_ecs.types.string_list

        out["add"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(data["add"])
    if data.get("drop") is not None:
        import capo_ecs.types.string_list

        out["drop"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(data["drop"])
    return out
