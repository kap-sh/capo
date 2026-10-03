"""Generated from Smithy shape ``com.amazonaws.kendra#UpdateIndexRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.capacity_units_configuration
    import capo_kendra.types.description
    import capo_kendra.types.document_metadata_configuration_list
    import capo_kendra.types.index_id
    import capo_kendra.types.index_name
    import capo_kendra.types.role_arn
    import capo_kendra.types.user_context_policy
    import capo_kendra.types.user_group_resolution_configuration
    import capo_kendra.types.user_token_configuration_list


class UpdateIndexRequest(TypedDict, closed=True):
    id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index you want to update.</p>"""
    name: NotRequired["capo_kendra.types.index_name.IndexName"]
    """<p>A new name for the index.</p>"""
    role_arn: NotRequired["capo_kendra.types.role_arn.RoleArn"]
    """<p>An Identity and Access Management (IAM) role that gives Amazon Kendra permission to access Amazon CloudWatch logs and metrics.</p>"""
    description: NotRequired["capo_kendra.types.description.Description"]
    """<p>A new description for the index.</p>"""
    document_metadata_configuration_updates: NotRequired[
        "capo_kendra.types.document_metadata_configuration_list.DocumentMetadataConfigurationList"
    ]
    """<p>The document metadata configuration you want to update for the index. Document metadata are fields or attributes associated with your documents. For example, the company department name associated with each document.</p>"""
    capacity_units: NotRequired[
        "capo_kendra.types.capacity_units_configuration.CapacityUnitsConfiguration"
    ]
    """<p>Sets the number of additional document storage and query capacity units that should be used by the index. You can change the capacity of the index up to 5 times per day, or make 5 API calls.</p> <p>If you are using extra storage units, you can't reduce the storage capacity below what is required to meet the storage needs for your index.</p>"""
    user_token_configurations: NotRequired[
        "capo_kendra.types.user_token_configuration_list.UserTokenConfigurationList"
    ]
    """<p>The user token configuration.</p> <important> <p>If you're using an Amazon Kendra Gen AI Enterprise Edition index and you try to use <code>UserTokenConfigurations</code> to configure user context policy, Amazon Kendra returns a <code>ValidationException</code> error.</p> </important>"""
    user_context_policy: NotRequired[
        "capo_kendra.types.user_context_policy.UserContextPolicy"
    ]
    """<p>The user context policy.</p> <important> <p>If you're using an Amazon Kendra Gen AI Enterprise Edition index, you can only use <code>ATTRIBUTE_FILTER</code> to filter search results by user context. If you're using an Amazon Kendra Gen AI Enterprise Edition index and you try to use <code>USER_TOKEN</code> to configure user context policy, Amazon Kendra returns a <code>ValidationException</code> error.</p> </important>"""
    user_group_resolution_configuration: NotRequired[
        "capo_kendra.types.user_group_resolution_configuration.UserGroupResolutionConfiguration"
    ]
    """<p>Gets users and groups from IAM Identity Center identity source. To configure this, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_UserGroupResolutionConfiguration.html">UserGroupResolutionConfiguration</a>. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.</p> <important> <p>If you're using an Amazon Kendra Gen AI Enterprise Edition index, <code>UserGroupResolutionConfiguration</code> isn't supported.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateIndexRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "document_metadata_configuration_updates" in value:
        import capo_kendra.types.document_metadata_configuration_list

        out["DocumentMetadataConfigurationUpdates"] = (
            capo_kendra.types.document_metadata_configuration_list.serialize_aws_json_1_1(
                value["document_metadata_configuration_updates"]
            )
        )
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


def deserialize_aws_json_1_1(data: dict) -> UpdateIndexRequest:
    out: UpdateIndexRequest = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("UpdateIndexRequest.id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DocumentMetadataConfigurationUpdates") is not None:
        import capo_kendra.types.document_metadata_configuration_list

        out["document_metadata_configuration_updates"] = (
            capo_kendra.types.document_metadata_configuration_list.deserialize_aws_json_1_1(
                data["DocumentMetadataConfigurationUpdates"]
            )
        )
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
