"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnSort``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.aggregation_function
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.sort_direction


class ColumnSort(TypedDict, closed=True):
    sort_by: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    direction: "capo_quicksight.types.sort_direction.SortDirection"
    """<p>The sort direction.</p>"""
    aggregation_function: NotRequired[
        "capo_quicksight.types.aggregation_function.AggregationFunction"
    ]
    """<p>The aggregation function that is defined in the column sort.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnSort) -> dict:
    out: dict = {}
    import capo_quicksight.types.column_identifier

    out["SortBy"] = capo_quicksight.types.column_identifier.serialize_json(
        value["sort_by"]
    )
    import capo_quicksight.types.sort_direction

    out["Direction"] = capo_quicksight.types.sort_direction.serialize_json(
        value["direction"]
    )
    if "aggregation_function" in value:
        import capo_quicksight.types.aggregation_function

        out["AggregationFunction"] = (
            capo_quicksight.types.aggregation_function.serialize_json(
                value["aggregation_function"]
            )
        )
    return out


def deserialize_json(data: dict) -> ColumnSort:
    out: ColumnSort = {}  # type: ignore[typeddict-item]
    if data.get("SortBy") is not None:
        import capo_quicksight.types.column_identifier

        out["sort_by"] = capo_quicksight.types.column_identifier.deserialize_json(
            data["SortBy"]
        )
    else:
        raise DeserializationError("ColumnSort.sort_by required")
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
    if data.get("AggregationFunction") is not None:
        import capo_quicksight.types.aggregation_function

        out["aggregation_function"] = (
            capo_quicksight.types.aggregation_function.deserialize_json(
                data["AggregationFunction"]
            )
        )
    return out
