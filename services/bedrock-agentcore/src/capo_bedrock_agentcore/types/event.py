"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Event``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.actor_id
    import capo_bedrock_agentcore.types.branch
    import capo_bedrock_agentcore.types.event_id
    import capo_bedrock_agentcore.types.memory_id
    import capo_bedrock_agentcore.types.metadata_map
    import capo_bedrock_agentcore.types.payload_type_list
    import capo_bedrock_agentcore.types.session_id


class Event(TypedDict, closed=True):
    memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The identifier of the AgentCore Memory resource containing the event.</p>"""
    actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId"
    """<p>The identifier of the actor associated with the event.</p>"""
    session_id: "capo_bedrock_agentcore.types.session_id.SessionId"
    """<p>The identifier of the session containing the event.</p>"""
    event_id: "capo_bedrock_agentcore.types.event_id.EventId"
    """<p>The unique identifier of the event.</p>"""
    event_timestamp: "datetime.datetime"
    """<p>The timestamp when the event occurred.</p>"""
    payload: "capo_bedrock_agentcore.types.payload_type_list.PayloadTypeList"
    """<p>The content payload of the event.</p>"""
    branch: NotRequired["capo_bedrock_agentcore.types.branch.Branch"]
    """<p>The branch information for the event.</p>"""
    metadata: NotRequired["capo_bedrock_agentcore.types.metadata_map.MetadataMap"]
    """<p>Metadata associated with an event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Event) -> dict:
    out: dict = {}
    out["memoryId"] = value["memory_id"]
    out["actorId"] = value["actor_id"]
    out["sessionId"] = value["session_id"]
    out["eventId"] = value["event_id"]
    import capo_bedrock_agentcore.types._prelude.timestamp

    out["eventTimestamp"] = (
        capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
            value["event_timestamp"]
        )
    )
    import capo_bedrock_agentcore.types.payload_type_list

    out["payload"] = capo_bedrock_agentcore.types.payload_type_list.serialize_json(
        value["payload"]
    )
    if "branch" in value:
        import capo_bedrock_agentcore.types.branch

        out["branch"] = capo_bedrock_agentcore.types.branch.serialize_json(
            value["branch"]
        )
    if "metadata" in value:
        import capo_bedrock_agentcore.types.metadata_map

        out["metadata"] = capo_bedrock_agentcore.types.metadata_map.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> Event:
    out: Event = {}  # type: ignore[typeddict-item]
    if data.get("memoryId") is not None:
        out["memory_id"] = data["memoryId"]
    else:
        raise DeserializationError("Event.memory_id required")
    if data.get("actorId") is not None:
        out["actor_id"] = data["actorId"]
    else:
        raise DeserializationError("Event.actor_id required")
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("Event.session_id required")
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        raise DeserializationError("Event.event_id required")
    if data.get("eventTimestamp") is not None:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["event_timestamp"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["eventTimestamp"]
            )
        )
    else:
        raise DeserializationError("Event.event_timestamp required")
    if data.get("payload") is not None:
        import capo_bedrock_agentcore.types.payload_type_list

        out["payload"] = (
            capo_bedrock_agentcore.types.payload_type_list.deserialize_json(
                data["payload"]
            )
        )
    else:
        raise DeserializationError("Event.payload required")
    if data.get("branch") is not None:
        import capo_bedrock_agentcore.types.branch

        out["branch"] = capo_bedrock_agentcore.types.branch.deserialize_json(
            data["branch"]
        )
    if data.get("metadata") is not None:
        import capo_bedrock_agentcore.types.metadata_map

        out["metadata"] = capo_bedrock_agentcore.types.metadata_map.deserialize_json(
            data["metadata"]
        )
    return out


def redact_sensitive(value: Event) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payload" in value:
        import capo_bedrock_agentcore.types.payload_type_list

        out["payload"] = (
            capo_bedrock_agentcore.types.payload_type_list.redact_sensitive(
                value["payload"]
            )
        )
    return out
