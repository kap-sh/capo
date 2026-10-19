"""Generated from Smithy shape ``com.amazonaws.quicksight#DataPathSort``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_path_value_list
    import capo_quicksight.types.sort_direction


class DataPathSort(TypedDict, closed=True):
    direction: "capo_quicksight.types.sort_direction.SortDirection"
    """<p>Determines the sort direction.</p>"""
    sort_paths: "capo_quicksight.types.data_path_value_list.DataPathValueList"
    """<p>The list of data paths that need to be sorted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataPathSort) -> dict:
    out: dict = {}
    import capo_quicksight.types.sort_direction

    out["Direction"] = capo_quicksight.types.sort_direction.serialize_json(
        value["direction"]
    )
    import capo_quicksight.types.data_path_value_list

    out["SortPaths"] = capo_quicksight.types.data_path_value_list.serialize_json(
        value["sort_paths"]
    )
    return out


def deserialize_json(data: dict) -> DataPathSort:
    out: DataPathSort = {}  # type: ignore[typeddict-item]
    if data.get("Direction") is not None:
        import capo_quicksight.types.sort_direction

        out["direction"] = capo_quicksight.types.sort_direction.deserialize_json(
            data["Direction"]
        )
    else:
        import typing

        out["direction"] = typing.cast(
            "capo_quicksight.types.sort_direction.SortDirection", ""
        )
    if data.get("SortPaths") is not None:
        import capo_quicksight.types.data_path_value_list

        out["sort_paths"] = capo_quicksight.types.data_path_value_list.deserialize_json(
            data["SortPaths"]
        )
    else:
        out["sort_paths"] = []
    return out


def redact_sensitive(value: DataPathSort) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sort_paths" in value:
        import capo_quicksight.types.data_path_value_list

        out["sort_paths"] = capo_quicksight.types.data_path_value_list.redact_sensitive(
            value["sort_paths"]
        )
    return out
