"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#EventSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.event_id
    import capo_opensearchmemory.types.event_timestamp
    import capo_opensearchmemory.types.metadata_map


class EventSummary(TypedDict, closed=True):
    event_id: "capo_opensearchmemory.types.event_id.EventId"
    """<p>The event's ID.</p>"""
    metadata: NotRequired["capo_opensearchmemory.types.metadata_map.MetadataMap"]
    """<p>The event's metadata tags, as supplied to <code>CreateEvent</code>. May be empty.</p>"""
    event_timestamp: "capo_opensearchmemory.types.event_timestamp.EventTimestamp"
    """<p>The time the event occurred.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EventSummary) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    if "metadata" in value:
        import capo_opensearchmemory.types.metadata_map

        out["metadata"] = (
            capo_opensearchmemory.types.metadata_map.serialize_aws_json_1_0(
                value["metadata"]
            )
        )
    import capo_opensearchmemory.types.event_timestamp

    out["eventTimestamp"] = (
        capo_opensearchmemory.types.event_timestamp.serialize_aws_json_1_0(
            value["event_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> EventSummary:
    out: EventSummary = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        out["event_id"] = ""
    if data.get("metadata") is not None:
        import capo_opensearchmemory.types.metadata_map

        out["metadata"] = (
            capo_opensearchmemory.types.metadata_map.deserialize_aws_json_1_0(
                data["metadata"]
            )
        )
    if data.get("eventTimestamp") is not None:
        import capo_opensearchmemory.types.event_timestamp

        out["event_timestamp"] = (
            capo_opensearchmemory.types.event_timestamp.deserialize_aws_json_1_0(
                data["eventTimestamp"]
            )
        )
    else:
        import datetime

        out["event_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
