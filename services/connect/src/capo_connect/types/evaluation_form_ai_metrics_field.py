"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormAiMetricsField``."""

from typing import Literal, TypeAlias, cast

EvaluationFormAiMetricsField: TypeAlias = Literal[
    "AI_SESSION_IS_HANDED_OFF",
    "AI_SESSION_SELF_SERVICE_DURATION",
    "AI_SESSION_GOAL_SUCCESS_RATE",
    "AI_SESSION_COMPLETENESS_SCORE",
    "AI_SESSION_FAITHFULNESS_SCORE",
    "AI_AGENT_MAX_PROMPT_LATENCY",
    "AI_TOOL_MAX_LATENCY",
    "AI_TOOL_SELECTION_ACCURACY",
    "AI_TOOL_PARAMETER_ACCURACY",
    "AI_TOOL_UTILIZATION_ACCURACY",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormAiMetricsField) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormAiMetricsField:
    return cast(EvaluationFormAiMetricsField, data)
