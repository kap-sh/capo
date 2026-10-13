"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#IngestPayloadList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.ingest_payload_type

IngestPayloadList: TypeAlias = list[
    "capo_bedrock_agentcore.types.ingest_payload_type.IngestPayloadType"
]


# --- restJson1 ser/de ---
def serialize_json(value: IngestPayloadList) -> list:
    import capo_bedrock_agentcore.types.ingest_payload_type

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.ingest_payload_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IngestPayloadList:
    import capo_bedrock_agentcore.types.ingest_payload_type

    out: IngestPayloadList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.ingest_payload_type.deserialize_json(item)
        )
    return out


def redact_sensitive(value: IngestPayloadList) -> list[Any]:
    import capo_bedrock_agentcore.types.ingest_payload_type

    return [
        capo_bedrock_agentcore.types.ingest_payload_type.redact_sensitive(item)
        for item in value
    ]
