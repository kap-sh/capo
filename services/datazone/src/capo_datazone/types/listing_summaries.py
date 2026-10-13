"""Generated from Smithy shape ``com.amazonaws.datazone#ListingSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.listing_summary

ListingSummaries: TypeAlias = list["capo_datazone.types.listing_summary.ListingSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: ListingSummaries) -> list:
    import capo_datazone.types.listing_summary

    out: list = []
    for item in value:
        out.append(capo_datazone.types.listing_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListingSummaries:
    import capo_datazone.types.listing_summary

    out: ListingSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.listing_summary.deserialize_json(item))
    return out


def redact_sensitive(value: ListingSummaries) -> list[Any]:
    import capo_datazone.types.listing_summary

    return [
        capo_datazone.types.listing_summary.redact_sensitive(item) for item in value
    ]
