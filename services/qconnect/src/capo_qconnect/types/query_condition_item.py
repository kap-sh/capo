"""Generated from Smithy shape ``com.amazonaws.qconnect#QueryConditionItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_string
    import capo_qconnect.types.query_condition_comparison_operator
    import capo_qconnect.types.query_condition_field_name


class QueryConditionItem(TypedDict, closed=True):
    field: "capo_qconnect.types.query_condition_field_name.QueryConditionFieldName"
    """<p> The name of the field for query condition to query on.</p>"""
    comparator: "capo_qconnect.types.query_condition_comparison_operator.QueryConditionComparisonOperator"
    """<p>The comparison operator for query condition to query on.</p>"""
    value: "capo_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The value for the query condition to query on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryConditionItem) -> dict:
    out: dict = {}
    out["field"] = value["field"]
    out["comparator"] = value["comparator"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> QueryConditionItem:
    out: QueryConditionItem = {}  # type: ignore[typeddict-item]
    if data.get("field") is not None:
        out["field"] = data["field"]
    else:
        out["field"] = ""
    if data.get("comparator") is not None:
        out["comparator"] = data["comparator"]
    else:
        out["comparator"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
