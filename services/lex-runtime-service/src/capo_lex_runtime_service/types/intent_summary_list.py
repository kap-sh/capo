"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#IntentSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_lex_runtime_service.types.intent_summary

IntentSummaryList: TypeAlias = list[
    "capo_lex_runtime_service.types.intent_summary.IntentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntentSummaryList) -> list:
    import capo_lex_runtime_service.types.intent_summary

    out: list = []
    for item in value:
        out.append(capo_lex_runtime_service.types.intent_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> IntentSummaryList:
    import capo_lex_runtime_service.types.intent_summary

    out: IntentSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lex_runtime_service.types.intent_summary.deserialize_json(item))
    return out


def redact_sensitive(value: IntentSummaryList) -> list[Any]:
    import capo_lex_runtime_service.types.intent_summary

    return [
        capo_lex_runtime_service.types.intent_summary.redact_sensitive(item)
        for item in value
    ]
