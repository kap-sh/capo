"""Generated from Smithy shape ``com.amazonaws.wisdom#QuickResponseSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_wisdom.types.quick_response_summary

QuickResponseSummaryList: TypeAlias = list[
    "capo_wisdom.types.quick_response_summary.QuickResponseSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuickResponseSummaryList) -> list:
    import capo_wisdom.types.quick_response_summary

    out: list = []
    for item in value:
        out.append(capo_wisdom.types.quick_response_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuickResponseSummaryList:
    import capo_wisdom.types.quick_response_summary

    out: QuickResponseSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_wisdom.types.quick_response_summary.deserialize_json(item))
    return out


def redact_sensitive(value: QuickResponseSummaryList) -> list[Any]:
    import capo_wisdom.types.quick_response_summary

    return [
        capo_wisdom.types.quick_response_summary.redact_sensitive(item)
        for item in value
    ]
