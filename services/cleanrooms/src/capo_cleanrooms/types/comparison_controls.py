"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ComparisonControls``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_rule_column_list


class ComparisonControls(TypedDict, closed=True):
    allowed_literal_comparison_columns: (
        "capo_cleanrooms.types.analysis_rule_column_list.AnalysisRuleColumnList"
    )
    """<p>The columns that a query can compare to literal values, for example, in a WHERE clause. Clean Rooms rejects a query that compares any other column to a literal value. Specify an empty list to block literal comparison on every column. You can't specify a column that you also use as an identity column in an aggregation threshold.</p>"""
    allowed_column_comparison_columns: (
        "capo_cleanrooms.types.analysis_rule_column_list.AnalysisRuleColumnList"
    )
    """<p>The columns that a query can compare to another column, for example, in a join, a WHERE clause, a GROUP BY clause, or a window function. Clean Rooms rejects a query that uses any other column in a column-to-column comparison. Specify an empty list to block column-to-column comparison on every column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComparisonControls) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.analysis_rule_column_list

    out["allowedLiteralComparisonColumns"] = (
        capo_cleanrooms.types.analysis_rule_column_list.serialize_json(
            value["allowed_literal_comparison_columns"]
        )
    )
    import capo_cleanrooms.types.analysis_rule_column_list

    out["allowedColumnComparisonColumns"] = (
        capo_cleanrooms.types.analysis_rule_column_list.serialize_json(
            value["allowed_column_comparison_columns"]
        )
    )
    return out


def deserialize_json(data: dict) -> ComparisonControls:
    out: ComparisonControls = {}  # type: ignore[typeddict-item]
    if data.get("allowedLiteralComparisonColumns") is not None:
        import capo_cleanrooms.types.analysis_rule_column_list

        out["allowed_literal_comparison_columns"] = (
            capo_cleanrooms.types.analysis_rule_column_list.deserialize_json(
                data["allowedLiteralComparisonColumns"]
            )
        )
    else:
        out["allowed_literal_comparison_columns"] = []
    if data.get("allowedColumnComparisonColumns") is not None:
        import capo_cleanrooms.types.analysis_rule_column_list

        out["allowed_column_comparison_columns"] = (
            capo_cleanrooms.types.analysis_rule_column_list.deserialize_json(
                data["allowedColumnComparisonColumns"]
            )
        )
    else:
        out["allowed_column_comparison_columns"] = []
    return out
