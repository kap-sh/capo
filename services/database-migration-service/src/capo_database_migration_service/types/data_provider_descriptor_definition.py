"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DataProviderDescriptorDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class DataProviderDescriptorDefinition(TypedDict, closed=True):
    data_provider_identifier: "capo_database_migration_service.types.string.String"
    """<p>The name or Amazon Resource Name (ARN) of the data provider.</p>"""
    secrets_manager_secret_id: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The identifier of the Amazon Web Services Secrets Manager Secret used to store access credentials for the data provider.</p>"""
    secrets_manager_access_role_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The ARN of the role used to access Amazon Web Services Secrets Manager.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataProviderDescriptorDefinition) -> dict:
    out: dict = {}
    out["DataProviderIdentifier"] = value["data_provider_identifier"]
    if "secrets_manager_secret_id" in value:
        out["SecretsManagerSecretId"] = value["secrets_manager_secret_id"]
    if "secrets_manager_access_role_arn" in value:
        out["SecretsManagerAccessRoleArn"] = value["secrets_manager_access_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataProviderDescriptorDefinition:
    out: DataProviderDescriptorDefinition = {}  # type: ignore[typeddict-item]
    if data.get("DataProviderIdentifier") is not None:
        out["data_provider_identifier"] = data["DataProviderIdentifier"]
    else:
        out["data_provider_identifier"] = ""
    if data.get("SecretsManagerSecretId") is not None:
        out["secrets_manager_secret_id"] = data["SecretsManagerSecretId"]
    if data.get("SecretsManagerAccessRoleArn") is not None:
        out["secrets_manager_access_role_arn"] = data["SecretsManagerAccessRoleArn"]
    return out
