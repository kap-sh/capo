"""Generated from Smithy shape ``com.amazonaws.connect#UpdateRoutingProfileNameRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.routing_profile_description
    import capo_connect.types.routing_profile_id
    import capo_connect.types.routing_profile_name


class UpdateRoutingProfileNameRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    routing_profile_id: "capo_connect.types.routing_profile_id.RoutingProfileId"
    """<p>The identifier of the routing profile.</p>"""
    name: NotRequired["capo_connect.types.routing_profile_name.RoutingProfileName"]
    """<p>The name of the routing profile. Must not be more than 127 characters.</p>"""
    description: NotRequired[
        "capo_connect.types.routing_profile_description.RoutingProfileDescription"
    ]
    """<p>The description of the routing profile. Must not be more than 250 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRoutingProfileNameRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateRoutingProfileNameRequest:
    out: UpdateRoutingProfileNameRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
