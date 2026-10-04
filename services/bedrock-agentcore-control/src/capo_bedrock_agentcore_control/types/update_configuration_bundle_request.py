"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateConfigurationBundleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.branch_name
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.component_configuration_map
    import capo_bedrock_agentcore_control.types.configuration_bundle_description
    import capo_bedrock_agentcore_control.types.configuration_bundle_id
    import capo_bedrock_agentcore_control.types.configuration_bundle_name
    import capo_bedrock_agentcore_control.types.configuration_bundle_version_list
    import capo_bedrock_agentcore_control.types.kms_key_arn
    import capo_bedrock_agentcore_control.types.version_created_by_source


class UpdateConfigurationBundleRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    bundle_id: "capo_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId"
    """<p>The unique identifier of the configuration bundle to update.</p>"""
    bundle_name: NotRequired[
        "capo_bedrock_agentcore_control.types.configuration_bundle_name.ConfigurationBundleName"
    ]
    """<p>The updated name for the configuration bundle.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.configuration_bundle_description.ConfigurationBundleDescription"
    ]
    """<p>The updated description for the configuration bundle.</p>"""
    components: NotRequired[
        "capo_bedrock_agentcore_control.types.component_configuration_map.ComponentConfigurationMap"
    ]
    """<p>The updated component configurations. Creates a new version of the bundle.</p>"""
    parent_version_ids: "capo_bedrock_agentcore_control.types.configuration_bundle_version_list.ConfigurationBundleVersionList"
    """<p>A list of parent version identifiers for lineage tracking. Regular commits have a single parent. Merge commits have two parents: the target branch parent and the source branch parent. If the branch already exists, the first parent must be the latest version on that branch.</p>"""
    branch_name: NotRequired[
        "capo_bedrock_agentcore_control.types.branch_name.BranchName"
    ]
    """<p>The branch name for this version. If not specified, inherits the parent's branch or defaults to <code>mainline</code>.</p>"""
    commit_message: "str"
    """<p>A commit message describing the changes in this version.</p>"""
    created_by: NotRequired[
        "capo_bedrock_agentcore_control.types.version_created_by_source.VersionCreatedBySource"
    ]
    """<p>The source that created this version, including the source name and optional ARN.</p>"""
    kms_key_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>Optional KMS key ARN for encrypting component configurations. If provided, components will be encrypted with this key. If the bundle already has a KMS key, this rotates to the new key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfigurationBundleRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "bundle_name" in value:
        out["bundleName"] = value["bundle_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "components" in value:
        import capo_bedrock_agentcore_control.types.component_configuration_map

        out["components"] = (
            capo_bedrock_agentcore_control.types.component_configuration_map.serialize_json(
                value["components"]
            )
        )
    import capo_bedrock_agentcore_control.types.configuration_bundle_version_list

    out["parentVersionIds"] = (
        capo_bedrock_agentcore_control.types.configuration_bundle_version_list.serialize_json(
            value["parent_version_ids"]
        )
    )
    if "branch_name" in value:
        out["branchName"] = value["branch_name"]
    out["commitMessage"] = value["commit_message"]
    if "created_by" in value:
        import capo_bedrock_agentcore_control.types.version_created_by_source

        out["createdBy"] = (
            capo_bedrock_agentcore_control.types.version_created_by_source.serialize_json(
                value["created_by"]
            )
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> UpdateConfigurationBundleRequest:
    out: UpdateConfigurationBundleRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("bundleName") is not None:
        out["bundle_name"] = data["bundleName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("components") is not None:
        import capo_bedrock_agentcore_control.types.component_configuration_map

        out["components"] = (
            capo_bedrock_agentcore_control.types.component_configuration_map.deserialize_json(
                data["components"]
            )
        )
    if data.get("parentVersionIds") is not None:
        import capo_bedrock_agentcore_control.types.configuration_bundle_version_list

        out["parent_version_ids"] = (
            capo_bedrock_agentcore_control.types.configuration_bundle_version_list.deserialize_json(
                data["parentVersionIds"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateConfigurationBundleRequest.parent_version_ids required"
        )
    if data.get("branchName") is not None:
        out["branch_name"] = data["branchName"]
    if data.get("commitMessage") is not None:
        out["commit_message"] = data["commitMessage"]
    else:
        raise DeserializationError(
            "UpdateConfigurationBundleRequest.commit_message required"
        )
    if data.get("createdBy") is not None:
        import capo_bedrock_agentcore_control.types.version_created_by_source

        out["created_by"] = (
            capo_bedrock_agentcore_control.types.version_created_by_source.deserialize_json(
                data["createdBy"]
            )
        )
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
