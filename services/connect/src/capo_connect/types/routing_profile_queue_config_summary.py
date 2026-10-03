"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileQueueConfigSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.channel
    import capo_connect.types.delay
    import capo_connect.types.priority
    import capo_connect.types.queue_id
    import capo_connect.types.queue_name


class RoutingProfileQueueConfigSummary(TypedDict, closed=True):
    queue_id: "capo_connect.types.queue_id.QueueId"
    """<p>The identifier for the queue.</p>"""
    queue_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the queue.</p>"""
    queue_name: "capo_connect.types.queue_name.QueueName"
    """<p>The name of the queue.</p>"""
    priority: "capo_connect.types.priority.Priority"
    """<p>The order in which contacts are to be handled for the queue. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing-profiles-priority.html">Queues: priority and delay</a>.</p>"""
    delay: "capo_connect.types.delay.Delay"
    """<p>The delay, in seconds, that a contact should be in the queue before they are routed to an available agent. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing-profiles-priority.html">Queues: priority and delay</a> in the <i>Connect Customer Administrator Guide</i>.</p>"""
    channel: "capo_connect.types.channel.Channel"
    """<p>The channels this queue supports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileQueueConfigSummary) -> dict:
    out: dict = {}
    out["QueueId"] = value["queue_id"]
    out["QueueArn"] = value["queue_arn"]
    out["QueueName"] = value["queue_name"]
    out["Priority"] = value["priority"]
    out["Delay"] = value.get("delay", 0)
    import capo_connect.types.channel

    out["Channel"] = capo_connect.types.channel.serialize_json(value["channel"])
    return out


def deserialize_json(data: dict) -> RoutingProfileQueueConfigSummary:
    out: RoutingProfileQueueConfigSummary = {}  # type: ignore[typeddict-item]
    if data.get("QueueId") is not None:
        out["queue_id"] = data["QueueId"]
    else:
        raise DeserializationError("RoutingProfileQueueConfigSummary.queue_id required")
    if data.get("QueueArn") is not None:
        out["queue_arn"] = data["QueueArn"]
    else:
        raise DeserializationError(
            "RoutingProfileQueueConfigSummary.queue_arn required"
        )
    if data.get("QueueName") is not None:
        out["queue_name"] = data["QueueName"]
    else:
        raise DeserializationError(
            "RoutingProfileQueueConfigSummary.queue_name required"
        )
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    else:
        raise DeserializationError("RoutingProfileQueueConfigSummary.priority required")
    if data.get("Delay") is not None:
        out["delay"] = data["Delay"]
    else:
        out["delay"] = 0
    if data.get("Channel") is not None:
        import capo_connect.types.channel

        out["channel"] = capo_connect.types.channel.deserialize_json(data["Channel"])
    else:
        raise DeserializationError("RoutingProfileQueueConfigSummary.channel required")
    return out
