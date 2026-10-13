"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailManagedWordListsConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_managed_words_config

GuardrailManagedWordListsConfig: TypeAlias = list[
    "capo_bedrock.types.guardrail_managed_words_config.GuardrailManagedWordsConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailManagedWordListsConfig) -> list:
    import capo_bedrock.types.guardrail_managed_words_config

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.guardrail_managed_words_config.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GuardrailManagedWordListsConfig:
    import capo_bedrock.types.guardrail_managed_words_config

    out: GuardrailManagedWordListsConfig = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.guardrail_managed_words_config.deserialize_json(item)
        )
    return out


def redact_sensitive(value: GuardrailManagedWordListsConfig) -> list[Any]:
    import capo_bedrock.types.guardrail_managed_words_config

    return [
        capo_bedrock.types.guardrail_managed_words_config.redact_sensitive(item)
        for item in value
    ]
