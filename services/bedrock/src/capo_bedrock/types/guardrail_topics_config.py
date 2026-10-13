"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailTopicsConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_topic_config

GuardrailTopicsConfig: TypeAlias = list[
    "capo_bedrock.types.guardrail_topic_config.GuardrailTopicConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopicsConfig) -> list:
    import capo_bedrock.types.guardrail_topic_config

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.guardrail_topic_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailTopicsConfig:
    import capo_bedrock.types.guardrail_topic_config

    out: GuardrailTopicsConfig = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock.types.guardrail_topic_config.deserialize_json(item))
    return out


def redact_sensitive(value: GuardrailTopicsConfig) -> list[Any]:
    import capo_bedrock.types.guardrail_topic_config

    return [
        capo_bedrock.types.guardrail_topic_config.redact_sensitive(item)
        for item in value
    ]
