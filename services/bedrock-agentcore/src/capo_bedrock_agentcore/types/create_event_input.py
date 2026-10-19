"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CreateEventInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.actor_id
    import capo_bedrock_agentcore.types.branch
    import capo_bedrock_agentcore.types.extraction_config
    import capo_bedrock_agentcore.types.extraction_mode
    import capo_bedrock_agentcore.types.memory_id
    import capo_bedrock_agentcore.types.metadata_map
    import capo_bedrock_agentcore.types.payload_type_list
    import capo_bedrock_agentcore.types.session_id


class CreateEventInput(TypedDict, closed=True):
    memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The identifier of the AgentCore Memory resource in which to create the event.</p>"""
    actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId"
    """<p>The identifier of the actor associated with this event. An actor represents an entity that participates in sessions and generates events.</p>"""
    session_id: NotRequired["capo_bedrock_agentcore.types.session_id.SessionId"]
    """<p>The identifier of the session in which this event occurs. A session represents a sequence of related events.</p>"""
    event_timestamp: "datetime.datetime"
    """<p>The timestamp when the event occurred. If not specified, the current time is used.</p>"""
    payload: "capo_bedrock_agentcore.types.payload_type_list.PayloadTypeList"
    """<p>The content payload of the event. This can include conversational data, JSON data, or binary content.</p>"""
    branch: NotRequired["capo_bedrock_agentcore.types.branch.Branch"]
    """<p>The branch information for this event. Branches allow for organizing events into different conversation threads or paths.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, AgentCore ignores the request, but does not return an error.</p>"""
    metadata: NotRequired["capo_bedrock_agentcore.types.metadata_map.MetadataMap"]
    """<p>The key-value metadata to attach to the event.</p>"""
    extraction_mode: NotRequired[
        "capo_bedrock_agentcore.types.extraction_mode.ExtractionMode"
    ]
    """<p>Controls long-term memory extraction for this event. When set to <code>SKIP</code>, the event is stored in short-term memory but is excluded from long-term memory extraction. If not specified, the event is processed for extraction as usual.</p>"""
    extraction_config: NotRequired[
        "capo_bedrock_agentcore.types.extraction_config.ExtractionConfig"
    ]
    """<p>The extraction configuration for long-term memory records. Use this parameter to specify namespace variable keys and their values for namespace substitution during extraction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEventInput) -> dict:
    out: dict = {}
    out["actorId"] = value["actor_id"]
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "metadata" in value:
        import capo_bedrock_agentcore.types.metadata_map

        out["metadata"] = capo_bedrock_agentcore.types.metadata_map.serialize_json(
            value["metadata"]
        )
    if "extraction_mode" in value:
        import capo_bedrock_agentcore.types.extraction_mode

        out["extractionMode"] = (
            capo_bedrock_agentcore.types.extraction_mode.serialize_json(
                value["extraction_mode"]
            )
        )
    if "extraction_config" in value:
        import capo_bedrock_agentcore.types.extraction_config

        out["extractionConfig"] = (
            capo_bedrock_agentcore.types.extraction_config.serialize_json(
                value["extraction_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateEventInput:
    out: CreateEventInput = {}  # type: ignore[typeddict-item]
    if data.get("actorId") is not None:
        out["actor_id"] = data["actorId"]
    else:
        out["actor_id"] = ""
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    if data.get("eventTimestamp") is not None:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["event_timestamp"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["eventTimestamp"]
            )
        )
    else:
        import datetime

        out["event_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("payload") is not None:
        import capo_bedrock_agentcore.types.payload_type_list

        out["payload"] = (
            capo_bedrock_agentcore.types.payload_type_list.deserialize_json(
                data["payload"]
            )
        )
    else:
        out["payload"] = []
    if data.get("branch") is not None:
        import capo_bedrock_agentcore.types.branch

        out["branch"] = capo_bedrock_agentcore.types.branch.deserialize_json(
            data["branch"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("metadata") is not None:
        import capo_bedrock_agentcore.types.metadata_map

        out["metadata"] = capo_bedrock_agentcore.types.metadata_map.deserialize_json(
            data["metadata"]
        )
    if data.get("extractionMode") is not None:
        import capo_bedrock_agentcore.types.extraction_mode

        out["extraction_mode"] = (
            capo_bedrock_agentcore.types.extraction_mode.deserialize_json(
                data["extractionMode"]
            )
        )
    if data.get("extractionConfig") is not None:
        import capo_bedrock_agentcore.types.extraction_config

        out["extraction_config"] = (
            capo_bedrock_agentcore.types.extraction_config.deserialize_json(
                data["extractionConfig"]
            )
        )
    return out


def redact_sensitive(value: CreateEventInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payload" in value:
        import capo_bedrock_agentcore.types.payload_type_list

        out["payload"] = (
            capo_bedrock_agentcore.types.payload_type_list.redact_sensitive(
                value["payload"]
            )
        )
    return out
