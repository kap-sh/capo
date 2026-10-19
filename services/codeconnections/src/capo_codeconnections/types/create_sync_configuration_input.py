"""Generated from Smithy shape ``com.amazonaws.codeconnections#CreateSyncConfigurationInput``."""

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


class CreateSyncConfigurationInput(TypedDict, closed=True):
    branch: "capo_codeconnections.types.branch_name.BranchName"
    """<p>The branch in the repository from which changes will be synced.</p>"""
    config_file: "capo_codeconnections.types.deployment_file_path.DeploymentFilePath"
    """<p>The file name of the configuration file that manages syncing between the connection and the repository. This configuration file is stored in the repository.</p>"""
    repository_link_id: "capo_codeconnections.types.repository_link_id.RepositoryLinkId"
    """<p>The ID of the repository link created for the connection. A repository link allows Git sync to monitor and sync changes to files in a specified Git repository.</p>"""
    resource_name: "capo_codeconnections.types.resource_name.ResourceName"
    """<p>The name of the Amazon Web Services resource (for example, a CloudFormation stack in the case of CFN_STACK_SYNC) that will be synchronized from the linked repository.</p>"""
    role_arn: "capo_codeconnections.types.iam_role_arn.IamRoleArn"
    """<p>The ARN of the IAM role that grants permission for Amazon Web Services to use Git sync to update a given Amazon Web Services resource on your behalf.</p>"""
    sync_type: (
        "capo_codeconnections.types.sync_configuration_type.SyncConfigurationType"
    )
    """<p>The type of sync configuration.</p>"""
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
def serialize_aws_json_1_0(value: CreateSyncConfigurationInput) -> dict:
    out: dict = {}
    out["Branch"] = value["branch"]
    out["ConfigFile"] = value["config_file"]
    out["RepositoryLinkId"] = value["repository_link_id"]
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


def deserialize_aws_json_1_0(data: dict) -> CreateSyncConfigurationInput:
    out: CreateSyncConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("Branch") is not None:
        out["branch"] = data["Branch"]
    else:
        out["branch"] = ""
    if data.get("ConfigFile") is not None:
        out["config_file"] = data["ConfigFile"]
    else:
        out["config_file"] = ""
    if data.get("RepositoryLinkId") is not None:
        out["repository_link_id"] = data["RepositoryLinkId"]
    else:
        out["repository_link_id"] = ""
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
