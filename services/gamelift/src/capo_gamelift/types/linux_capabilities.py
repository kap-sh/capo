"""Generated from Smithy shape ``com.amazonaws.gamelift#LinuxCapabilities``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.linux_capability_list


class LinuxCapabilities(TypedDict, closed=True):
    include: NotRequired[
        "capo_gamelift.types.linux_capability_list.LinuxCapabilityList"
    ]
    """<p>The list of Linux capabilities to add to the container's default configuration. Specify each capability as a string from the set of supported capability names (for example, <code>NET_BIND_SERVICE</code> or <code>SYS_PTRACE</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LinuxCapabilities) -> dict:
    out: dict = {}
    if "include" in value:
        import capo_gamelift.types.linux_capability_list

        out["Include"] = (
            capo_gamelift.types.linux_capability_list.serialize_aws_json_1_1(
                value["include"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LinuxCapabilities:
    out: LinuxCapabilities = {}  # type: ignore[typeddict-item]
    if data.get("Include") is not None:
        import capo_gamelift.types.linux_capability_list

        out["include"] = (
            capo_gamelift.types.linux_capability_list.deserialize_aws_json_1_1(
                data["Include"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LinuxCapabilities) -> dict:
    out: dict = {}
    if "include" in value:
        import capo_gamelift.types.linux_capability_list

        out["Include"] = capo_gamelift.types.linux_capability_list.serialize_cbor(
            value["include"]
        )
    return out


def deserialize_cbor(data: dict) -> LinuxCapabilities:
    out: LinuxCapabilities = {}  # type: ignore[typeddict-item]
    if data.get("Include") is not None:
        import capo_gamelift.types.linux_capability_list

        out["include"] = capo_gamelift.types.linux_capability_list.deserialize_cbor(
            data["Include"]
        )
    return out
