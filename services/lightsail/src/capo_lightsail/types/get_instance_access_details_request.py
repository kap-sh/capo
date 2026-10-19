"""Generated from Smithy shape ``com.amazonaws.lightsail#GetInstanceAccessDetailsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.instance_access_protocol
    import capo_lightsail.types.resource_name


class GetInstanceAccessDetailsRequest(TypedDict, closed=True):
    instance_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the instance to access.</p>"""
    protocol: NotRequired[
        "capo_lightsail.types.instance_access_protocol.InstanceAccessProtocol"
    ]
    """<p>The protocol to use to connect to your instance. Defaults to <code>ssh</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInstanceAccessDetailsRequest) -> dict:
    out: dict = {}
    out["instanceName"] = value["instance_name"]
    if "protocol" in value:
        import capo_lightsail.types.instance_access_protocol

        out["protocol"] = (
            capo_lightsail.types.instance_access_protocol.serialize_aws_json_1_1(
                value["protocol"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInstanceAccessDetailsRequest:
    out: GetInstanceAccessDetailsRequest = {}  # type: ignore[typeddict-item]
    if data.get("instanceName") is not None:
        out["instance_name"] = data["instanceName"]
    else:
        out["instance_name"] = ""
    if data.get("protocol") is not None:
        import capo_lightsail.types.instance_access_protocol

        out["protocol"] = (
            capo_lightsail.types.instance_access_protocol.deserialize_aws_json_1_1(
                data["protocol"]
            )
        )
    return out
