"""Generated from Smithy shape ``com.amazonaws.qconnect#GuardrailWordsConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.guardrail_word_config

GuardrailWordsConfig: TypeAlias = list[
    "capo_qconnect.types.guardrail_word_config.GuardrailWordConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailWordsConfig) -> list:
    import capo_qconnect.types.guardrail_word_config

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.guardrail_word_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailWordsConfig:
    import capo_qconnect.types.guardrail_word_config

    out: GuardrailWordsConfig = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.guardrail_word_config.deserialize_json(item))
    return out


def redact_sensitive(value: GuardrailWordsConfig) -> list[Any]:
    import capo_qconnect.types.guardrail_word_config

    return [
        capo_qconnect.types.guardrail_word_config.redact_sensitive(item)
        for item in value
    ]
