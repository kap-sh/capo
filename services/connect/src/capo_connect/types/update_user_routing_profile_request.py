"""Generated from Smithy shape ``com.amazonaws.connect#UpdateUserRoutingProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.routing_profile_id
    import capo_connect.types.user_id


class UpdateUserRoutingProfileRequest(TypedDict, closed=True):
    routing_profile_id: "capo_connect.types.routing_profile_id.RoutingProfileId"
    """<p>The identifier of the routing profile for the user.</p>"""
    user_id: "capo_connect.types.user_id.UserId"
    """<p>The identifier of the user account.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserRoutingProfileRequest) -> dict:
    out: dict = {}
    out["RoutingProfileId"] = value["routing_profile_id"]
    return out


def deserialize_json(data: dict) -> UpdateUserRoutingProfileRequest:
    out: UpdateUserRoutingProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("RoutingProfileId") is not None:
        out["routing_profile_id"] = data["RoutingProfileId"]
    else:
        raise DeserializationError(
            "UpdateUserRoutingProfileRequest.routing_profile_id required"
        )
    return out
