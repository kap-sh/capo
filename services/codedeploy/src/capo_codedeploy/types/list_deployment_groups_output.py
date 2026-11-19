"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListDeploymentGroupsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.application_name
    import capo_codedeploy.types.deployment_groups_list
    import capo_codedeploy.types.next_token


class ListDeploymentGroupsOutput(TypedDict, closed=True):
    application_name: NotRequired[
        "capo_codedeploy.types.application_name.ApplicationName"
    ]
    """<p>The application name.</p>"""
    deployment_groups: NotRequired[
        "capo_codedeploy.types.deployment_groups_list.DeploymentGroupsList"
    ]
    """<p>A list of deployment group names.</p>"""
    next_token: NotRequired["capo_codedeploy.types.next_token.NextToken"]
    """<p>If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list deployment groups call to return the next set of deployment groups in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDeploymentGroupsOutput) -> dict:
    out: dict = {}
    if "application_name" in value:
        out["applicationName"] = value["application_name"]
    if "deployment_groups" in value:
        import capo_codedeploy.types.deployment_groups_list

        out["deploymentGroups"] = (
            capo_codedeploy.types.deployment_groups_list.serialize_aws_json_1_1(
                value["deployment_groups"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDeploymentGroupsOutput:
    out: ListDeploymentGroupsOutput = {}  # type: ignore[typeddict-item]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    if data.get("deploymentGroups") is not None:
        import capo_codedeploy.types.deployment_groups_list

        out["deployment_groups"] = (
            capo_codedeploy.types.deployment_groups_list.deserialize_aws_json_1_1(
                data["deploymentGroups"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListDeploymentGroupsOutput) -> dict:
    out: dict = {}
    if "application_name" in value:
        out["applicationName"] = value["application_name"]
    if "deployment_groups" in value:
        import capo_codedeploy.types.deployment_groups_list

        out["deploymentGroups"] = (
            capo_codedeploy.types.deployment_groups_list.serialize_cbor(
                value["deployment_groups"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListDeploymentGroupsOutput:
    out: ListDeploymentGroupsOutput = {}  # type: ignore[typeddict-item]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    if data.get("deploymentGroups") is not None:
        import capo_codedeploy.types.deployment_groups_list

        out["deployment_groups"] = (
            capo_codedeploy.types.deployment_groups_list.deserialize_cbor(
                data["deploymentGroups"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
