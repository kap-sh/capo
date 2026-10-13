"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceRunActivities``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.data_source_run_activity

DataSourceRunActivities: TypeAlias = list[
    "capo_datazone.types.data_source_run_activity.DataSourceRunActivity"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceRunActivities) -> list:
    import capo_datazone.types.data_source_run_activity

    out: list = []
    for item in value:
        out.append(capo_datazone.types.data_source_run_activity.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSourceRunActivities:
    import capo_datazone.types.data_source_run_activity

    out: DataSourceRunActivities = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.data_source_run_activity.deserialize_json(item))
    return out


def redact_sensitive(value: DataSourceRunActivities) -> list[Any]:
    import capo_datazone.types.data_source_run_activity

    return [
        capo_datazone.types.data_source_run_activity.redact_sensitive(item)
        for item in value
    ]
