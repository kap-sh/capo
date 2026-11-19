"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormContactField``."""

from typing import Literal, TypeAlias, cast

EvaluationFormContactField: TypeAlias = Literal[
    "CATEGORIES",
    "AGENT_ARN",
    "QUEUE_ARN",
    "ROUTING_PROFILE_ARN",
    "CHANNEL",
    "INITIATION_METHOD",
    "IS_QUEUED",
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
    "RECORDING_MEDIA_STREAM_TYPES",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormContactField) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormContactField:
    return cast(EvaluationFormContactField, data)
