"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#Event``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.actor_id
    import capo_opensearchmemory.types.event_id
    import capo_opensearchmemory.types.event_payload
    import capo_opensearchmemory.types.event_timestamp
    import capo_opensearchmemory.types.metadata_map
    import capo_opensearchmemory.types.session_id
    import capo_opensearchmemory.types.space_id


class Event(TypedDict, closed=True):
    event_id: "capo_opensearchmemory.types.event_id.EventId"
    """<p>The event's ID.</p>"""
    space_id: "capo_opensearchmemory.types.space_id.SpaceId"
    """<p>The ID of the space.</p>"""
    actor_id: "capo_opensearchmemory.types.actor_id.ActorId"
    """<p>The ID of the actor the event belongs to.</p>"""
    session_id: "capo_opensearchmemory.types.session_id.SessionId"
    """<p>The ID of the session the event belongs to.</p>"""
    payload: "capo_opensearchmemory.types.event_payload.EventPayload"
    """<p>The event's content, as submitted to <code>CreateEvent</code>.</p>"""
    metadata: NotRequired["capo_opensearchmemory.types.metadata_map.MetadataMap"]
    """<p>The event's metadata tags, as supplied to <code>CreateEvent</code>. May be empty.</p>"""
    event_timestamp: "capo_opensearchmemory.types.event_timestamp.EventTimestamp"
    """<p>The time the event occurred.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Event) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    out["spaceId"] = value["space_id"]
    out["actorId"] = value["actor_id"]
    out["sessionId"] = value["session_id"]
    import capo_opensearchmemory.types.event_payload

    out["payload"] = capo_opensearchmemory.types.event_payload.serialize_aws_json_1_0(
        value["payload"]
    )
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


def deserialize_aws_json_1_0(data: dict) -> Event:
    out: Event = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        out["event_id"] = ""
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("actorId") is not None:
        out["actor_id"] = data["actorId"]
    else:
        out["actor_id"] = ""
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("payload") is not None:
        import capo_opensearchmemory.types.event_payload

        out["payload"] = (
            capo_opensearchmemory.types.event_payload.deserialize_aws_json_1_0(
                data["payload"]
            )
        )
    else:
        out["payload"] = {"$unknown": {"name": ""}}
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


def redact_sensitive(value: Event) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payload" in value:
        import capo_opensearchmemory.types.event_payload

        out["payload"] = capo_opensearchmemory.types.event_payload.redact_sensitive(
            value["payload"]
        )
    return out
