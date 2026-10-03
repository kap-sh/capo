"""Generated from Smithy shape ``com.amazonaws.connect#UpdateRoutingProfileDefaultOutboundQueueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.queue_id
    import capo_connect.types.routing_profile_id


class UpdateRoutingProfileDefaultOutboundQueueRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    routing_profile_id: "capo_connect.types.routing_profile_id.RoutingProfileId"
    """<p>The identifier of the routing profile.</p>"""
    default_outbound_queue_id: "capo_connect.types.queue_id.QueueId"
    """<p>The identifier for the default outbound queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRoutingProfileDefaultOutboundQueueRequest) -> dict:
    out: dict = {}
    out["DefaultOutboundQueueId"] = value["default_outbound_queue_id"]
    return out


def deserialize_json(data: dict) -> UpdateRoutingProfileDefaultOutboundQueueRequest:
    out: UpdateRoutingProfileDefaultOutboundQueueRequest = {}  # type: ignore[typeddict-item]
    if data.get("DefaultOutboundQueueId") is not None:
        out["default_outbound_queue_id"] = data["DefaultOutboundQueueId"]
    else:
        raise DeserializationError(
            "UpdateRoutingProfileDefaultOutboundQueueRequest.default_outbound_queue_id required"
        )
    return out
