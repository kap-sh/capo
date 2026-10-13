"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InlineMemoryContent``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.ingest_payload_list


class InlineMemoryContent(TypedDict, closed=True):
    payload: "capo_bedrock_agentcore.types.ingest_payload_list.IngestPayloadList"
    """<p>The list of content payload items to ingest.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InlineMemoryContent) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.ingest_payload_list

    out["payload"] = capo_bedrock_agentcore.types.ingest_payload_list.serialize_json(
        value["payload"]
    )
    return out


def deserialize_json(data: dict) -> InlineMemoryContent:
    out: InlineMemoryContent = {}  # type: ignore[typeddict-item]
    if data.get("payload") is not None:
        import capo_bedrock_agentcore.types.ingest_payload_list

        out["payload"] = (
            capo_bedrock_agentcore.types.ingest_payload_list.deserialize_json(
                data["payload"]
            )
        )
    else:
        raise DeserializationError("InlineMemoryContent.payload required")
    return out


def redact_sensitive(value: InlineMemoryContent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payload" in value:
        import capo_bedrock_agentcore.types.ingest_payload_list

        out["payload"] = (
            capo_bedrock_agentcore.types.ingest_payload_list.redact_sensitive(
                value["payload"]
            )
        )
    return out
