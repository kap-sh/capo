"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RedactionIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.redaction_identifier

RedactionIdentifierList: TypeAlias = list[
    "capo_bedrock_agentcore.types.redaction_identifier.RedactionIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: RedactionIdentifierList) -> list:
    import capo_bedrock_agentcore.types.redaction_identifier

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.redaction_identifier.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RedactionIdentifierList:
    import capo_bedrock_agentcore.types.redaction_identifier

    out: RedactionIdentifierList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.redaction_identifier.deserialize_json(item)
        )
    return out
