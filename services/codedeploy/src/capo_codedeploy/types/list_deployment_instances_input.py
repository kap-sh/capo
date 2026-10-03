"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListDeploymentInstancesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_id
    import capo_codedeploy.types.instance_status_list
    import capo_codedeploy.types.instance_type_list
    import capo_codedeploy.types.next_token


class ListDeploymentInstancesInput(TypedDict, closed=True):
    deployment_id: "capo_codedeploy.types.deployment_id.DeploymentId"
    """<p> The unique ID of a deployment. </p>"""
    next_token: NotRequired["capo_codedeploy.types.next_token.NextToken"]
    """<p>An identifier returned from the previous list deployment instances call. It can be used to return the next set of deployment instances in the list.</p>"""
    instance_status_filter: NotRequired[
        "capo_codedeploy.types.instance_status_list.InstanceStatusList"
    ]
    """<p>A subset of instances to list by status:</p> <ul> <li> <p> <code>Pending</code>: Include those instances with pending deployments.</p> </li> <li> <p> <code>InProgress</code>: Include those instances where deployments are still in progress.</p> </li> <li> <p> <code>Succeeded</code>: Include those instances with successful deployments.</p> </li> <li> <p> <code>Failed</code>: Include those instances with failed deployments.</p> </li> <li> <p> <code>Skipped</code>: Include those instances with skipped deployments.</p> </li> <li> <p> <code>Unknown</code>: Include those instances with deployments in an unknown state.</p> </li> </ul>"""
    instance_type_filter: NotRequired[
        "capo_codedeploy.types.instance_type_list.InstanceTypeList"
    ]
    """<p>The set of instances in a blue/green deployment, either those in the original environment ("BLUE") or those in the replacement environment ("GREEN"), for which you want to view instance information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDeploymentInstancesInput) -> dict:
    out: dict = {}
    out["deploymentId"] = value["deployment_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "instance_status_filter" in value:
        import capo_codedeploy.types.instance_status_list

        out["instanceStatusFilter"] = (
            capo_codedeploy.types.instance_status_list.serialize_aws_json_1_1(
                value["instance_status_filter"]
            )
        )
    if "instance_type_filter" in value:
        import capo_codedeploy.types.instance_type_list

        out["instanceTypeFilter"] = (
            capo_codedeploy.types.instance_type_list.serialize_aws_json_1_1(
                value["instance_type_filter"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDeploymentInstancesInput:
    out: ListDeploymentInstancesInput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    else:
        raise DeserializationError(
            "ListDeploymentInstancesInput.deployment_id required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("instanceStatusFilter") is not None:
        import capo_codedeploy.types.instance_status_list

        out["instance_status_filter"] = (
            capo_codedeploy.types.instance_status_list.deserialize_aws_json_1_1(
                data["instanceStatusFilter"]
            )
        )
    if data.get("instanceTypeFilter") is not None:
        import capo_codedeploy.types.instance_type_list

        out["instance_type_filter"] = (
            capo_codedeploy.types.instance_type_list.deserialize_aws_json_1_1(
                data["instanceTypeFilter"]
            )
        )
    return out
