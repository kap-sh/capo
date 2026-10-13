"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailModalities``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_modality

GuardrailModalities: TypeAlias = list[
    "capo_bedrock.types.guardrail_modality.GuardrailModality"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailModalities) -> list:
    import capo_bedrock.types.guardrail_modality

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.guardrail_modality.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailModalities:
    import capo_bedrock.types.guardrail_modality

    out: GuardrailModalities = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock.types.guardrail_modality.deserialize_json(item))
    return out


def redact_sensitive(value: GuardrailModalities) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
