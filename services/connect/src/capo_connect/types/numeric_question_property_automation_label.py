"""Generated from Smithy shape ``com.amazonaws.connect#NumericQuestionPropertyAutomationLabel``."""

from typing import Literal, TypeAlias, cast

NumericQuestionPropertyAutomationLabel: TypeAlias = Literal[
    "OVERALL_CUSTOMER_SENTIMENT_SCORE",
    "OVERALL_AGENT_SENTIMENT_SCORE",
    "CUSTOMER_SENTIMENT_SCORE_WITHOUT_AGENT",
    "CUSTOMER_SENTIMENT_SCORE_WITH_AGENT",
    "NON_TALK_TIME",
    "NON_TALK_TIME_PERCENTAGE",
    "NUMBER_OF_INTERRUPTIONS",
    "CONTACT_DURATION",
    "AGENT_INTERACTION_DURATION",
    "CUSTOMER_HOLD_TIME",
    "LONGEST_HOLD_DURATION",
    "NUMBER_OF_HOLDS",
    "AGENT_INTERACTION_AND_HOLD_DURATION",
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
def serialize_json(value: NumericQuestionPropertyAutomationLabel) -> str:
    return value


def deserialize_json(data: str) -> NumericQuestionPropertyAutomationLabel:
    return cast(NumericQuestionPropertyAutomationLabel, data)
