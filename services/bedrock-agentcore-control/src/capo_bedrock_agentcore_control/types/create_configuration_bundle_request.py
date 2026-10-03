"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateConfigurationBundleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.branch_name
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.component_configuration_map
    import capo_bedrock_agentcore_control.types.configuration_bundle_description
    import capo_bedrock_agentcore_control.types.configuration_bundle_name
    import capo_bedrock_agentcore_control.types.kms_key_arn
    import capo_bedrock_agentcore_control.types.tags_map
    import capo_bedrock_agentcore_control.types.version_created_by_source


class CreateConfigurationBundleRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    bundle_name: "capo_bedrock_agentcore_control.types.configuration_bundle_name.ConfigurationBundleName"
    """<p>The name for the configuration bundle. Names must be unique within your account.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.configuration_bundle_description.ConfigurationBundleDescription"
    ]
    """<p>The description for the configuration bundle.</p>"""
    components: "capo_bedrock_agentcore_control.types.component_configuration_map.ComponentConfigurationMap"
    """<p>A map of component identifiers to their configurations. Each component represents a configurable element within the bundle.</p>"""
    branch_name: NotRequired[
        "capo_bedrock_agentcore_control.types.branch_name.BranchName"
    ]
    """<p>The branch name for version tracking. Defaults to <code>mainline</code> if not specified.</p>"""
    commit_message: NotRequired["str"]
    """<p>A commit message describing the initial version of the configuration bundle.</p>"""
    created_by: NotRequired[
        "capo_bedrock_agentcore_control.types.version_created_by_source.VersionCreatedBySource"
    ]
    """<p>The source that created this version, including the source name and optional ARN.</p>"""
    kms_key_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>Optional KMS key ARN for encrypting component configurations.</p>"""
    tags: NotRequired["capo_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>A map of tag keys and values to assign to the configuration bundle. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfigurationBundleRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["bundleName"] = value["bundle_name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore_control.types.component_configuration_map

    out["components"] = (
        capo_bedrock_agentcore_control.types.component_configuration_map.serialize_json(
            value["components"]
        )
    )
    if "branch_name" in value:
        out["branchName"] = value["branch_name"]
    if "commit_message" in value:
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
    if "tags" in value:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateConfigurationBundleRequest:
    out: CreateConfigurationBundleRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("bundleName") is not None:
        out["bundle_name"] = data["bundleName"]
    else:
        raise DeserializationError(
            "CreateConfigurationBundleRequest.bundle_name required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("components") is not None:
        import capo_bedrock_agentcore_control.types.component_configuration_map

        out["components"] = (
            capo_bedrock_agentcore_control.types.component_configuration_map.deserialize_json(
                data["components"]
            )
        )
    else:
        raise DeserializationError(
            "CreateConfigurationBundleRequest.components required"
        )
    if data.get("branchName") is not None:
        out["branch_name"] = data["branchName"]
    if data.get("commitMessage") is not None:
        out["commit_message"] = data["commitMessage"]
    if data.get("createdBy") is not None:
        import capo_bedrock_agentcore_control.types.version_created_by_source

        out["created_by"] = (
            capo_bedrock_agentcore_control.types.version_created_by_source.deserialize_json(
                data["createdBy"]
            )
        )
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("tags") is not None:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
