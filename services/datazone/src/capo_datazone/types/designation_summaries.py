"""Generated from Smithy shape ``com.amazonaws.datazone#DesignationSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.designation_summary

DesignationSummaries: TypeAlias = list[
    "capo_datazone.types.designation_summary.DesignationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DesignationSummaries) -> list:
    import capo_datazone.types.designation_summary

    out: list = []
    for item in value:
        out.append(capo_datazone.types.designation_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DesignationSummaries:
    import capo_datazone.types.designation_summary

    out: DesignationSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.designation_summary.deserialize_json(item))
    return out


def redact_sensitive(value: DesignationSummaries) -> list[Any]:
    import capo_datazone.types.designation_summary

    return [
        capo_datazone.types.designation_summary.redact_sensitive(item) for item in value
    ]
