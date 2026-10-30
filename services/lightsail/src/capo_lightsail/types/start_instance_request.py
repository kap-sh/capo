"""Generated from Smithy shape ``com.amazonaws.lightsail#StartInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.instance_attribute_updates
    import capo_lightsail.types.resource_name


class StartInstanceRequest(TypedDict, closed=True):
    instance_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the instance (a virtual private server) to start.</p>"""
    attribute_updates: NotRequired[
        "capo_lightsail.types.instance_attribute_updates.InstanceAttributeUpdates"
    ]
    """<p>An object that describes the attributes to update on the instance before it starts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartInstanceRequest) -> dict:
    out: dict = {}
    out["instanceName"] = value["instance_name"]
    if "attribute_updates" in value:
        import capo_lightsail.types.instance_attribute_updates

        out["attributeUpdates"] = (
            capo_lightsail.types.instance_attribute_updates.serialize_aws_json_1_1(
                value["attribute_updates"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartInstanceRequest:
    out: StartInstanceRequest = {}  # type: ignore[typeddict-item]
    if data.get("instanceName") is not None:
        out["instance_name"] = data["instanceName"]
    else:
        out["instance_name"] = ""
    if data.get("attributeUpdates") is not None:
        import capo_lightsail.types.instance_attribute_updates

        out["attribute_updates"] = (
            capo_lightsail.types.instance_attribute_updates.deserialize_aws_json_1_1(
                data["attributeUpdates"]
            )
        )
    return out
