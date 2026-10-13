"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailWords``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_word

GuardrailWords: TypeAlias = list["capo_bedrock.types.guardrail_word.GuardrailWord"]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailWords) -> list:
    import capo_bedrock.types.guardrail_word

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.guardrail_word.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailWords:
    import capo_bedrock.types.guardrail_word

    out: GuardrailWords = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock.types.guardrail_word.deserialize_json(item))
    return out


def redact_sensitive(value: GuardrailWords) -> list[Any]:
    import capo_bedrock.types.guardrail_word

    return [capo_bedrock.types.guardrail_word.redact_sensitive(item) for item in value]
