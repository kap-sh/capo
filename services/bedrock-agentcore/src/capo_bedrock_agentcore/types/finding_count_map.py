"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#FindingCountMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.finding_identifier_key

FindingCountMap: TypeAlias = dict[
    "capo_bedrock_agentcore.types.finding_identifier_key.FindingIdentifierKey", "int"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FindingCountMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> FindingCountMap:
    out: FindingCountMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
