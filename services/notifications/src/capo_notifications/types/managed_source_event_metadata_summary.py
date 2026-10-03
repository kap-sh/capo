"""Generated from Smithy shape ``com.amazonaws.notifications#ManagedSourceEventMetadataSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_notifications.types.event_type
    import capo_notifications.types.region
    import capo_notifications.types.source


class ManagedSourceEventMetadataSummary(TypedDict, closed=True):
    event_origin_region: NotRequired["capo_notifications.types.region.Region"]
    """<p>The Region where the notification originated.</p>"""
    source: "capo_notifications.types.source.Source"
    """<p>The source service of the notification.</p> <p>Must match one of the valid EventBridge sources. Only Amazon Web Services service sourced events are supported. For example, <code>aws.ec2</code> and <code>aws.cloudwatch</code>. For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level">Event delivery from Amazon Web Services services</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    event_type: "capo_notifications.types.event_type.EventType"
    """<p>The event Type of the notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedSourceEventMetadataSummary) -> dict:
    out: dict = {}
    if "event_origin_region" in value:
        out["eventOriginRegion"] = value["event_origin_region"]
    out["source"] = value["source"]
    out["eventType"] = value["event_type"]
    return out


def deserialize_json(data: dict) -> ManagedSourceEventMetadataSummary:
    out: ManagedSourceEventMetadataSummary = {}  # type: ignore[typeddict-item]
    if data.get("eventOriginRegion") is not None:
        out["event_origin_region"] = data["eventOriginRegion"]
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        raise DeserializationError("ManagedSourceEventMetadataSummary.source required")
    if data.get("eventType") is not None:
        out["event_type"] = data["eventType"]
    else:
        raise DeserializationError(
            "ManagedSourceEventMetadataSummary.event_type required"
        )
    return out
