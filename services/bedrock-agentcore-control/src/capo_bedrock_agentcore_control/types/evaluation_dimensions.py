"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EvaluationDimensions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.evaluation_dimension

EvaluationDimensions: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.evaluation_dimension.EvaluationDimension"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationDimensions) -> list:
    import capo_bedrock_agentcore_control.types.evaluation_dimension

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.evaluation_dimension.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EvaluationDimensions:
    import capo_bedrock_agentcore_control.types.evaluation_dimension

    out: EvaluationDimensions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.evaluation_dimension.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: EvaluationDimensions) -> list[Any]:
    import capo_bedrock_agentcore_control.types.evaluation_dimension

    return [
        capo_bedrock_agentcore_control.types.evaluation_dimension.redact_sensitive(item)
        for item in value
    ]
