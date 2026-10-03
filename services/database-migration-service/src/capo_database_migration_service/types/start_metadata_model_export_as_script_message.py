"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartMetadataModelExportAsScriptMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.migration_project_identifier
    import capo_database_migration_service.types.origin_type_value
    import capo_database_migration_service.types.string


class StartMetadataModelExportAsScriptMessage(TypedDict, closed=True):
    migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier"
    """<p>The migration project name or Amazon Resource Name (ARN).</p>"""
    selection_rules: "capo_database_migration_service.types.string.String"
    """<p>A JSON string that identifies the metadata models to export as a SQL script. For the selection rule format and examples, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html">Selection rules in DMS Schema Conversion</a>.</p> <p>Usage:</p> <ul> <li> <p>Accepts source or target selection rules depending on the <code>Origin</code> parameter. The <code>server-name</code> in the object locator must match the corresponding data provider.</p> </li> <li> <p>Supports <code>explicit</code>, <code>include</code>, and <code>exclude</code> rule actions.</p> </li> </ul>"""
    origin: "capo_database_migration_service.types.origin_type_value.OriginTypeValue"
    """<p>Specifies the metadata tree to export from.</p>"""
    file_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The name for the exported file. When you omit this parameter, the service generates a name from the data provider engine name and an export timestamp.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMetadataModelExportAsScriptMessage) -> dict:
    out: dict = {}
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    out["SelectionRules"] = value["selection_rules"]
    import capo_database_migration_service.types.origin_type_value

    out["Origin"] = (
        capo_database_migration_service.types.origin_type_value.serialize_aws_json_1_1(
            value["origin"]
        )
    )
    if "file_name" in value:
        out["FileName"] = value["file_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMetadataModelExportAsScriptMessage:
    out: StartMetadataModelExportAsScriptMessage = {}  # type: ignore[typeddict-item]
    if data.get("MigrationProjectIdentifier") is not None:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    else:
        raise DeserializationError(
            "StartMetadataModelExportAsScriptMessage.migration_project_identifier required"
        )
    if data.get("SelectionRules") is not None:
        out["selection_rules"] = data["SelectionRules"]
    else:
        raise DeserializationError(
            "StartMetadataModelExportAsScriptMessage.selection_rules required"
        )
    if data.get("Origin") is not None:
        import capo_database_migration_service.types.origin_type_value

        out["origin"] = (
            capo_database_migration_service.types.origin_type_value.deserialize_aws_json_1_1(
                data["Origin"]
            )
        )
    else:
        raise DeserializationError(
            "StartMetadataModelExportAsScriptMessage.origin required"
        )
    if data.get("FileName") is not None:
        out["file_name"] = data["FileName"]
    return out
