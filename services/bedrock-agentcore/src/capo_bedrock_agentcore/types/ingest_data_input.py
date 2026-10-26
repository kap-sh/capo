"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#IngestDataInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.actor_id
    import capo_bedrock_agentcore.types.content_source
    import capo_bedrock_agentcore.types.extraction_config
    import capo_bedrock_agentcore.types.memory_id
    import capo_bedrock_agentcore.types.metadata_map
    import capo_bedrock_agentcore.types.session_id


class IngestDataInput(TypedDict, closed=True):
    memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The identifier of the AgentCore Memory resource to ingest content into.</p>"""
    source: "capo_bedrock_agentcore.types.content_source.ContentSource"
    """<p>The content to ingest. Only inline content is supported.</p>"""
    content_timestamp: "datetime.datetime"
    """<p>The timestamp of when the content occurred.</p>"""
    actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId"
    """<p>The identifier of the actor associated with this content. An actor represents an entity that participates in sessions and generates content.</p>"""
    session_id: NotRequired["capo_bedrock_agentcore.types.session_id.SessionId"]
    """<p>The identifier of the session that the content belongs to. If not provided, a session identifier is generated and returned in the response.</p>"""
    extraction_config: NotRequired[
        "capo_bedrock_agentcore.types.extraction_config.ExtractionConfig"
    ]
    """<p>The extraction configuration for long-term memory records. Use this parameter to specify namespace variable keys and their values for namespace substitution during extraction.</p>"""
    metadata: NotRequired["capo_bedrock_agentcore.types.metadata_map.MetadataMap"]
    """<p>The key-value metadata to attach to the content.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, AgentCore ignores the request, but does not return an error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestDataInput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.content_source

    out["source"] = capo_bedrock_agentcore.types.content_source.serialize_json(
        value["source"]
    )
    import capo_bedrock_agentcore.types._prelude.timestamp

    out["contentTimestamp"] = (
        capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
            value["content_timestamp"]
        )
    )
    out["actorId"] = value["actor_id"]
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "extraction_config" in value:
        import capo_bedrock_agentcore.types.extraction_config

        out["extractionConfig"] = (
            capo_bedrock_agentcore.types.extraction_config.serialize_json(
                value["extraction_config"]
            )
        )
    if "metadata" in value:
        import capo_bedrock_agentcore.types.metadata_map

        out["metadata"] = capo_bedrock_agentcore.types.metadata_map.serialize_json(
            value["metadata"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> IngestDataInput:
    out: IngestDataInput = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        import capo_bedrock_agentcore.types.content_source

        out["source"] = capo_bedrock_agentcore.types.content_source.deserialize_json(
            data["source"]
        )
    else:
        out["source"] = {"$unknown": {"name": ""}}
    if data.get("contentTimestamp") is not None:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["content_timestamp"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["contentTimestamp"]
            )
        )
    else:
        import datetime

        out["content_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("actorId") is not None:
        out["actor_id"] = data["actorId"]
    else:
        out["actor_id"] = ""
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    if data.get("extractionConfig") is not None:
        import capo_bedrock_agentcore.types.extraction_config

        out["extraction_config"] = (
            capo_bedrock_agentcore.types.extraction_config.deserialize_json(
                data["extractionConfig"]
            )
        )
    if data.get("metadata") is not None:
        import capo_bedrock_agentcore.types.metadata_map

        out["metadata"] = capo_bedrock_agentcore.types.metadata_map.deserialize_json(
            data["metadata"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: IngestDataInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source" in value:
        import capo_bedrock_agentcore.types.content_source

        out["source"] = capo_bedrock_agentcore.types.content_source.redact_sensitive(
            value["source"]
        )
    return out
