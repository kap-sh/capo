"""Generated from Smithy shape ``com.amazonaws.lightsail#CloseInstancePublicPortsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.port_info
    import capo_lightsail.types.resource_name


class CloseInstancePublicPortsRequest(TypedDict, closed=True):
    port_info: "capo_lightsail.types.port_info.PortInfo"
    """<p>An object to describe the ports to close for the specified instance.</p>"""
    instance_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the instance for which to close ports.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloseInstancePublicPortsRequest) -> dict:
    out: dict = {}
    import capo_lightsail.types.port_info

    out["portInfo"] = capo_lightsail.types.port_info.serialize_aws_json_1_1(
        value["port_info"]
    )
    out["instanceName"] = value["instance_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloseInstancePublicPortsRequest:
    out: CloseInstancePublicPortsRequest = {}  # type: ignore[typeddict-item]
    if data.get("portInfo") is not None:
        import capo_lightsail.types.port_info

        out["port_info"] = capo_lightsail.types.port_info.deserialize_aws_json_1_1(
            data["portInfo"]
        )
    else:
        raise DeserializationError("CloseInstancePublicPortsRequest.port_info required")
    if data.get("instanceName") is not None:
        out["instance_name"] = data["instanceName"]
    else:
        out["instance_name"] = ""
    return out
