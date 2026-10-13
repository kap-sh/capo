"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.data_source_summary

DataSourceSummaries: TypeAlias = list[
    "capo_datazone.types.data_source_summary.DataSourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceSummaries) -> list:
    import capo_datazone.types.data_source_summary

    out: list = []
    for item in value:
        out.append(capo_datazone.types.data_source_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSourceSummaries:
    import capo_datazone.types.data_source_summary

    out: DataSourceSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.data_source_summary.deserialize_json(item))
    return out


def redact_sensitive(value: DataSourceSummaries) -> list[Any]:
    import capo_datazone.types.data_source_summary

    return [
        capo_datazone.types.data_source_summary.redact_sensitive(item) for item in value
    ]
