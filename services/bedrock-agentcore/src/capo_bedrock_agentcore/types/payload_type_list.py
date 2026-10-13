"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PayloadTypeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.payload_type

PayloadTypeList: TypeAlias = list[
    "capo_bedrock_agentcore.types.payload_type.PayloadType"
]


# --- restJson1 ser/de ---
def serialize_json(value: PayloadTypeList) -> list:
    import capo_bedrock_agentcore.types.payload_type

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore.types.payload_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> PayloadTypeList:
    import capo_bedrock_agentcore.types.payload_type

    out: PayloadTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agentcore.types.payload_type.deserialize_json(item))
    return out


def redact_sensitive(value: PayloadTypeList) -> list[Any]:
    import capo_bedrock_agentcore.types.payload_type

    return [
        capo_bedrock_agentcore.types.payload_type.redact_sensitive(item)
        for item in value
    ]
