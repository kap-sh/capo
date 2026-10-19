"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ColumnLineageEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.analysis_rule_column_name
    import capo_cleanrooms.types.base_table_dependency_type
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.uuid


class ColumnLineageEntry(TypedDict, closed=True):
    column: "capo_cleanrooms.types.analysis_rule_column_name.AnalysisRuleColumnName"
    """<p>The name of the column in the intermediate table.</p>"""
    source_column: (
        "capo_cleanrooms.types.analysis_rule_column_name.AnalysisRuleColumnName"
    )
    """<p>The name of the column in the source table.</p>"""
    source_name: "capo_cleanrooms.types.display_name.DisplayName"
    """<p>The name of the source table.</p>"""
    source_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the source table.</p>"""
    source_type: (
        "capo_cleanrooms.types.base_table_dependency_type.BaseTableDependencyType"
    )
    """<p>The type of the source table.</p>"""
    source_account_id: "capo_cleanrooms.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the owner of the source table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnLineageEntry) -> dict:
    out: dict = {}
    out["column"] = value["column"]
    out["sourceColumn"] = value["source_column"]
    out["sourceName"] = value["source_name"]
    out["sourceId"] = value["source_id"]
    import capo_cleanrooms.types.base_table_dependency_type

    out["sourceType"] = capo_cleanrooms.types.base_table_dependency_type.serialize_json(
        value["source_type"]
    )
    out["sourceAccountId"] = value["source_account_id"]
    return out


def deserialize_json(data: dict) -> ColumnLineageEntry:
    out: ColumnLineageEntry = {}  # type: ignore[typeddict-item]
    if data.get("column") is not None:
        out["column"] = data["column"]
    else:
        out["column"] = ""
    if data.get("sourceColumn") is not None:
        out["source_column"] = data["sourceColumn"]
    else:
        out["source_column"] = ""
    if data.get("sourceName") is not None:
        out["source_name"] = data["sourceName"]
    else:
        out["source_name"] = ""
    if data.get("sourceId") is not None:
        out["source_id"] = data["sourceId"]
    else:
        out["source_id"] = ""
    if data.get("sourceType") is not None:
        import capo_cleanrooms.types.base_table_dependency_type

        out["source_type"] = (
            capo_cleanrooms.types.base_table_dependency_type.deserialize_json(
                data["sourceType"]
            )
        )
    else:
        import typing

        out["source_type"] = typing.cast(
            "capo_cleanrooms.types.base_table_dependency_type.BaseTableDependencyType",
            "",
        )
    if data.get("sourceAccountId") is not None:
        out["source_account_id"] = data["sourceAccountId"]
    else:
        out["source_account_id"] = ""
    return out
