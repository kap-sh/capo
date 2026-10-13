"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailManagedWordLists``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_managed_words

GuardrailManagedWordLists: TypeAlias = list[
    "capo_bedrock.types.guardrail_managed_words.GuardrailManagedWords"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailManagedWordLists) -> list:
    import capo_bedrock.types.guardrail_managed_words

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.guardrail_managed_words.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailManagedWordLists:
    import capo_bedrock.types.guardrail_managed_words

    out: GuardrailManagedWordLists = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock.types.guardrail_managed_words.deserialize_json(item))
    return out


def redact_sensitive(value: GuardrailManagedWordLists) -> list[Any]:
    import capo_bedrock.types.guardrail_managed_words

    return [
        capo_bedrock.types.guardrail_managed_words.redact_sensitive(item)
        for item in value
    ]
