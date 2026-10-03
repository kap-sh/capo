"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#PutRawEventsSystemMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eventbridgev2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridgev2.types.content_type
    import capo_eventbridgev2.types.event_deduplication_id
    import capo_eventbridgev2.types.event_group_id


class PutRawEventsSystemMetadata(TypedDict, closed=True):
    content_type: "capo_eventbridgev2.types.content_type.ContentType"
    """Content type of the event data (e.g., "application/cloudevents+json")."""
    deduplication_id: NotRequired[
        "capo_eventbridgev2.types.event_deduplication_id.EventDeduplicationId"
    ]
    """Deduplication ID for FIFO deduplication."""
    event_group_id: NotRequired["capo_eventbridgev2.types.event_group_id.EventGroupId"]
    """Event group ID for FIFO ordering."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutRawEventsSystemMetadata) -> dict:
    out: dict = {}
    out["ContentType"] = value["content_type"]
    if "deduplication_id" in value:
        out["DeduplicationId"] = value["deduplication_id"]
    if "event_group_id" in value:
        out["EventGroupId"] = value["event_group_id"]
    return out


def deserialize_cbor(data: dict) -> PutRawEventsSystemMetadata:
    out: PutRawEventsSystemMetadata = {}  # type: ignore[typeddict-item]
    if data.get("ContentType") is not None:
        out["content_type"] = data["ContentType"]
    else:
        raise DeserializationError("PutRawEventsSystemMetadata.content_type required")
    if data.get("DeduplicationId") is not None:
        out["deduplication_id"] = data["DeduplicationId"]
    if data.get("EventGroupId") is not None:
        out["event_group_id"] = data["EventGroupId"]
    return out
