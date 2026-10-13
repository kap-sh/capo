"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluationResults``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.evaluation_result_content

EvaluationResults: TypeAlias = list[
    "capo_bedrock_agentcore.types.evaluation_result_content.EvaluationResultContent"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationResults) -> list:
    import capo_bedrock_agentcore.types.evaluation_result_content

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.evaluation_result_content.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EvaluationResults:
    import capo_bedrock_agentcore.types.evaluation_result_content

    out: EvaluationResults = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.evaluation_result_content.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: EvaluationResults) -> list[Any]:
    import capo_bedrock_agentcore.types.evaluation_result_content

    return [
        capo_bedrock_agentcore.types.evaluation_result_content.redact_sensitive(item)
        for item in value
    ]
