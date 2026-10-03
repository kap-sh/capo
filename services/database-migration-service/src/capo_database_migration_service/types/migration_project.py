"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#MigrationProject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.data_provider_descriptor_list
    import capo_database_migration_service.types.iso8601_date_time
    import capo_database_migration_service.types.sc_application_attributes
    import capo_database_migration_service.types.string


class MigrationProject(TypedDict, closed=True):
    migration_project_name: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The name of the migration project.</p>"""
    migration_project_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The ARN string that uniquely identifies the migration project.</p>"""
    migration_project_creation_time: NotRequired[
        "capo_database_migration_service.types.iso8601_date_time.Iso8601DateTime"
    ]
    """<p>The time when the migration project was created.</p>"""
    source_data_provider_descriptors: NotRequired[
        "capo_database_migration_service.types.data_provider_descriptor_list.DataProviderDescriptorList"
    ]
    """<p>Information about the source data provider, including the name or ARN, and Secrets Manager parameters.</p>"""
    target_data_provider_descriptors: NotRequired[
        "capo_database_migration_service.types.data_provider_descriptor_list.DataProviderDescriptorList"
    ]
    """<p>Information about the target data provider, including the name or ARN, and Secrets Manager parameters.</p>"""
    instance_profile_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the instance profile for your migration project.</p>"""
    instance_profile_name: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The name of the associated instance profile.</p>"""
    transformation_rules: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The transformation rules for the migration project in JSON format. Transformation rules let you customize how DMS Schema Conversion converts your source database objects, including renaming, adding prefixes or suffixes, and changing data types. For the transformation rule format and examples, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/sc-transformation-rules.html">Transformation rules in DMS Schema Conversion</a>.</p> <note> <p>Homogeneous data migrations do not support transformation rules.</p> </note>"""
    description: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>A user-friendly description of the migration project.</p>"""
    schema_conversion_application_attributes: NotRequired[
        "capo_database_migration_service.types.sc_application_attributes.SCApplicationAttributes"
    ]
    """<p>The schema conversion application attributes, including the Amazon S3 bucket name and Amazon S3 role ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MigrationProject) -> dict:
    out: dict = {}
    if "migration_project_name" in value:
        out["MigrationProjectName"] = value["migration_project_name"]
    if "migration_project_arn" in value:
        out["MigrationProjectArn"] = value["migration_project_arn"]
    if "migration_project_creation_time" in value:
        import capo_database_migration_service.types.iso8601_date_time

        out["MigrationProjectCreationTime"] = (
            capo_database_migration_service.types.iso8601_date_time.serialize_aws_json_1_1(
                value["migration_project_creation_time"]
            )
        )
    if "source_data_provider_descriptors" in value:
        import capo_database_migration_service.types.data_provider_descriptor_list

        out["SourceDataProviderDescriptors"] = (
            capo_database_migration_service.types.data_provider_descriptor_list.serialize_aws_json_1_1(
                value["source_data_provider_descriptors"]
            )
        )
    if "target_data_provider_descriptors" in value:
        import capo_database_migration_service.types.data_provider_descriptor_list

        out["TargetDataProviderDescriptors"] = (
            capo_database_migration_service.types.data_provider_descriptor_list.serialize_aws_json_1_1(
                value["target_data_provider_descriptors"]
            )
        )
    if "instance_profile_arn" in value:
        out["InstanceProfileArn"] = value["instance_profile_arn"]
    if "instance_profile_name" in value:
        out["InstanceProfileName"] = value["instance_profile_name"]
    if "transformation_rules" in value:
        out["TransformationRules"] = value["transformation_rules"]
    if "description" in value:
        out["Description"] = value["description"]
    if "schema_conversion_application_attributes" in value:
        import capo_database_migration_service.types.sc_application_attributes

        out["SchemaConversionApplicationAttributes"] = (
            capo_database_migration_service.types.sc_application_attributes.serialize_aws_json_1_1(
                value["schema_conversion_application_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MigrationProject:
    out: MigrationProject = {}  # type: ignore[typeddict-item]
    if data.get("MigrationProjectName") is not None:
        out["migration_project_name"] = data["MigrationProjectName"]
    if data.get("MigrationProjectArn") is not None:
        out["migration_project_arn"] = data["MigrationProjectArn"]
    if data.get("MigrationProjectCreationTime") is not None:
        import capo_database_migration_service.types.iso8601_date_time

        out["migration_project_creation_time"] = (
            capo_database_migration_service.types.iso8601_date_time.deserialize_aws_json_1_1(
                data["MigrationProjectCreationTime"]
            )
        )
    if data.get("SourceDataProviderDescriptors") is not None:
        import capo_database_migration_service.types.data_provider_descriptor_list

        out["source_data_provider_descriptors"] = (
            capo_database_migration_service.types.data_provider_descriptor_list.deserialize_aws_json_1_1(
                data["SourceDataProviderDescriptors"]
            )
        )
    if data.get("TargetDataProviderDescriptors") is not None:
        import capo_database_migration_service.types.data_provider_descriptor_list

        out["target_data_provider_descriptors"] = (
            capo_database_migration_service.types.data_provider_descriptor_list.deserialize_aws_json_1_1(
                data["TargetDataProviderDescriptors"]
            )
        )
    if data.get("InstanceProfileArn") is not None:
        out["instance_profile_arn"] = data["InstanceProfileArn"]
    if data.get("InstanceProfileName") is not None:
        out["instance_profile_name"] = data["InstanceProfileName"]
    if data.get("TransformationRules") is not None:
        out["transformation_rules"] = data["TransformationRules"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("SchemaConversionApplicationAttributes") is not None:
        import capo_database_migration_service.types.sc_application_attributes

        out["schema_conversion_application_attributes"] = (
            capo_database_migration_service.types.sc_application_attributes.deserialize_aws_json_1_1(
                data["SchemaConversionApplicationAttributes"]
            )
        )
    return out
