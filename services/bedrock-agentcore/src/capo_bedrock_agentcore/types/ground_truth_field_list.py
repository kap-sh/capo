"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GroundTruthFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.ground_truth_field

GroundTruthFieldList: TypeAlias = list[
    "capo_bedrock_agentcore.types.ground_truth_field.GroundTruthField"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroundTruthFieldList) -> list:
    import capo_bedrock_agentcore.types.ground_truth_field

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore.types.ground_truth_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroundTruthFieldList:
    import capo_bedrock_agentcore.types.ground_truth_field

    out: GroundTruthFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.ground_truth_field.deserialize_json(item)
        )
    return out
