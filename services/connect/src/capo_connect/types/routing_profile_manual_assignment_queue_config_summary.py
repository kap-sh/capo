"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileManualAssignmentQueueConfigSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.channel
    import capo_connect.types.queue_id
    import capo_connect.types.queue_name


class RoutingProfileManualAssignmentQueueConfigSummary(TypedDict, closed=True):
    queue_id: "capo_connect.types.queue_id.QueueId"
    """<p>The identifier for the queue.</p>"""
    queue_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the queue.</p>"""
    queue_name: "capo_connect.types.queue_name.QueueName"
    """<p>The name of the queue.</p>"""
    channel: "capo_connect.types.channel.Channel"
    """<p>The channels this queue supports. Valid Values: CHAT | TASK | EMAIL </p> <important> <p>VOICE is not supported. The information shown below is incorrect. We're working to correct it. </p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileManualAssignmentQueueConfigSummary) -> dict:
    out: dict = {}
    out["QueueId"] = value["queue_id"]
    out["QueueArn"] = value["queue_arn"]
    out["QueueName"] = value["queue_name"]
    import capo_connect.types.channel

    out["Channel"] = capo_connect.types.channel.serialize_json(value["channel"])
    return out


def deserialize_json(data: dict) -> RoutingProfileManualAssignmentQueueConfigSummary:
    out: RoutingProfileManualAssignmentQueueConfigSummary = {}  # type: ignore[typeddict-item]
    if data.get("QueueId") is not None:
        out["queue_id"] = data["QueueId"]
    else:
        out["queue_id"] = ""
    if data.get("QueueArn") is not None:
        out["queue_arn"] = data["QueueArn"]
    else:
        out["queue_arn"] = ""
    if data.get("QueueName") is not None:
        out["queue_name"] = data["QueueName"]
    else:
        out["queue_name"] = ""
    if data.get("Channel") is not None:
        import capo_connect.types.channel

        out["channel"] = capo_connect.types.channel.deserialize_json(data["Channel"])
    else:
        import typing

        out["channel"] = typing.cast("capo_connect.types.channel.Channel", "")
    return out
