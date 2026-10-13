"""Generated from Smithy shape ``com.amazonaws.qconnect#AIGuardrailVersionSummariesList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.ai_guardrail_version_summary

AIGuardrailVersionSummariesList: TypeAlias = list[
    "capo_qconnect.types.ai_guardrail_version_summary.AIGuardrailVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AIGuardrailVersionSummariesList) -> list:
    import capo_qconnect.types.ai_guardrail_version_summary

    out: list = []
    for item in value:
        out.append(
            capo_qconnect.types.ai_guardrail_version_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AIGuardrailVersionSummariesList:
    import capo_qconnect.types.ai_guardrail_version_summary

    out: AIGuardrailVersionSummariesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_qconnect.types.ai_guardrail_version_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: AIGuardrailVersionSummariesList) -> list[Any]:
    import capo_qconnect.types.ai_guardrail_version_summary

    return [
        capo_qconnect.types.ai_guardrail_version_summary.redact_sensitive(item)
        for item in value
    ]
