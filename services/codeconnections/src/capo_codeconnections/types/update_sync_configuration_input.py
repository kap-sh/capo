"""Generated from Smithy shape ``com.amazonaws.codeconnections#UpdateSyncConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.branch_name
    import capo_codeconnections.types.deployment_file_path
    import capo_codeconnections.types.iam_role_arn
    import capo_codeconnections.types.publish_deployment_status
    import capo_codeconnections.types.pull_request_comment
    import capo_codeconnections.types.repository_link_id
    import capo_codeconnections.types.resource_name
    import capo_codeconnections.types.sync_configuration_type
    import capo_codeconnections.types.trigger_resource_update_on


class UpdateSyncConfigurationInput(TypedDict, closed=True):
    branch: NotRequired["capo_codeconnections.types.branch_name.BranchName"]
    """<p>The branch for the sync configuration to be updated.</p>"""
    config_file: NotRequired[
        "capo_codeconnections.types.deployment_file_path.DeploymentFilePath"
    ]
    """<p>The configuration file for the sync configuration to be updated.</p>"""
    repository_link_id: NotRequired[
        "capo_codeconnections.types.repository_link_id.RepositoryLinkId"
    ]
    """<p>The ID of the repository link for the sync configuration to be updated.</p>"""
    resource_name: "capo_codeconnections.types.resource_name.ResourceName"
    """<p>The name of the Amazon Web Services resource for the sync configuration to be updated.</p>"""
    role_arn: NotRequired["capo_codeconnections.types.iam_role_arn.IamRoleArn"]
    """<p>The ARN of the IAM role for the sync configuration to be updated.</p>"""
    sync_type: (
        "capo_codeconnections.types.sync_configuration_type.SyncConfigurationType"
    )
    """<p>The sync type for the sync configuration to be updated.</p>"""
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
    """<p>TA toggle that specifies whether to enable or disable pull request comments for the sync configuration to be updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateSyncConfigurationInput) -> dict:
    out: dict = {}
    if "branch" in value:
        out["Branch"] = value["branch"]
    if "config_file" in value:
        out["ConfigFile"] = value["config_file"]
    if "repository_link_id" in value:
        out["RepositoryLinkId"] = value["repository_link_id"]
    out["ResourceName"] = value["resource_name"]
    if "role_arn" in value:
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


def deserialize_aws_json_1_0(data: dict) -> UpdateSyncConfigurationInput:
    out: UpdateSyncConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("Branch") is not None:
        out["branch"] = data["Branch"]
    if data.get("ConfigFile") is not None:
        out["config_file"] = data["ConfigFile"]
    if data.get("RepositoryLinkId") is not None:
        out["repository_link_id"] = data["RepositoryLinkId"]
    if data.get("ResourceName") is not None:
        out["resource_name"] = data["ResourceName"]
    else:
        out["resource_name"] = ""
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
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
