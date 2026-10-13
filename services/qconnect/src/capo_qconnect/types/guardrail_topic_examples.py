"""Generated from Smithy shape ``com.amazonaws.qconnect#GuardrailTopicExamples``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.guardrail_topic_example

GuardrailTopicExamples: TypeAlias = list[
    "capo_qconnect.types.guardrail_topic_example.GuardrailTopicExample"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopicExamples) -> list:
    return list(value)


def deserialize_json(data: list) -> GuardrailTopicExamples:
    return [item for item in data if item is not None]


def redact_sensitive(value: GuardrailTopicExamples) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
