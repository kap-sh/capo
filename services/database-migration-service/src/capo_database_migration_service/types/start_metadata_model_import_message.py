"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartMetadataModelImportMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean
    import capo_database_migration_service.types.migration_project_identifier
    import capo_database_migration_service.types.origin_type_value
    import capo_database_migration_service.types.string


class StartMetadataModelImportMessage(TypedDict, closed=True):
    migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier"
    """<p>The migration project name or Amazon Resource Name (ARN).</p>"""
    selection_rules: "capo_database_migration_service.types.string.String"
    """<p>A JSON string that identifies the metadata models to import from the data provider. For the selection rule format and examples, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html">Selection rules in DMS Schema Conversion</a>.</p> <p>Usage:</p> <ul> <li> <p>Accepts source or target selection rules depending on the <code>Origin</code> parameter. The <code>server-name</code> in the object locator must match the corresponding data provider.</p> </li> <li> <p>Supports <code>explicit</code>, <code>include</code>, and <code>exclude</code> rule actions.</p> </li> </ul>"""
    origin: "capo_database_migration_service.types.origin_type_value.OriginTypeValue"
    """<p>Specifies the metadata tree to import into.</p> <note> <p>You cannot import from a virtual target data provider.</p> </note>"""
    refresh: "capo_database_migration_service.types.boolean.Boolean"
    """<p>Specifies whether to refresh the selected metadata models from the data provider.</p> <p>When <code>true</code>, the import reloads the selected metadata models with current definitions and removes their existing subtree.</p> <p>When <code>false</code> (default), the import loads the full subtree that has not yet been loaded into the metadata tree.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMetadataModelImportMessage) -> dict:
    out: dict = {}
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    out["SelectionRules"] = value["selection_rules"]
    import capo_database_migration_service.types.origin_type_value

    out["Origin"] = (
        capo_database_migration_service.types.origin_type_value.serialize_aws_json_1_1(
            value["origin"]
        )
    )
    out["Refresh"] = value.get("refresh", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMetadataModelImportMessage:
    out: StartMetadataModelImportMessage = {}  # type: ignore[typeddict-item]
    if data.get("MigrationProjectIdentifier") is not None:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    else:
        raise DeserializationError(
            "StartMetadataModelImportMessage.migration_project_identifier required"
        )
    if data.get("SelectionRules") is not None:
        out["selection_rules"] = data["SelectionRules"]
    else:
        raise DeserializationError(
            "StartMetadataModelImportMessage.selection_rules required"
        )
    if data.get("Origin") is not None:
        import capo_database_migration_service.types.origin_type_value

        out["origin"] = (
            capo_database_migration_service.types.origin_type_value.deserialize_aws_json_1_1(
                data["Origin"]
            )
        )
    else:
        raise DeserializationError("StartMetadataModelImportMessage.origin required")
    if data.get("Refresh") is not None:
        out["refresh"] = data["Refresh"]
    else:
        out["refresh"] = False
    return out
