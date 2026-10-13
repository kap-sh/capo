"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EvaluatorSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.evaluator_summary

EvaluatorSummaryList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.evaluator_summary.EvaluatorSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorSummaryList) -> list:
    import capo_bedrock_agentcore_control.types.evaluator_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.evaluator_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EvaluatorSummaryList:
    import capo_bedrock_agentcore_control.types.evaluator_summary

    out: EvaluatorSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.evaluator_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: EvaluatorSummaryList) -> list[Any]:
    import capo_bedrock_agentcore_control.types.evaluator_summary

    return [
        capo_bedrock_agentcore_control.types.evaluator_summary.redact_sensitive(item)
        for item in value
    ]
