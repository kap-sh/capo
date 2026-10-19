"""Generated from Smithy shape ``com.amazonaws.quicksight#AggregationSortConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.aggregation_function
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.sort_direction


class AggregationSortConfiguration(TypedDict, closed=True):
    column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that determines the sort order of aggregated values.</p>"""
    sort_direction: "capo_quicksight.types.sort_direction.SortDirection"
    """<p>The sort direction of values.</p> <ul> <li> <p> <code>ASC</code>: Sort in ascending order.</p> </li> <li> <p> <code>DESC</code>: Sort in descending order.</p> </li> </ul>"""
    aggregation_function: NotRequired[
        "capo_quicksight.types.aggregation_function.AggregationFunction"
    ]
    """<p>The function that aggregates the values in <code>Column</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregationSortConfiguration) -> dict:
    out: dict = {}
    import capo_quicksight.types.column_identifier

    out["Column"] = capo_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    import capo_quicksight.types.sort_direction

    out["SortDirection"] = capo_quicksight.types.sort_direction.serialize_json(
        value["sort_direction"]
    )
    if "aggregation_function" in value:
        import capo_quicksight.types.aggregation_function

        out["AggregationFunction"] = (
            capo_quicksight.types.aggregation_function.serialize_json(
                value["aggregation_function"]
            )
        )
    return out


def deserialize_json(data: dict) -> AggregationSortConfiguration:
    out: AggregationSortConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Column") is not None:
        import capo_quicksight.types.column_identifier

        out["column"] = capo_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("AggregationSortConfiguration.column required")
    if data.get("SortDirection") is not None:
        import capo_quicksight.types.sort_direction

        out["sort_direction"] = capo_quicksight.types.sort_direction.deserialize_json(
            data["SortDirection"]
        )
    else:
        import typing

        out["sort_direction"] = typing.cast(
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
