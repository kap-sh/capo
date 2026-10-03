"""Generated from Smithy shape ``com.amazonaws.kendra#DescribeIndexResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.capacity_units_configuration
    import capo_kendra.types.description
    import capo_kendra.types.document_metadata_configuration_list
    import capo_kendra.types.error_message
    import capo_kendra.types.index_edition
    import capo_kendra.types.index_id
    import capo_kendra.types.index_name
    import capo_kendra.types.index_statistics
    import capo_kendra.types.index_status
    import capo_kendra.types.role_arn
    import capo_kendra.types.server_side_encryption_configuration
    import capo_kendra.types.timestamp
    import capo_kendra.types.user_context_policy
    import capo_kendra.types.user_group_resolution_configuration
    import capo_kendra.types.user_token_configuration_list


class DescribeIndexResponse(TypedDict, closed=True):
    name: NotRequired["capo_kendra.types.index_name.IndexName"]
    """<p>The name of the index.</p>"""
    id: NotRequired["capo_kendra.types.index_id.IndexId"]
    """<p>The identifier of the index.</p>"""
    edition: NotRequired["capo_kendra.types.index_edition.IndexEdition"]
    """<p>The Amazon Kendra edition used for the index. You decide the edition when you create the index.</p>"""
    role_arn: NotRequired["capo_kendra.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that gives Amazon Kendra permission to write to your Amazon CloudWatch logs.</p>"""
    server_side_encryption_configuration: NotRequired[
        "capo_kendra.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    ]
    """<p>The identifier of the KMS customer master key (CMK) that is used to encrypt your data. Amazon Kendra doesn't support asymmetric CMKs.</p>"""
    status: NotRequired["capo_kendra.types.index_status.IndexStatus"]
    """<p>The current status of the index. When the value is <code>ACTIVE</code>, the index is ready for use. If the <code>Status</code> field value is <code>FAILED</code>, the <code>ErrorMessage</code> field contains a message that explains why.</p>"""
    description: NotRequired["capo_kendra.types.description.Description"]
    """<p>The description for the index.</p>"""
    created_at: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the index was created.</p>"""
    updated_at: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the index was last updated.</p>"""
    document_metadata_configurations: NotRequired[
        "capo_kendra.types.document_metadata_configuration_list.DocumentMetadataConfigurationList"
    ]
    """<p>Configuration information for document metadata or fields. Document metadata are fields or attributes associated with your documents. For example, the company department name associated with each document.</p>"""
    index_statistics: NotRequired["capo_kendra.types.index_statistics.IndexStatistics"]
    """<p>Provides information about the number of FAQ questions and answers and the number of text documents indexed.</p>"""
    error_message: NotRequired["capo_kendra.types.error_message.ErrorMessage"]
    """<p>When the <code>Status</code> field value is <code>FAILED</code>, the <code>ErrorMessage</code> field contains a message that explains why.</p>"""
    capacity_units: NotRequired[
        "capo_kendra.types.capacity_units_configuration.CapacityUnitsConfiguration"
    ]
    """<p>For Enterprise Edition indexes, you can choose to use additional capacity to meet the needs of your application. This contains the capacity units used for the index. A query or document storage capacity of zero indicates that the index is using the default capacity. For more information on the default capacity for an index and adjusting this, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/adjusting-capacity.html">Adjusting capacity</a>.</p>"""
    user_token_configurations: NotRequired[
        "capo_kendra.types.user_token_configuration_list.UserTokenConfigurationList"
    ]
    """<p>The user token configuration for the Amazon Kendra index.</p>"""
    user_context_policy: NotRequired[
        "capo_kendra.types.user_context_policy.UserContextPolicy"
    ]
    """<p>The user context policy for the Amazon Kendra index.</p>"""
    user_group_resolution_configuration: NotRequired[
        "capo_kendra.types.user_group_resolution_configuration.UserGroupResolutionConfiguration"
    ]
    """<p>Whether you have enabled IAM Identity Center identity source for your users and groups. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeIndexResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "edition" in value:
        import capo_kendra.types.index_edition

        out["Edition"] = capo_kendra.types.index_edition.serialize_aws_json_1_1(
            value["edition"]
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "server_side_encryption_configuration" in value:
        import capo_kendra.types.server_side_encryption_configuration

        out["ServerSideEncryptionConfiguration"] = (
            capo_kendra.types.server_side_encryption_configuration.serialize_aws_json_1_1(
                value["server_side_encryption_configuration"]
            )
        )
    if "status" in value:
        import capo_kendra.types.index_status

        out["Status"] = capo_kendra.types.index_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "created_at" in value:
        import capo_kendra.types.timestamp

        out["CreatedAt"] = capo_kendra.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_kendra.types.timestamp

        out["UpdatedAt"] = capo_kendra.types.timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    if "document_metadata_configurations" in value:
        import capo_kendra.types.document_metadata_configuration_list

        out["DocumentMetadataConfigurations"] = (
            capo_kendra.types.document_metadata_configuration_list.serialize_aws_json_1_1(
                value["document_metadata_configurations"]
            )
        )
    if "index_statistics" in value:
        import capo_kendra.types.index_statistics

        out["IndexStatistics"] = (
            capo_kendra.types.index_statistics.serialize_aws_json_1_1(
                value["index_statistics"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "capacity_units" in value:
        import capo_kendra.types.capacity_units_configuration

        out["CapacityUnits"] = (
            capo_kendra.types.capacity_units_configuration.serialize_aws_json_1_1(
                value["capacity_units"]
            )
        )
    if "user_token_configurations" in value:
        import capo_kendra.types.user_token_configuration_list

        out["UserTokenConfigurations"] = (
            capo_kendra.types.user_token_configuration_list.serialize_aws_json_1_1(
                value["user_token_configurations"]
            )
        )
    if "user_context_policy" in value:
        import capo_kendra.types.user_context_policy

        out["UserContextPolicy"] = (
            capo_kendra.types.user_context_policy.serialize_aws_json_1_1(
                value["user_context_policy"]
            )
        )
    if "user_group_resolution_configuration" in value:
        import capo_kendra.types.user_group_resolution_configuration

        out["UserGroupResolutionConfiguration"] = (
            capo_kendra.types.user_group_resolution_configuration.serialize_aws_json_1_1(
                value["user_group_resolution_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeIndexResponse:
    out: DescribeIndexResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Edition") is not None:
        import capo_kendra.types.index_edition

        out["edition"] = capo_kendra.types.index_edition.deserialize_aws_json_1_1(
            data["Edition"]
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("ServerSideEncryptionConfiguration") is not None:
        import capo_kendra.types.server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            capo_kendra.types.server_side_encryption_configuration.deserialize_aws_json_1_1(
                data["ServerSideEncryptionConfiguration"]
            )
        )
    if data.get("Status") is not None:
        import capo_kendra.types.index_status

        out["status"] = capo_kendra.types.index_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreatedAt") is not None:
        import capo_kendra.types.timestamp

        out["created_at"] = capo_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_kendra.types.timestamp

        out["updated_at"] = capo_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    if data.get("DocumentMetadataConfigurations") is not None:
        import capo_kendra.types.document_metadata_configuration_list

        out["document_metadata_configurations"] = (
            capo_kendra.types.document_metadata_configuration_list.deserialize_aws_json_1_1(
                data["DocumentMetadataConfigurations"]
            )
        )
    if data.get("IndexStatistics") is not None:
        import capo_kendra.types.index_statistics

        out["index_statistics"] = (
            capo_kendra.types.index_statistics.deserialize_aws_json_1_1(
                data["IndexStatistics"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("CapacityUnits") is not None:
        import capo_kendra.types.capacity_units_configuration

        out["capacity_units"] = (
            capo_kendra.types.capacity_units_configuration.deserialize_aws_json_1_1(
                data["CapacityUnits"]
            )
        )
    if data.get("UserTokenConfigurations") is not None:
        import capo_kendra.types.user_token_configuration_list

        out["user_token_configurations"] = (
            capo_kendra.types.user_token_configuration_list.deserialize_aws_json_1_1(
                data["UserTokenConfigurations"]
            )
        )
    if data.get("UserContextPolicy") is not None:
        import capo_kendra.types.user_context_policy

        out["user_context_policy"] = (
            capo_kendra.types.user_context_policy.deserialize_aws_json_1_1(
                data["UserContextPolicy"]
            )
        )
    if data.get("UserGroupResolutionConfiguration") is not None:
        import capo_kendra.types.user_group_resolution_configuration

        out["user_group_resolution_configuration"] = (
            capo_kendra.types.user_group_resolution_configuration.deserialize_aws_json_1_1(
                data["UserGroupResolutionConfiguration"]
            )
        )
    return out
