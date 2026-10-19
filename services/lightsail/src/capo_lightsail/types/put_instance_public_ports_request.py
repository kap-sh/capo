"""Generated from Smithy shape ``com.amazonaws.lightsail#PutInstancePublicPortsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.port_info_list
    import capo_lightsail.types.resource_name


class PutInstancePublicPortsRequest(TypedDict, closed=True):
    port_infos: "capo_lightsail.types.port_info_list.PortInfoList"
    """<p>An array of objects to describe the ports to open for the specified instance.</p>"""
    instance_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the instance for which to open ports.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutInstancePublicPortsRequest) -> dict:
    out: dict = {}
    import capo_lightsail.types.port_info_list

    out["portInfos"] = capo_lightsail.types.port_info_list.serialize_aws_json_1_1(
        value["port_infos"]
    )
    out["instanceName"] = value["instance_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutInstancePublicPortsRequest:
    out: PutInstancePublicPortsRequest = {}  # type: ignore[typeddict-item]
    if data.get("portInfos") is not None:
        import capo_lightsail.types.port_info_list

        out["port_infos"] = (
            capo_lightsail.types.port_info_list.deserialize_aws_json_1_1(
                data["portInfos"]
            )
        )
    else:
        out["port_infos"] = []
    if data.get("instanceName") is not None:
        out["instance_name"] = data["instanceName"]
    else:
        out["instance_name"] = ""
    return out
