"""Generated from Smithy shape ``com.amazonaws.codedeploy#BatchGetDeploymentGroupsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.application_name
    import capo_codedeploy.types.deployment_groups_list


class BatchGetDeploymentGroupsInput(TypedDict, closed=True):
    application_name: "capo_codedeploy.types.application_name.ApplicationName"
    """<p>The name of an CodeDeploy application associated with the applicable user or Amazon Web Services account.</p>"""
    deployment_group_names: (
        "capo_codedeploy.types.deployment_groups_list.DeploymentGroupsList"
    )
    """<p>The names of the deployment groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDeploymentGroupsInput) -> dict:
    out: dict = {}
    out["applicationName"] = value["application_name"]
    import capo_codedeploy.types.deployment_groups_list

    out["deploymentGroupNames"] = (
        capo_codedeploy.types.deployment_groups_list.serialize_aws_json_1_1(
            value["deployment_group_names"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDeploymentGroupsInput:
    out: BatchGetDeploymentGroupsInput = {}  # type: ignore[typeddict-item]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    else:
        out["application_name"] = ""
    if data.get("deploymentGroupNames") is not None:
        import capo_codedeploy.types.deployment_groups_list

        out["deployment_group_names"] = (
            capo_codedeploy.types.deployment_groups_list.deserialize_aws_json_1_1(
                data["deploymentGroupNames"]
            )
        )
    else:
        out["deployment_group_names"] = []
    return out
