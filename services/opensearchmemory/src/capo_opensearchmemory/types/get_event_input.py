"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#GetEventInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.actor_id
    import capo_opensearchmemory.types.event_id
    import capo_opensearchmemory.types.session_id
    import capo_opensearchmemory.types.space_id


class GetEventInput(TypedDict, closed=True):
    space_id: "capo_opensearchmemory.types.space_id.SpaceId"
    """<p>The ID of the space.</p>"""
    event_id: "capo_opensearchmemory.types.event_id.EventId"
    """<p>The event's ID, as returned by <code>CreateEvent</code>, <code>ListEvents</code>, or <code>SearchEvents</code>.</p>"""
    actor_id: NotRequired["capo_opensearchmemory.types.actor_id.ActorId"]
    """<p>The actor the event must belong to. Omit it to skip this check. If it doesn't match the stored event, the call fails with <code>ResourceNotFoundException</code>, as if the event did not exist.</p>"""
    session_id: NotRequired["capo_opensearchmemory.types.session_id.SessionId"]
    """<p>The session the event must belong to. Omit it to skip this check. If it doesn't match the stored event, the call fails with <code>ResourceNotFoundException</code>, as if the event did not exist.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEventInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    out["eventId"] = value["event_id"]
    if "actor_id" in value:
        out["actorId"] = value["actor_id"]
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEventInput:
    out: GetEventInput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        out["event_id"] = ""
    if data.get("actorId") is not None:
        out["actor_id"] = data["actorId"]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    return out
