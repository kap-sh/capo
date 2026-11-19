"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CustomDataIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.custom_data_identifier

CustomDataIdentifierList: TypeAlias = list[
    "capo_bedrock_agentcore.types.custom_data_identifier.CustomDataIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomDataIdentifierList) -> list:
    import capo_bedrock_agentcore.types.custom_data_identifier

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.custom_data_identifier.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CustomDataIdentifierList:
    import capo_bedrock_agentcore.types.custom_data_identifier

    out: CustomDataIdentifierList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.custom_data_identifier.deserialize_json(item)
        )
    return out
