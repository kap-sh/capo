"""Generated from Smithy shape ``com.amazonaws.connect#AssociateContactWithUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.agent_resource_id
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id


class AssociateContactWithUserRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    user_id: "capo_connect.types.agent_resource_id.AgentResourceId"
    """<p>The identifier for the user. This can be the ID or the ARN of the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateContactWithUserRequest) -> dict:
    out: dict = {}
    out["UserId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> AssociateContactWithUserRequest:
    out: AssociateContactWithUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("AssociateContactWithUserRequest.user_id required")
    return out
