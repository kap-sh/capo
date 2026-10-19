"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisRuleList``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.additional_analyses
    import capo_cleanrooms.types.analysis_rule_column_list
    import capo_cleanrooms.types.join_operators_list


class AnalysisRuleList(TypedDict, closed=True):
    join_columns: (
        "capo_cleanrooms.types.analysis_rule_column_list.AnalysisRuleColumnList"
    )
    """<p>Columns that can be used to join a configured table with the table of the member who can query and other members' configured tables.</p>"""
    allowed_join_operators: NotRequired[
        "capo_cleanrooms.types.join_operators_list.JoinOperatorsList"
    ]
    """<p>The logical operators (if any) that are to be used in an INNER JOIN match condition. Default is <code>AND</code>.</p>"""
    list_columns: (
        "capo_cleanrooms.types.analysis_rule_column_list.AnalysisRuleColumnList"
    )
    """<p>Columns that can be listed in the output.</p>"""
    additional_analyses: NotRequired[
        "capo_cleanrooms.types.additional_analyses.AdditionalAnalyses"
    ]
    """<p> An indicator as to whether additional analyses (such as Clean Rooms ML) can be applied to the output of the direct query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisRuleList) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.analysis_rule_column_list

    out["joinColumns"] = capo_cleanrooms.types.analysis_rule_column_list.serialize_json(
        value["join_columns"]
    )
    if "allowed_join_operators" in value:
        import capo_cleanrooms.types.join_operators_list

        out["allowedJoinOperators"] = (
            capo_cleanrooms.types.join_operators_list.serialize_json(
                value["allowed_join_operators"]
            )
        )
    import capo_cleanrooms.types.analysis_rule_column_list

    out["listColumns"] = capo_cleanrooms.types.analysis_rule_column_list.serialize_json(
        value["list_columns"]
    )
    if "additional_analyses" in value:
        import capo_cleanrooms.types.additional_analyses

        out["additionalAnalyses"] = (
            capo_cleanrooms.types.additional_analyses.serialize_json(
                value["additional_analyses"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnalysisRuleList:
    out: AnalysisRuleList = {}  # type: ignore[typeddict-item]
    if data.get("joinColumns") is not None:
        import capo_cleanrooms.types.analysis_rule_column_list

        out["join_columns"] = (
            capo_cleanrooms.types.analysis_rule_column_list.deserialize_json(
                data["joinColumns"]
            )
        )
    else:
        out["join_columns"] = []
    if data.get("allowedJoinOperators") is not None:
        import capo_cleanrooms.types.join_operators_list

        out["allowed_join_operators"] = (
            capo_cleanrooms.types.join_operators_list.deserialize_json(
                data["allowedJoinOperators"]
            )
        )
    if data.get("listColumns") is not None:
        import capo_cleanrooms.types.analysis_rule_column_list

        out["list_columns"] = (
            capo_cleanrooms.types.analysis_rule_column_list.deserialize_json(
                data["listColumns"]
            )
        )
    else:
        out["list_columns"] = []
    if data.get("additionalAnalyses") is not None:
        import capo_cleanrooms.types.additional_analyses

        out["additional_analyses"] = (
            capo_cleanrooms.types.additional_analyses.deserialize_json(
                data["additionalAnalyses"]
            )
        )
    return out
