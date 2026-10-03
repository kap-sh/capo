"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateLocationAzureBlobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.agent_arn_list
    import capo_datasync.types.azure_access_tier
    import capo_datasync.types.azure_blob_authentication_type
    import capo_datasync.types.azure_blob_sas_configuration
    import capo_datasync.types.azure_blob_subdirectory
    import capo_datasync.types.azure_blob_type
    import capo_datasync.types.cmk_secret_config
    import capo_datasync.types.custom_secret_config
    import capo_datasync.types.location_arn


class UpdateLocationAzureBlobRequest(TypedDict, closed=True):
    location_arn: "capo_datasync.types.location_arn.LocationArn"
    """<p>Specifies the ARN of the Azure Blob Storage transfer location that you're updating.</p>"""
    subdirectory: NotRequired[
        "capo_datasync.types.azure_blob_subdirectory.AzureBlobSubdirectory"
    ]
    """<p>Specifies path segments if you want to limit your transfer to a virtual directory in your container (for example, <code>/my/images</code>).</p>"""
    authentication_type: NotRequired[
        "capo_datasync.types.azure_blob_authentication_type.AzureBlobAuthenticationType"
    ]
    """<p>Specifies the authentication method DataSync uses to access your Azure Blob Storage. DataSync can access blob storage using a shared access signature (SAS).</p>"""
    sas_configuration: NotRequired[
        "capo_datasync.types.azure_blob_sas_configuration.AzureBlobSasConfiguration"
    ]
    """<p>Specifies the SAS configuration that allows DataSync to access your Azure Blob Storage.</p>"""
    blob_type: NotRequired["capo_datasync.types.azure_blob_type.AzureBlobType"]
    """<p>Specifies the type of blob that you want your objects or files to be when transferring them into Azure Blob Storage. Currently, DataSync only supports moving data into Azure Blob Storage as block blobs. For more information on blob types, see the <a href="https://learn.microsoft.com/en-us/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs">Azure Blob Storage documentation</a>.</p>"""
    access_tier: NotRequired["capo_datasync.types.azure_access_tier.AzureAccessTier"]
    """<p>Specifies the access tier that you want your objects or files transferred into. This only applies when using the location as a transfer destination. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-access-tiers">Access tiers</a>.</p>"""
    agent_arns: NotRequired["capo_datasync.types.agent_arn_list.AgentArnList"]
    """<p>(Optional) Specifies the Amazon Resource Name (ARN) of the DataSync agent that can connect with your Azure Blob Storage container. If you are setting up an agentless cross-cloud transfer, you do not need to specify a value for this parameter.</p> <p>You can specify more than one agent. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/multiple-agents.html">Using multiple agents for your transfer</a>.</p> <note> <p>You cannot add or remove agents from a storage location after you initially create it.</p> </note>"""
    cmk_secret_config: NotRequired[
        "capo_datasync.types.cmk_secret_config.CmkSecretConfig"
    ]
    """<p>Specifies configuration information for a DataSync-managed secret, such as an authentication token or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed KMS key.</p>"""
    custom_secret_config: NotRequired[
        "capo_datasync.types.custom_secret_config.CustomSecretConfig"
    ]
    """<p>Specifies configuration information for a customer-managed secret, such as an authentication token or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed Identity and Access Management (IAM) role that provides access to the secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLocationAzureBlobRequest) -> dict:
    out: dict = {}
    out["LocationArn"] = value["location_arn"]
    if "subdirectory" in value:
        out["Subdirectory"] = value["subdirectory"]
    if "authentication_type" in value:
        import capo_datasync.types.azure_blob_authentication_type

        out["AuthenticationType"] = (
            capo_datasync.types.azure_blob_authentication_type.serialize_aws_json_1_1(
                value["authentication_type"]
            )
        )
    if "sas_configuration" in value:
        import capo_datasync.types.azure_blob_sas_configuration

        out["SasConfiguration"] = (
            capo_datasync.types.azure_blob_sas_configuration.serialize_aws_json_1_1(
                value["sas_configuration"]
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


def deserialize_aws_json_1_1(data: dict) -> UpdateLocationAzureBlobRequest:
    out: UpdateLocationAzureBlobRequest = {}  # type: ignore[typeddict-item]
    if data.get("LocationArn") is not None:
        out["location_arn"] = data["LocationArn"]
    else:
        raise DeserializationError(
            "UpdateLocationAzureBlobRequest.location_arn required"
        )
    if data.get("Subdirectory") is not None:
        out["subdirectory"] = data["Subdirectory"]
    if data.get("AuthenticationType") is not None:
        import capo_datasync.types.azure_blob_authentication_type

        out["authentication_type"] = (
            capo_datasync.types.azure_blob_authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    if data.get("SasConfiguration") is not None:
        import capo_datasync.types.azure_blob_sas_configuration

        out["sas_configuration"] = (
            capo_datasync.types.azure_blob_sas_configuration.deserialize_aws_json_1_1(
                data["SasConfiguration"]
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
