"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartMetadataModelExportToTargetMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.migration_project_identifier
    import capo_database_migration_service.types.string


class StartMetadataModelExportToTargetMessage(TypedDict, closed=True):
    migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier"
    """<p>The migration project name or Amazon Resource Name (ARN).</p>"""
    selection_rules: "capo_database_migration_service.types.string.String"
    """<p>A JSON string that identifies the metadata models to export to the target database. For the selection rule format and examples, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html">Selection rules in DMS Schema Conversion</a>.</p> <p>Usage:</p> <ul> <li> <p>Accepts only target selection rules, where <code>server-name</code> in the object locator matches the target data provider.</p> </li> <li> <p>Supports <code>explicit</code>, <code>include</code>, and <code>exclude</code> rule actions.</p> </li> </ul>"""
    overwrite_extension_pack: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to overwrite the extension pack if one already exists on the target database. The default value is <code>true</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMetadataModelExportToTargetMessage) -> dict:
    out: dict = {}
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    out["SelectionRules"] = value["selection_rules"]
    if "overwrite_extension_pack" in value:
        out["OverwriteExtensionPack"] = value["overwrite_extension_pack"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMetadataModelExportToTargetMessage:
    out: StartMetadataModelExportToTargetMessage = {}  # type: ignore[typeddict-item]
    if data.get("MigrationProjectIdentifier") is not None:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    else:
        raise DeserializationError(
            "StartMetadataModelExportToTargetMessage.migration_project_identifier required"
        )
    if data.get("SelectionRules") is not None:
        out["selection_rules"] = data["SelectionRules"]
    else:
        raise DeserializationError(
            "StartMetadataModelExportToTargetMessage.selection_rules required"
        )
    if data.get("OverwriteExtensionPack") is not None:
        out["overwrite_extension_pack"] = data["OverwriteExtensionPack"]
    return out
