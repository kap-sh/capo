"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisRuleIdMappingTable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_rule_column_list
    import capo_cleanrooms.types.query_constraint_list


class AnalysisRuleIdMappingTable(TypedDict, closed=True):
    join_columns: (
        "capo_cleanrooms.types.analysis_rule_column_list.AnalysisRuleColumnList"
    )
    """<p>The columns that query runners are allowed to use in an INNER JOIN statement.</p>"""
    query_constraints: "capo_cleanrooms.types.query_constraint_list.QueryConstraintList"
    """<p>The query constraints of the analysis rule ID mapping table.</p>"""
    dimension_columns: NotRequired[
        "capo_cleanrooms.types.analysis_rule_column_list.AnalysisRuleColumnList"
    ]
    """<p>The columns that query runners are allowed to select, group by, or filter by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisRuleIdMappingTable) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.analysis_rule_column_list

    out["joinColumns"] = capo_cleanrooms.types.analysis_rule_column_list.serialize_json(
        value["join_columns"]
    )
    import capo_cleanrooms.types.query_constraint_list

    out["queryConstraints"] = (
        capo_cleanrooms.types.query_constraint_list.serialize_json(
            value["query_constraints"]
        )
    )
    if "dimension_columns" in value:
        import capo_cleanrooms.types.analysis_rule_column_list

        out["dimensionColumns"] = (
            capo_cleanrooms.types.analysis_rule_column_list.serialize_json(
                value["dimension_columns"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnalysisRuleIdMappingTable:
    out: AnalysisRuleIdMappingTable = {}  # type: ignore[typeddict-item]
    if data.get("joinColumns") is not None:
        import capo_cleanrooms.types.analysis_rule_column_list

        out["join_columns"] = (
            capo_cleanrooms.types.analysis_rule_column_list.deserialize_json(
                data["joinColumns"]
            )
        )
    else:
        out["join_columns"] = []
    if data.get("queryConstraints") is not None:
        import capo_cleanrooms.types.query_constraint_list

        out["query_constraints"] = (
            capo_cleanrooms.types.query_constraint_list.deserialize_json(
                data["queryConstraints"]
            )
        )
    else:
        out["query_constraints"] = []
    if data.get("dimensionColumns") is not None:
        import capo_cleanrooms.types.analysis_rule_column_list

        out["dimension_columns"] = (
            capo_cleanrooms.types.analysis_rule_column_list.deserialize_json(
                data["dimensionColumns"]
            )
        )
    return out
