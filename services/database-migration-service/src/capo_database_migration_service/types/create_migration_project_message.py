"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CreateMigrationProjectMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.data_provider_descriptor_definition_list
    import capo_database_migration_service.types.sc_application_attributes
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.tag_list


class CreateMigrationProjectMessage(TypedDict, closed=True):
    migration_project_name: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>A user-friendly name for the migration project.</p>"""
    source_data_provider_descriptors: "capo_database_migration_service.types.data_provider_descriptor_definition_list.DataProviderDescriptorDefinitionList"
    """<p>Information about the source data provider, including the name, ARN, and Secrets Manager parameters.</p>"""
    target_data_provider_descriptors: "capo_database_migration_service.types.data_provider_descriptor_definition_list.DataProviderDescriptorDefinitionList"
    """<p>Information about the target data provider, including the name, ARN, and Amazon Web Services Secrets Manager parameters.</p>"""
    instance_profile_identifier: "capo_database_migration_service.types.string.String"
    """<p>The identifier of the associated instance profile. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.</p>"""
    transformation_rules: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>A JSON string that specifies the transformation rules for the migration project. Transformation rules let you customize how DMS Schema Conversion converts your source database objects, including renaming, adding prefixes or suffixes, and changing data types. For the transformation rule format and examples, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/sc-transformation-rules.html">Transformation rules in DMS Schema Conversion</a>.</p> <note> <p>Homogeneous data migrations do not support transformation rules.</p> </note>"""
    description: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>A user-friendly description of the migration project.</p>"""
    tags: NotRequired["capo_database_migration_service.types.tag_list.TagList"]
    """<p>One or more tags to be assigned to the migration project.</p>"""
    schema_conversion_application_attributes: NotRequired[
        "capo_database_migration_service.types.sc_application_attributes.SCApplicationAttributes"
    ]
    """<p>The schema conversion application attributes, including the Amazon S3 bucket name and Amazon S3 role ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMigrationProjectMessage) -> dict:
    out: dict = {}
    if "migration_project_name" in value:
        out["MigrationProjectName"] = value["migration_project_name"]
    import capo_database_migration_service.types.data_provider_descriptor_definition_list

    out["SourceDataProviderDescriptors"] = (
        capo_database_migration_service.types.data_provider_descriptor_definition_list.serialize_aws_json_1_1(
            value["source_data_provider_descriptors"]
        )
    )
    import capo_database_migration_service.types.data_provider_descriptor_definition_list

    out["TargetDataProviderDescriptors"] = (
        capo_database_migration_service.types.data_provider_descriptor_definition_list.serialize_aws_json_1_1(
            value["target_data_provider_descriptors"]
        )
    )
    out["InstanceProfileIdentifier"] = value["instance_profile_identifier"]
    if "transformation_rules" in value:
        out["TransformationRules"] = value["transformation_rules"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_database_migration_service.types.tag_list

        out["Tags"] = (
            capo_database_migration_service.types.tag_list.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    if "schema_conversion_application_attributes" in value:
        import capo_database_migration_service.types.sc_application_attributes

        out["SchemaConversionApplicationAttributes"] = (
            capo_database_migration_service.types.sc_application_attributes.serialize_aws_json_1_1(
                value["schema_conversion_application_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMigrationProjectMessage:
    out: CreateMigrationProjectMessage = {}  # type: ignore[typeddict-item]
    if data.get("MigrationProjectName") is not None:
        out["migration_project_name"] = data["MigrationProjectName"]
    if data.get("SourceDataProviderDescriptors") is not None:
        import capo_database_migration_service.types.data_provider_descriptor_definition_list

        out["source_data_provider_descriptors"] = (
            capo_database_migration_service.types.data_provider_descriptor_definition_list.deserialize_aws_json_1_1(
                data["SourceDataProviderDescriptors"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMigrationProjectMessage.source_data_provider_descriptors required"
        )
    if data.get("TargetDataProviderDescriptors") is not None:
        import capo_database_migration_service.types.data_provider_descriptor_definition_list

        out["target_data_provider_descriptors"] = (
            capo_database_migration_service.types.data_provider_descriptor_definition_list.deserialize_aws_json_1_1(
                data["TargetDataProviderDescriptors"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMigrationProjectMessage.target_data_provider_descriptors required"
        )
    if data.get("InstanceProfileIdentifier") is not None:
        out["instance_profile_identifier"] = data["InstanceProfileIdentifier"]
    else:
        raise DeserializationError(
            "CreateMigrationProjectMessage.instance_profile_identifier required"
        )
    if data.get("TransformationRules") is not None:
        out["transformation_rules"] = data["TransformationRules"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_database_migration_service.types.tag_list

        out["tags"] = (
            capo_database_migration_service.types.tag_list.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    if data.get("SchemaConversionApplicationAttributes") is not None:
        import capo_database_migration_service.types.sc_application_attributes

        out["schema_conversion_application_attributes"] = (
            capo_database_migration_service.types.sc_application_attributes.deserialize_aws_json_1_1(
                data["SchemaConversionApplicationAttributes"]
            )
        )
    return out
