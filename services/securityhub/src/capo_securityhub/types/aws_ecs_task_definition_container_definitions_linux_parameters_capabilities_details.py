"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string_list


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails(
    TypedDict, closed=True
):
    add: NotRequired["capo_securityhub.types.non_empty_string_list.NonEmptyStringList"]
    """<p>The Linux capabilities for the container that are added to the default configuration provided by Docker. Valid values are as follows:</p> <p>Valid values: <code>"ALL"</code> | <code>"AUDIT_CONTROL"</code> |<code> "AUDIT_WRITE"</code> | <code>"BLOCK_SUSPEND"</code> | <code>"CHOWN"</code> | <code>"DAC_OVERRIDE"</code> | <code>"DAC_READ_SEARCH"</code> | <code>"FOWNER"</code> | <code>"FSETID"</code> | <code>"IPC_LOCK"</code> | <code>"IPC_OWNER"</code> | <code>"KILL"</code> | <code>"LEASE"</code> | <code>"LINUX_IMMUTABLE"</code> | <code>"MAC_ADMIN"</code> |<code> "MAC_OVERRIDE"</code> | <code>"MKNOD"</code> | <code>"NET_ADMIN"</code> | <code>"NET_BIND_SERVICE"</code> | <code>"NET_BROADCAST"</code> | <code>"NET_RAW"</code> | <code>"SETFCAP"</code> | <code>"SETGID"</code> | <code>"SETPCAP"</code> | <code>"SETUID"</code> | <code>"SYS_ADMIN"</code> | <code>"SYS_BOOT"</code> | <code>"SYS_CHROOT"</code> | <code>"SYS_MODULE"</code> | <code>"SYS_NICE"</code> | <code>"SYS_PACCT"</code> | <code>"SYS_PTRACE"</code> | <code>"SYS_RAWIO"</code> | <code>"SYS_RESOURCE"</code> | <code>"SYS_TIME"</code> | <code>"SYS_TTY_CONFIG"</code> | <code>"SYSLOG"</code> | <code>"WAKE_ALARM"</code> </p>"""
    drop: NotRequired["capo_securityhub.types.non_empty_string_list.NonEmptyStringList"]
    """<p>The Linux capabilities for the container that are dropped from the default configuration provided by Docker.</p> <p>Valid values: <code>"ALL"</code> | <code>"AUDIT_CONTROL"</code> |<code> "AUDIT_WRITE"</code> | <code>"BLOCK_SUSPEND"</code> | <code>"CHOWN"</code> | <code>"DAC_OVERRIDE"</code> | <code>"DAC_READ_SEARCH"</code> | <code>"FOWNER"</code> | <code>"FSETID"</code> | <code>"IPC_LOCK"</code> | <code>"IPC_OWNER"</code> | <code>"KILL"</code> | <code>"LEASE"</code> | <code>"LINUX_IMMUTABLE"</code> | <code>"MAC_ADMIN"</code> |<code> "MAC_OVERRIDE"</code> | <code>"MKNOD"</code> | <code>"NET_ADMIN"</code> | <code>"NET_BIND_SERVICE"</code> | <code>"NET_BROADCAST"</code> | <code>"NET_RAW"</code> | <code>"SETFCAP"</code> | <code>"SETGID"</code> | <code>"SETPCAP"</code> | <code>"SETUID"</code> | <code>"SYS_ADMIN"</code> | <code>"SYS_BOOT"</code> | <code>"SYS_CHROOT"</code> | <code>"SYS_MODULE"</code> | <code>"SYS_NICE"</code> | <code>"SYS_PACCT"</code> | <code>"SYS_PTRACE"</code> | <code>"SYS_RAWIO"</code> | <code>"SYS_RESOURCE"</code> | <code>"SYS_TIME"</code> | <code>"SYS_TTY_CONFIG"</code> | <code>"SYSLOG"</code> | <code>"WAKE_ALARM"</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails,
) -> dict:
    out: dict = {}
    if "add" in value:
        import capo_securityhub.types.non_empty_string_list

        out["Add"] = capo_securityhub.types.non_empty_string_list.serialize_json(
            value["add"]
        )
    if "drop" in value:
        import capo_securityhub.types.non_empty_string_list

        out["Drop"] = capo_securityhub.types.non_empty_string_list.serialize_json(
            value["drop"]
        )
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails:
    out: AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails = {}  # type: ignore[typeddict-item]
    if data.get("Add") is not None:
        import capo_securityhub.types.non_empty_string_list

        out["add"] = capo_securityhub.types.non_empty_string_list.deserialize_json(
            data["Add"]
        )
    if data.get("Drop") is not None:
        import capo_securityhub.types.non_empty_string_list

        out["drop"] = capo_securityhub.types.non_empty_string_list.deserialize_json(
            data["Drop"]
        )
    return out
