"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileQueueConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.delay
    import capo_connect.types.priority
    import capo_connect.types.routing_profile_queue_reference


class RoutingProfileQueueConfig(TypedDict, closed=True):
    queue_reference: "capo_connect.types.routing_profile_queue_reference.RoutingProfileQueueReference"
    """<p>Contains information about a queue resource.</p>"""
    priority: "capo_connect.types.priority.Priority"
    """<p>The order in which contacts are to be handled for the queue. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing-profiles-priority.html">Queues: priority and delay</a>.</p>"""
    delay: "capo_connect.types.delay.Delay"
    """<p>The delay, in seconds, a contact should be in the queue before they are routed to an available agent. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing-profiles-priority.html">Queues: priority and delay</a> in the <i>Connect Customer Administrator Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileQueueConfig) -> dict:
    out: dict = {}
    import capo_connect.types.routing_profile_queue_reference

    out["QueueReference"] = (
        capo_connect.types.routing_profile_queue_reference.serialize_json(
            value["queue_reference"]
        )
    )
    out["Priority"] = value["priority"]
    out["Delay"] = value["delay"]
    return out


def deserialize_json(data: dict) -> RoutingProfileQueueConfig:
    out: RoutingProfileQueueConfig = {}  # type: ignore[typeddict-item]
    if data.get("QueueReference") is not None:
        import capo_connect.types.routing_profile_queue_reference

        out["queue_reference"] = (
            capo_connect.types.routing_profile_queue_reference.deserialize_json(
                data["QueueReference"]
            )
        )
    else:
        raise DeserializationError("RoutingProfileQueueConfig.queue_reference required")
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    else:
        raise DeserializationError("RoutingProfileQueueConfig.priority required")
    if data.get("Delay") is not None:
        out["delay"] = data["Delay"]
    else:
        raise DeserializationError("RoutingProfileQueueConfig.delay required")
    return out
