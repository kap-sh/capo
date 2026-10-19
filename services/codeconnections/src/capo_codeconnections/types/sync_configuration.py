"""Generated from Smithy shape ``com.amazonaws.codeconnections#SyncConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.branch_name
    import capo_codeconnections.types.deployment_file_path
    import capo_codeconnections.types.iam_role_arn
    import capo_codeconnections.types.owner_id
    import capo_codeconnections.types.provider_type
    import capo_codeconnections.types.publish_deployment_status
    import capo_codeconnections.types.pull_request_comment
    import capo_codeconnections.types.repository_link_id
    import capo_codeconnections.types.repository_name
    import capo_codeconnections.types.resource_name
    import capo_codeconnections.types.sync_configuration_type
    import capo_codeconnections.types.trigger_resource_update_on


class SyncConfiguration(TypedDict, closed=True):
    branch: "capo_codeconnections.types.branch_name.BranchName"
    """<p>The branch associated with a specific sync configuration.</p>"""
    config_file: NotRequired[
        "capo_codeconnections.types.deployment_file_path.DeploymentFilePath"
    ]
    """<p>The file path to the configuration file associated with a specific sync configuration. The path should point to an actual file in the sync configurations linked repository.</p>"""
    owner_id: "capo_codeconnections.types.owner_id.OwnerId"
    """<p>The owner ID for the repository associated with a specific sync configuration, such as the owner ID in GitHub.</p>"""
    provider_type: "capo_codeconnections.types.provider_type.ProviderType"
    """<p>The connection provider type associated with a specific sync configuration, such as GitHub.</p>"""
    repository_link_id: "capo_codeconnections.types.repository_link_id.RepositoryLinkId"
    """<p>The ID of the repository link associated with a specific sync configuration.</p>"""
    repository_name: "capo_codeconnections.types.repository_name.RepositoryName"
    """<p>The name of the repository associated with a specific sync configuration.</p>"""
    resource_name: "capo_codeconnections.types.resource_name.ResourceName"
    """<p>The name of the connection resource associated with a specific sync configuration.</p>"""
    role_arn: "capo_codeconnections.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role associated with a specific sync configuration.</p>"""
    sync_type: (
        "capo_codeconnections.types.sync_configuration_type.SyncConfigurationType"
    )
    """<p>The type of sync for a specific sync configuration.</p>"""
    publish_deployment_status: NotRequired[
        "capo_codeconnections.types.publish_deployment_status.PublishDeploymentStatus"
    ]
    """<p>Whether to enable or disable publishing of deployment status to source providers.</p>"""
    trigger_resource_update_on: NotRequired[
        "capo_codeconnections.types.trigger_resource_update_on.TriggerResourceUpdateOn"
    ]
    """<p>When to trigger Git sync to begin the stack update.</p>"""
    pull_request_comment: NotRequired[
        "capo_codeconnections.types.pull_request_comment.PullRequestComment"
    ]
    """<p>A toggle that specifies whether to enable or disable pull request comments for the sync configuration to be created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SyncConfiguration) -> dict:
    out: dict = {}
    out["Branch"] = value["branch"]
    if "config_file" in value:
        out["ConfigFile"] = value["config_file"]
    out["OwnerId"] = value["owner_id"]
    import capo_codeconnections.types.provider_type

    out["ProviderType"] = (
        capo_codeconnections.types.provider_type.serialize_aws_json_1_0(
            value["provider_type"]
        )
    )
    out["RepositoryLinkId"] = value["repository_link_id"]
    out["RepositoryName"] = value["repository_name"]
    out["ResourceName"] = value["resource_name"]
    out["RoleArn"] = value["role_arn"]
    import capo_codeconnections.types.sync_configuration_type

    out["SyncType"] = (
        capo_codeconnections.types.sync_configuration_type.serialize_aws_json_1_0(
            value["sync_type"]
        )
    )
    if "publish_deployment_status" in value:
        import capo_codeconnections.types.publish_deployment_status

        out["PublishDeploymentStatus"] = (
            capo_codeconnections.types.publish_deployment_status.serialize_aws_json_1_0(
                value["publish_deployment_status"]
            )
        )
    if "trigger_resource_update_on" in value:
        import capo_codeconnections.types.trigger_resource_update_on

        out["TriggerResourceUpdateOn"] = (
            capo_codeconnections.types.trigger_resource_update_on.serialize_aws_json_1_0(
                value["trigger_resource_update_on"]
            )
        )
    if "pull_request_comment" in value:
        import capo_codeconnections.types.pull_request_comment

        out["PullRequestComment"] = (
            capo_codeconnections.types.pull_request_comment.serialize_aws_json_1_0(
                value["pull_request_comment"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SyncConfiguration:
    out: SyncConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Branch") is not None:
        out["branch"] = data["Branch"]
    else:
        out["branch"] = ""
    if data.get("ConfigFile") is not None:
        out["config_file"] = data["ConfigFile"]
    if data.get("OwnerId") is not None:
        out["owner_id"] = data["OwnerId"]
    else:
        out["owner_id"] = ""
    if data.get("ProviderType") is not None:
        import capo_codeconnections.types.provider_type

        out["provider_type"] = (
            capo_codeconnections.types.provider_type.deserialize_aws_json_1_0(
                data["ProviderType"]
            )
        )
    else:
        import typing

        out["provider_type"] = typing.cast(
            "capo_codeconnections.types.provider_type.ProviderType", ""
        )
    if data.get("RepositoryLinkId") is not None:
        out["repository_link_id"] = data["RepositoryLinkId"]
    else:
        out["repository_link_id"] = ""
    if data.get("RepositoryName") is not None:
        out["repository_name"] = data["RepositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("ResourceName") is not None:
        out["resource_name"] = data["ResourceName"]
    else:
        out["resource_name"] = ""
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    if data.get("SyncType") is not None:
        import capo_codeconnections.types.sync_configuration_type

        out["sync_type"] = (
            capo_codeconnections.types.sync_configuration_type.deserialize_aws_json_1_0(
                data["SyncType"]
            )
        )
    else:
        import typing

        out["sync_type"] = typing.cast(
            "capo_codeconnections.types.sync_configuration_type.SyncConfigurationType",
            "",
        )
    if data.get("PublishDeploymentStatus") is not None:
        import capo_codeconnections.types.publish_deployment_status

        out["publish_deployment_status"] = (
            capo_codeconnections.types.publish_deployment_status.deserialize_aws_json_1_0(
                data["PublishDeploymentStatus"]
            )
        )
    if data.get("TriggerResourceUpdateOn") is not None:
        import capo_codeconnections.types.trigger_resource_update_on

        out["trigger_resource_update_on"] = (
            capo_codeconnections.types.trigger_resource_update_on.deserialize_aws_json_1_0(
                data["TriggerResourceUpdateOn"]
            )
        )
    if data.get("PullRequestComment") is not None:
        import capo_codeconnections.types.pull_request_comment

        out["pull_request_comment"] = (
            capo_codeconnections.types.pull_request_comment.deserialize_aws_json_1_0(
                data["PullRequestComment"]
            )
        )
    return out
