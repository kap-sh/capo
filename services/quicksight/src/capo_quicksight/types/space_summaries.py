"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.space_summary

SpaceSummaries: TypeAlias = list["capo_quicksight.types.space_summary.SpaceSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: SpaceSummaries) -> list:
    import capo_quicksight.types.space_summary

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.space_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SpaceSummaries:
    import capo_quicksight.types.space_summary

    out: SpaceSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.space_summary.deserialize_json(item))
    return out


def redact_sensitive(value: SpaceSummaries) -> list[Any]:
    import capo_quicksight.types.space_summary

    return [
        capo_quicksight.types.space_summary.redact_sensitive(item) for item in value
    ]
