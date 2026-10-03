"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartMetadataModelCreationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.metadata_model_properties
    import capo_database_migration_service.types.migration_project_identifier
    import capo_database_migration_service.types.string


class StartMetadataModelCreationMessage(TypedDict, closed=True):
    migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier"
    """<p>The migration project name or Amazon Resource Name (ARN).</p>"""
    selection_rules: "capo_database_migration_service.types.string.String"
    """<p>A JSON string that identifies the source schema for the metadata model. For the selection rule format and examples, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html">Selection rules in DMS Schema Conversion</a>.</p> <p>Usage:</p> <ul> <li> <p>Accepts only source selection rules, where <code>server-name</code> in the object locator matches the source data provider.</p> </li> <li> <p>Supports only <code>explicit</code> rule actions.</p> </li> <li> <p>Exactly one rule is allowed.</p> </li> </ul>"""
    metadata_model_name: "capo_database_migration_service.types.string.String"
    """<p>The name for the metadata model to use in subsequent operations.</p>"""
    properties: "capo_database_migration_service.types.metadata_model_properties.MetadataModelProperties"
    """<p>The properties of the metadata model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMetadataModelCreationMessage) -> dict:
    out: dict = {}
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    out["SelectionRules"] = value["selection_rules"]
    out["MetadataModelName"] = value["metadata_model_name"]
    import capo_database_migration_service.types.metadata_model_properties

    out["Properties"] = (
        capo_database_migration_service.types.metadata_model_properties.serialize_aws_json_1_1(
            value["properties"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMetadataModelCreationMessage:
    out: StartMetadataModelCreationMessage = {}  # type: ignore[typeddict-item]
    if data.get("MigrationProjectIdentifier") is not None:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    else:
        raise DeserializationError(
            "StartMetadataModelCreationMessage.migration_project_identifier required"
        )
    if data.get("SelectionRules") is not None:
        out["selection_rules"] = data["SelectionRules"]
    else:
        raise DeserializationError(
            "StartMetadataModelCreationMessage.selection_rules required"
        )
    if data.get("MetadataModelName") is not None:
        out["metadata_model_name"] = data["MetadataModelName"]
    else:
        raise DeserializationError(
            "StartMetadataModelCreationMessage.metadata_model_name required"
        )
    if data.get("Properties") is not None:
        import capo_database_migration_service.types.metadata_model_properties

        out["properties"] = (
            capo_database_migration_service.types.metadata_model_properties.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    else:
        raise DeserializationError(
            "StartMetadataModelCreationMessage.properties required"
        )
    return out
