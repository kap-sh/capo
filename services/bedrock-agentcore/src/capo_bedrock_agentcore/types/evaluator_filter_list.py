"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluatorFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.evaluator_filter

EvaluatorFilterList: TypeAlias = list[
    "capo_bedrock_agentcore.types.evaluator_filter.EvaluatorFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorFilterList) -> list:
    import capo_bedrock_agentcore.types.evaluator_filter

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore.types.evaluator_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> EvaluatorFilterList:
    import capo_bedrock_agentcore.types.evaluator_filter

    out: EvaluatorFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agentcore.types.evaluator_filter.deserialize_json(item))
    return out
