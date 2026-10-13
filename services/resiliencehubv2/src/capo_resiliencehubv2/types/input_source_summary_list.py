"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#InputSourceSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.input_source_summary

InputSourceSummaryList: TypeAlias = list[
    "capo_resiliencehubv2.types.input_source_summary.InputSourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: InputSourceSummaryList) -> list:
    import capo_resiliencehubv2.types.input_source_summary

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.input_source_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> InputSourceSummaryList:
    import capo_resiliencehubv2.types.input_source_summary

    out: InputSourceSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_resiliencehubv2.types.input_source_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: InputSourceSummaryList) -> list[Any]:
    import capo_resiliencehubv2.types.input_source_summary

    return [
        capo_resiliencehubv2.types.input_source_summary.redact_sensitive(item)
        for item in value
    ]
