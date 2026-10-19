"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AggregateColumn``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.aggregate_function_name
    import capo_cleanrooms.types.analysis_rule_column_name_list


class AggregateColumn(TypedDict, closed=True):
    column_names: "capo_cleanrooms.types.analysis_rule_column_name_list.AnalysisRuleColumnNameList"
    """<p>Column names in configured table of aggregate columns.</p>"""
    function: "capo_cleanrooms.types.aggregate_function_name.AggregateFunctionName"
    """<p>Aggregation function that can be applied to aggregate column in query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregateColumn) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.analysis_rule_column_name_list

    out["columnNames"] = (
        capo_cleanrooms.types.analysis_rule_column_name_list.serialize_json(
            value["column_names"]
        )
    )
    out["function"] = value["function"]
    return out


def deserialize_json(data: dict) -> AggregateColumn:
    out: AggregateColumn = {}  # type: ignore[typeddict-item]
    if data.get("columnNames") is not None:
        import capo_cleanrooms.types.analysis_rule_column_name_list

        out["column_names"] = (
            capo_cleanrooms.types.analysis_rule_column_name_list.deserialize_json(
                data["columnNames"]
            )
        )
    else:
        out["column_names"] = []
    if data.get("function") is not None:
        out["function"] = data["function"]
    else:
        out["function"] = ""
    return out
