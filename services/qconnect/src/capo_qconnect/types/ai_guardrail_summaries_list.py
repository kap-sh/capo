"""Generated from Smithy shape ``com.amazonaws.qconnect#AIGuardrailSummariesList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.ai_guardrail_summary

AIGuardrailSummariesList: TypeAlias = list[
    "capo_qconnect.types.ai_guardrail_summary.AIGuardrailSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AIGuardrailSummariesList) -> list:
    import capo_qconnect.types.ai_guardrail_summary

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.ai_guardrail_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AIGuardrailSummariesList:
    import capo_qconnect.types.ai_guardrail_summary

    out: AIGuardrailSummariesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.ai_guardrail_summary.deserialize_json(item))
    return out


def redact_sensitive(value: AIGuardrailSummariesList) -> list[Any]:
    import capo_qconnect.types.ai_guardrail_summary

    return [
        capo_qconnect.types.ai_guardrail_summary.redact_sensitive(item)
        for item in value
    ]
