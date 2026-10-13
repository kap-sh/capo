"""Generated from Smithy shape ``com.amazonaws.qconnect#GuardrailRegexesConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.guardrail_regex_config

GuardrailRegexesConfig: TypeAlias = list[
    "capo_qconnect.types.guardrail_regex_config.GuardrailRegexConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailRegexesConfig) -> list:
    import capo_qconnect.types.guardrail_regex_config

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.guardrail_regex_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailRegexesConfig:
    import capo_qconnect.types.guardrail_regex_config

    out: GuardrailRegexesConfig = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.guardrail_regex_config.deserialize_json(item))
    return out


def redact_sensitive(value: GuardrailRegexesConfig) -> list[Any]:
    import capo_qconnect.types.guardrail_regex_config

    return [
        capo_qconnect.types.guardrail_regex_config.redact_sensitive(item)
        for item in value
    ]
