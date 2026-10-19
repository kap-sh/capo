"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileQueueReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.channel
    import capo_connect.types.queue_id


class RoutingProfileQueueReference(TypedDict, closed=True):
    queue_id: "capo_connect.types.queue_id.QueueId"
    """<p>The identifier for the queue.</p>"""
    channel: "capo_connect.types.channel.Channel"
    """<p>The channels agents can handle in the Contact Control Panel (CCP) for this routing profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileQueueReference) -> dict:
    out: dict = {}
    out["QueueId"] = value["queue_id"]
    import capo_connect.types.channel

    out["Channel"] = capo_connect.types.channel.serialize_json(value["channel"])
    return out


def deserialize_json(data: dict) -> RoutingProfileQueueReference:
    out: RoutingProfileQueueReference = {}  # type: ignore[typeddict-item]
    if data.get("QueueId") is not None:
        out["queue_id"] = data["QueueId"]
    else:
        out["queue_id"] = ""
    if data.get("Channel") is not None:
        import capo_connect.types.channel

        out["channel"] = capo_connect.types.channel.deserialize_json(data["Channel"])
    else:
        import typing

        out["channel"] = typing.cast("capo_connect.types.channel.Channel", "")
    return out
