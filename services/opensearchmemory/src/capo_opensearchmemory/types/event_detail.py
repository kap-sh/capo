"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#EventDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.actor_id
    import capo_opensearchmemory.types.event_id
    import capo_opensearchmemory.types.event_timestamp
    import capo_opensearchmemory.types.session_id
    import capo_opensearchmemory.types.space_id


class EventDetail(TypedDict, closed=True):
    event_id: "capo_opensearchmemory.types.event_id.EventId"
    """<p>The event's ID, assigned by the service. Use it with <code>GetEvent</code> and <code>DeleteEvent</code>.</p>"""
    space_id: "capo_opensearchmemory.types.space_id.SpaceId"
    """<p>The ID of the space.</p>"""
    actor_id: "capo_opensearchmemory.types.actor_id.ActorId"
    """<p>The ID of the actor the event belongs to.</p>"""
    session_id: "capo_opensearchmemory.types.session_id.SessionId"
    """<p>The ID of the session the event belongs to, including one the service generated.</p>"""
    event_timestamp: "capo_opensearchmemory.types.event_timestamp.EventTimestamp"
    """<p>When the event occurred: the value supplied, or the time the request was received.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EventDetail) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    out["spaceId"] = value["space_id"]
    out["actorId"] = value["actor_id"]
    out["sessionId"] = value["session_id"]
    import capo_opensearchmemory.types.event_timestamp

    out["eventTimestamp"] = (
        capo_opensearchmemory.types.event_timestamp.serialize_aws_json_1_0(
            value["event_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> EventDetail:
    out: EventDetail = {}  # type: ignore[typeddict-item]
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
