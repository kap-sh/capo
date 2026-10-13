"""Generated from Smithy shape ``com.amazonaws.datazone#AssetFilters``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.asset_filter_summary

AssetFilters: TypeAlias = list[
    "capo_datazone.types.asset_filter_summary.AssetFilterSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetFilters) -> list:
    import capo_datazone.types.asset_filter_summary

    out: list = []
    for item in value:
        out.append(capo_datazone.types.asset_filter_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssetFilters:
    import capo_datazone.types.asset_filter_summary

    out: AssetFilters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.asset_filter_summary.deserialize_json(item))
    return out


def redact_sensitive(value: AssetFilters) -> list[Any]:
    import capo_datazone.types.asset_filter_summary

    return [
        capo_datazone.types.asset_filter_summary.redact_sensitive(item)
        for item in value
    ]
