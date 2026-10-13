"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#OnlineEvaluationConfigSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.online_evaluation_config_summary

OnlineEvaluationConfigSummaryList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.online_evaluation_config_summary.OnlineEvaluationConfigSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: OnlineEvaluationConfigSummaryList) -> list:
    import capo_bedrock_agentcore_control.types.online_evaluation_config_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.online_evaluation_config_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> OnlineEvaluationConfigSummaryList:
    import capo_bedrock_agentcore_control.types.online_evaluation_config_summary

    out: OnlineEvaluationConfigSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.online_evaluation_config_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: OnlineEvaluationConfigSummaryList) -> list[Any]:
    import capo_bedrock_agentcore_control.types.online_evaluation_config_summary

    return [
        capo_bedrock_agentcore_control.types.online_evaluation_config_summary.redact_sensitive(
            item
        )
        for item in value
    ]
