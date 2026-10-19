"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AggregationConstraint``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.aggregation_type
    import capo_cleanrooms.types.analysis_rule_column_name


class AggregationConstraint(TypedDict, closed=True):
    column_name: (
        "capo_cleanrooms.types.analysis_rule_column_name.AnalysisRuleColumnName"
    )
    """<p>Column in aggregation constraint for which there must be a minimum number of distinct values in an output row for it to be in the query output.</p>"""
    minimum: "int"
    """<p>The minimum number of distinct values that an output row must be an aggregation of. Minimum threshold of distinct values for a specified column that must exist in an output row for it to be in the query output.</p>"""
    type: "capo_cleanrooms.types.aggregation_type.AggregationType"
    """<p>The type of aggregation the constraint allows. The only valid value is currently `COUNT_DISTINCT`.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregationConstraint) -> dict:
    out: dict = {}
    out["columnName"] = value["column_name"]
    out["minimum"] = value["minimum"]
    out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AggregationConstraint:
    out: AggregationConstraint = {}  # type: ignore[typeddict-item]
    if data.get("columnName") is not None:
        out["column_name"] = data["columnName"]
    else:
        out["column_name"] = ""
    if data.get("minimum") is not None:
        out["minimum"] = data["minimum"]
    else:
        out["minimum"] = 0
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    return out
