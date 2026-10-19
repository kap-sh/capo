"""Generated from Smithy shape ``com.amazonaws.quicksight#SemanticTable``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_entity_resource_id
    import capo_quicksight.types.row_level_permission_configuration
    import capo_quicksight.types.semantic_table_alias
    import capo_quicksight.types.table_semantic_metadata


class SemanticTable(TypedDict, closed=True):
    alias: "capo_quicksight.types.semantic_table_alias.SemanticTableAlias"
    """<p>Alias for the semantic table.</p>"""
    destination_table_id: (
        "capo_quicksight.types.data_set_entity_resource_id.DataSetEntityResourceId"
    )
    """<p>The identifier of the destination table from data preparation that provides data to this semantic table.</p>"""
    row_level_permission_configuration: NotRequired[
        "capo_quicksight.types.row_level_permission_configuration.RowLevelPermissionConfiguration"
    ]
    """<p>Configuration for row level security that control data access for this semantic table.</p>"""
    semantic_metadata: NotRequired[
        "capo_quicksight.types.table_semantic_metadata.TableSemanticMetadata"
    ]
    """<p>The column-level semantic metadata for this semantic table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SemanticTable) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    out["DestinationTableId"] = value["destination_table_id"]
    if "row_level_permission_configuration" in value:
        import capo_quicksight.types.row_level_permission_configuration

        out["RowLevelPermissionConfiguration"] = (
            capo_quicksight.types.row_level_permission_configuration.serialize_json(
                value["row_level_permission_configuration"]
            )
        )
    if "semantic_metadata" in value:
        import capo_quicksight.types.table_semantic_metadata

        out["SemanticMetadata"] = (
            capo_quicksight.types.table_semantic_metadata.serialize_json(
                value["semantic_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> SemanticTable:
    out: SemanticTable = {}  # type: ignore[typeddict-item]
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    else:
        out["alias"] = ""
    if data.get("DestinationTableId") is not None:
        out["destination_table_id"] = data["DestinationTableId"]
    else:
        out["destination_table_id"] = ""
    if data.get("RowLevelPermissionConfiguration") is not None:
        import capo_quicksight.types.row_level_permission_configuration

        out["row_level_permission_configuration"] = (
            capo_quicksight.types.row_level_permission_configuration.deserialize_json(
                data["RowLevelPermissionConfiguration"]
            )
        )
    if data.get("SemanticMetadata") is not None:
        import capo_quicksight.types.table_semantic_metadata

        out["semantic_metadata"] = (
            capo_quicksight.types.table_semantic_metadata.deserialize_json(
                data["SemanticMetadata"]
            )
        )
    return out


def redact_sensitive(value: SemanticTable) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "row_level_permission_configuration" in value:
        import capo_quicksight.types.row_level_permission_configuration

        out["row_level_permission_configuration"] = (
            capo_quicksight.types.row_level_permission_configuration.redact_sensitive(
                value["row_level_permission_configuration"]
            )
        )
    if "semantic_metadata" in value:
        import capo_quicksight.types.table_semantic_metadata

        out["semantic_metadata"] = (
            capo_quicksight.types.table_semantic_metadata.redact_sensitive(
                value["semantic_metadata"]
            )
        )
    return out
