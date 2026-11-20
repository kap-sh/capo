"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#BatchGetEventInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.actor_id
    import capo_opensearchmemory.types.batch_get_event_id_list
    import capo_opensearchmemory.types.session_id
    import capo_opensearchmemory.types.space_id


class BatchGetEventInput(TypedDict, closed=True):
    space_id: "capo_opensearchmemory.types.space_id.SpaceId"
    """<p>The ID of the space.</p>"""
    actor_id: NotRequired["capo_opensearchmemory.types.actor_id.ActorId"]
    """<p>The actor that every requested event must belong to. Omit it to skip this check. The operation reports an event that doesn't match in <code>errors</code> as <code>RESOURCE_NOT_FOUND</code>.</p>"""
    session_id: NotRequired["capo_opensearchmemory.types.session_id.SessionId"]
    """<p>The session that every requested event must belong to. Omit it to skip this check. The operation reports an event that doesn't match in <code>errors</code> as <code>RESOURCE_NOT_FOUND</code>.</p>"""
    event_ids: "capo_opensearchmemory.types.batch_get_event_id_list.BatchGetEventIdList"
    """<p>The IDs of the events to get: 1 to 10, without duplicates.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetEventInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    if "actor_id" in value:
        out["actorId"] = value["actor_id"]
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    import capo_opensearchmemory.types.batch_get_event_id_list

    out["eventIds"] = (
        capo_opensearchmemory.types.batch_get_event_id_list.serialize_aws_json_1_0(
            value["event_ids"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetEventInput:
    out: BatchGetEventInput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("actorId") is not None:
        out["actor_id"] = data["actorId"]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    if data.get("eventIds") is not None:
        import capo_opensearchmemory.types.batch_get_event_id_list

        out["event_ids"] = (
            capo_opensearchmemory.types.batch_get_event_id_list.deserialize_aws_json_1_0(
                data["eventIds"]
            )
        )
    else:
        out["event_ids"] = []
    return out
