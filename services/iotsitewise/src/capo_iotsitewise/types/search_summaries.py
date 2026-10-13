"""Generated from Smithy shape ``com.amazonaws.iotsitewise#SearchSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.search_summary

SearchSummaries: TypeAlias = list["capo_iotsitewise.types.search_summary.SearchSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: SearchSummaries) -> list:
    import capo_iotsitewise.types.search_summary

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.search_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchSummaries:
    import capo_iotsitewise.types.search_summary

    out: SearchSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_iotsitewise.types.search_summary.deserialize_json(item))
    return out


def redact_sensitive(value: SearchSummaries) -> list[Any]:
    import capo_iotsitewise.types.search_summary

    return [
        capo_iotsitewise.types.search_summary.redact_sensitive(item) for item in value
    ]
