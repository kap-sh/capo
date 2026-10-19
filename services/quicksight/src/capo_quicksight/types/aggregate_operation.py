"""Generated from Smithy shape ``com.amazonaws.quicksight#AggregateOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.aggregation_list
    import capo_quicksight.types.group_by_column_name_list
    import capo_quicksight.types.transform_operation_alias
    import capo_quicksight.types.transform_operation_source


class AggregateOperation(TypedDict, closed=True):
    alias: "capo_quicksight.types.transform_operation_alias.TransformOperationAlias"
    """<p>Alias for this operation.</p>"""
    source: "capo_quicksight.types.transform_operation_source.TransformOperationSource"
    """<p>The source transform operation that provides input data for the aggregation.</p>"""
    group_by_column_names: NotRequired[
        "capo_quicksight.types.group_by_column_name_list.GroupByColumnNameList"
    ]
    """<p>The list of column names to group by when performing the aggregation. Rows with the same values in these columns will be grouped together.</p>"""
    aggregations: "capo_quicksight.types.aggregation_list.AggregationList"
    """<p>The list of aggregation functions to apply to the grouped data, such as <code>SUM</code>, <code>COUNT</code>, or <code>AVERAGE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregateOperation) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    import capo_quicksight.types.transform_operation_source

    out["Source"] = capo_quicksight.types.transform_operation_source.serialize_json(
        value["source"]
    )
    if "group_by_column_names" in value:
        import capo_quicksight.types.group_by_column_name_list

        out["GroupByColumnNames"] = (
            capo_quicksight.types.group_by_column_name_list.serialize_json(
                value["group_by_column_names"]
            )
        )
    import capo_quicksight.types.aggregation_list

    out["Aggregations"] = capo_quicksight.types.aggregation_list.serialize_json(
        value["aggregations"]
    )
    return out


def deserialize_json(data: dict) -> AggregateOperation:
    out: AggregateOperation = {}  # type: ignore[typeddict-item]
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    else:
        out["alias"] = ""
    if data.get("Source") is not None:
        import capo_quicksight.types.transform_operation_source

        out["source"] = (
            capo_quicksight.types.transform_operation_source.deserialize_json(
                data["Source"]
            )
        )
    else:
        raise DeserializationError("AggregateOperation.source required")
    if data.get("GroupByColumnNames") is not None:
        import capo_quicksight.types.group_by_column_name_list

        out["group_by_column_names"] = (
            capo_quicksight.types.group_by_column_name_list.deserialize_json(
                data["GroupByColumnNames"]
            )
        )
    if data.get("Aggregations") is not None:
        import capo_quicksight.types.aggregation_list

        out["aggregations"] = capo_quicksight.types.aggregation_list.deserialize_json(
            data["Aggregations"]
        )
    else:
        out["aggregations"] = []
    return out
