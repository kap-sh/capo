"""Generated from Smithy shape ``com.amazonaws.cleanrooms#InheritedDisallowedOutputColumns``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_rule_column_name_list
    import capo_cleanrooms.types.column_lineage_list


class InheritedDisallowedOutputColumns(TypedDict, closed=True):
    value: "capo_cleanrooms.types.analysis_rule_column_name_list.AnalysisRuleColumnNameList"
    """<p>The list of column names that are disallowed from appearing in query output, inherited from parent tables.</p>"""
    column_lineage: "capo_cleanrooms.types.column_lineage_list.ColumnLineageList"
    """<p>The lineage information that traces each disallowed output column back to its source in a parent table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InheritedDisallowedOutputColumns) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.analysis_rule_column_name_list

    out["value"] = capo_cleanrooms.types.analysis_rule_column_name_list.serialize_json(
        value["value"]
    )
    import capo_cleanrooms.types.column_lineage_list

    out["columnLineage"] = capo_cleanrooms.types.column_lineage_list.serialize_json(
        value["column_lineage"]
    )
    return out


def deserialize_json(data: dict) -> InheritedDisallowedOutputColumns:
    out: InheritedDisallowedOutputColumns = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        import capo_cleanrooms.types.analysis_rule_column_name_list

        out["value"] = (
            capo_cleanrooms.types.analysis_rule_column_name_list.deserialize_json(
                data["value"]
            )
        )
    else:
        out["value"] = []
    if data.get("columnLineage") is not None:
        import capo_cleanrooms.types.column_lineage_list

        out["column_lineage"] = (
            capo_cleanrooms.types.column_lineage_list.deserialize_json(
                data["columnLineage"]
            )
        )
    else:
        out["column_lineage"] = []
    return out
