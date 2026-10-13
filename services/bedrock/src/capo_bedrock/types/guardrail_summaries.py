"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_summary

GuardrailSummaries: TypeAlias = list[
    "capo_bedrock.types.guardrail_summary.GuardrailSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailSummaries) -> list:
    import capo_bedrock.types.guardrail_summary

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.guardrail_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailSummaries:
    import capo_bedrock.types.guardrail_summary

    out: GuardrailSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock.types.guardrail_summary.deserialize_json(item))
    return out


def redact_sensitive(value: GuardrailSummaries) -> list[Any]:
    import capo_bedrock.types.guardrail_summary

    return [
        capo_bedrock.types.guardrail_summary.redact_sensitive(item) for item in value
    ]
