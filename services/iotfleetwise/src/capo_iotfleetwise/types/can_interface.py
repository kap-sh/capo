"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CanInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.can_interface_name
    import capo_iotfleetwise.types.protocol_name
    import capo_iotfleetwise.types.protocol_version


class CanInterface(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.can_interface_name.CanInterfaceName"
    """<p>The unique name of the interface.</p>"""
    protocol_name: NotRequired["capo_iotfleetwise.types.protocol_name.ProtocolName"]
    """<p>The name of the communication protocol for the interface.</p>"""
    protocol_version: NotRequired[
        "capo_iotfleetwise.types.protocol_version.ProtocolVersion"
    ]
    """<p>The version of the communication protocol for the interface.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CanInterface) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "protocol_name" in value:
        out["protocolName"] = value["protocol_name"]
    if "protocol_version" in value:
        out["protocolVersion"] = value["protocol_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CanInterface:
    out: CanInterface = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("protocolName") is not None:
        out["protocol_name"] = data["protocolName"]
    if data.get("protocolVersion") is not None:
        out["protocol_version"] = data["protocolVersion"]
    return out
