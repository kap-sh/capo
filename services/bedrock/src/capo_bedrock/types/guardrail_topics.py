"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailTopics``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_topic

GuardrailTopics: TypeAlias = list["capo_bedrock.types.guardrail_topic.GuardrailTopic"]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopics) -> list:
    import capo_bedrock.types.guardrail_topic

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.guardrail_topic.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailTopics:
    import capo_bedrock.types.guardrail_topic

    out: GuardrailTopics = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock.types.guardrail_topic.deserialize_json(item))
    return out


def redact_sensitive(value: GuardrailTopics) -> list[Any]:
    import capo_bedrock.types.guardrail_topic

    return [capo_bedrock.types.guardrail_topic.redact_sensitive(item) for item in value]
