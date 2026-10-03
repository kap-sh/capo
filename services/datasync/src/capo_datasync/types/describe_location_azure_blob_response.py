"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeLocationAzureBlobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.agent_arn_list
    import capo_datasync.types.azure_access_tier
    import capo_datasync.types.azure_blob_authentication_type
    import capo_datasync.types.azure_blob_type
    import capo_datasync.types.cmk_secret_config
    import capo_datasync.types.custom_secret_config
    import capo_datasync.types.location_arn
    import capo_datasync.types.location_uri
    import capo_datasync.types.managed_secret_config
    import capo_datasync.types.time


class DescribeLocationAzureBlobResponse(TypedDict, closed=True):
    location_arn: NotRequired["capo_datasync.types.location_arn.LocationArn"]
    """<p>The ARN of your Azure Blob Storage transfer location.</p>"""
    location_uri: NotRequired["capo_datasync.types.location_uri.LocationUri"]
    """<p>The URL of the Azure Blob Storage container involved in your transfer.</p>"""
    authentication_type: NotRequired[
        "capo_datasync.types.azure_blob_authentication_type.AzureBlobAuthenticationType"
    ]
    """<p>The authentication method DataSync uses to access your Azure Blob Storage. DataSync can access blob storage using a shared access signature (SAS).</p>"""
    blob_type: NotRequired["capo_datasync.types.azure_blob_type.AzureBlobType"]
    """<p>The type of blob that you want your objects or files to be when transferring them into Azure Blob Storage. Currently, DataSync only supports moving data into Azure Blob Storage as block blobs. For more information on blob types, see the <a href="https://learn.microsoft.com/en-us/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs">Azure Blob Storage documentation</a>.</p>"""
    access_tier: NotRequired["capo_datasync.types.azure_access_tier.AzureAccessTier"]
    """<p>The access tier that you want your objects or files transferred into. This only applies when using the location as a transfer destination. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-access-tiers">Access tiers</a>.</p>"""
    agent_arns: NotRequired["capo_datasync.types.agent_arn_list.AgentArnList"]
    """<p>The ARNs of the DataSync agents that can connect with your Azure Blob Storage container.</p>"""
    creation_time: NotRequired["capo_datasync.types.time.Time"]
    """<p>The time that your Azure Blob Storage transfer location was created.</p>"""
    managed_secret_config: NotRequired[
        "capo_datasync.types.managed_secret_config.ManagedSecretConfig"
    ]
    """<p>Describes configuration information for a DataSync-managed secret, such as an authentication token that DataSync uses to access a specific storage location. DataSync uses the default Amazon Web Services-managed KMS key to encrypt this secret in Secrets Manager.</p>"""
    cmk_secret_config: NotRequired[
        "capo_datasync.types.cmk_secret_config.CmkSecretConfig"
    ]
    """<p>Describes configuration information for a DataSync-managed secret, such as an authentication token that DataSync uses to access a specific storage location, with a customer-managed KMS key.</p>"""
    custom_secret_config: NotRequired[
        "capo_datasync.types.custom_secret_config.CustomSecretConfig"
    ]
    """<p>Describes configuration information for a customer-managed secret, such as an authentication token that DataSync uses to access a specific storage location, with a customer-managed Identity and Access Management (IAM) role that provides access to the secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLocationAzureBlobResponse) -> dict:
    out: dict = {}
    if "location_arn" in value:
        out["LocationArn"] = value["location_arn"]
    if "location_uri" in value:
        out["LocationUri"] = value["location_uri"]
    if "authentication_type" in value:
        import capo_datasync.types.azure_blob_authentication_type

        out["AuthenticationType"] = (
            capo_datasync.types.azure_blob_authentication_type.serialize_aws_json_1_1(
                value["authentication_type"]
            )
        )
    if "blob_type" in value:
        import capo_datasync.types.azure_blob_type

        out["BlobType"] = capo_datasync.types.azure_blob_type.serialize_aws_json_1_1(
            value["blob_type"]
        )
    if "access_tier" in value:
        import capo_datasync.types.azure_access_tier

        out["AccessTier"] = (
            capo_datasync.types.azure_access_tier.serialize_aws_json_1_1(
                value["access_tier"]
            )
        )
    if "agent_arns" in value:
        import capo_datasync.types.agent_arn_list

        out["AgentArns"] = capo_datasync.types.agent_arn_list.serialize_aws_json_1_1(
            value["agent_arns"]
        )
    if "creation_time" in value:
        import capo_datasync.types.time

        out["CreationTime"] = capo_datasync.types.time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "managed_secret_config" in value:
        import capo_datasync.types.managed_secret_config

        out["ManagedSecretConfig"] = (
            capo_datasync.types.managed_secret_config.serialize_aws_json_1_1(
                value["managed_secret_config"]
            )
        )
    if "cmk_secret_config" in value:
        import capo_datasync.types.cmk_secret_config

        out["CmkSecretConfig"] = (
            capo_datasync.types.cmk_secret_config.serialize_aws_json_1_1(
                value["cmk_secret_config"]
            )
        )
    if "custom_secret_config" in value:
        import capo_datasync.types.custom_secret_config

        out["CustomSecretConfig"] = (
            capo_datasync.types.custom_secret_config.serialize_aws_json_1_1(
                value["custom_secret_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLocationAzureBlobResponse:
    out: DescribeLocationAzureBlobResponse = {}  # type: ignore[typeddict-item]
    if data.get("LocationArn") is not None:
        out["location_arn"] = data["LocationArn"]
    if data.get("LocationUri") is not None:
        out["location_uri"] = data["LocationUri"]
    if data.get("AuthenticationType") is not None:
        import capo_datasync.types.azure_blob_authentication_type

        out["authentication_type"] = (
            capo_datasync.types.azure_blob_authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    if data.get("BlobType") is not None:
        import capo_datasync.types.azure_blob_type

        out["blob_type"] = capo_datasync.types.azure_blob_type.deserialize_aws_json_1_1(
            data["BlobType"]
        )
    if data.get("AccessTier") is not None:
        import capo_datasync.types.azure_access_tier

        out["access_tier"] = (
            capo_datasync.types.azure_access_tier.deserialize_aws_json_1_1(
                data["AccessTier"]
            )
        )
    if data.get("AgentArns") is not None:
        import capo_datasync.types.agent_arn_list

        out["agent_arns"] = capo_datasync.types.agent_arn_list.deserialize_aws_json_1_1(
            data["AgentArns"]
        )
    if data.get("CreationTime") is not None:
        import capo_datasync.types.time

        out["creation_time"] = capo_datasync.types.time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("ManagedSecretConfig") is not None:
        import capo_datasync.types.managed_secret_config

        out["managed_secret_config"] = (
            capo_datasync.types.managed_secret_config.deserialize_aws_json_1_1(
                data["ManagedSecretConfig"]
            )
        )
    if data.get("CmkSecretConfig") is not None:
        import capo_datasync.types.cmk_secret_config

        out["cmk_secret_config"] = (
            capo_datasync.types.cmk_secret_config.deserialize_aws_json_1_1(
                data["CmkSecretConfig"]
            )
        )
    if data.get("CustomSecretConfig") is not None:
        import capo_datasync.types.custom_secret_config

        out["custom_secret_config"] = (
            capo_datasync.types.custom_secret_config.deserialize_aws_json_1_1(
                data["CustomSecretConfig"]
            )
        )
    return out
