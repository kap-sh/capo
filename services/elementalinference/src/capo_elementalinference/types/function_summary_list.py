"""Generated from Smithy shape ``com.amazonaws.elementalinference#FunctionSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_elementalinference.types.function_summary

FunctionSummaryList: TypeAlias = list[
    "capo_elementalinference.types.function_summary.FunctionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionSummaryList) -> list:
    import capo_elementalinference.types.function_summary

    out: list = []
    for item in value:
        out.append(capo_elementalinference.types.function_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> FunctionSummaryList:
    import capo_elementalinference.types.function_summary

    out: FunctionSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_elementalinference.types.function_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: FunctionSummaryList) -> list[Any]:
    import capo_elementalinference.types.function_summary

    return [
        capo_elementalinference.types.function_summary.redact_sensitive(item)
        for item in value
    ]
