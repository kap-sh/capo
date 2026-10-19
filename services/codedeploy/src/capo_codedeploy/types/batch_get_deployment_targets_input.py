"""Generated from Smithy shape ``com.amazonaws.codedeploy#BatchGetDeploymentTargetsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_id
    import capo_codedeploy.types.target_id_list


class BatchGetDeploymentTargetsInput(TypedDict, closed=True):
    deployment_id: "capo_codedeploy.types.deployment_id.DeploymentId"
    """<p> The unique ID of a deployment. </p>"""
    target_ids: "capo_codedeploy.types.target_id_list.TargetIdList"
    """<p> The unique IDs of the deployment targets. The compute platform of the deployment determines the type of the targets and their formats. The maximum number of deployment target IDs you can specify is 25.</p> <ul> <li> <p> For deployments that use the EC2/On-premises compute platform, the target IDs are Amazon EC2 or on-premises instances IDs, and their target type is <code>instanceTarget</code>. </p> </li> <li> <p> For deployments that use the Lambda compute platform, the target IDs are the names of Lambda functions, and their target type is <code>instanceTarget</code>. </p> </li> <li> <p> For deployments that use the Amazon ECS compute platform, the target IDs are pairs of Amazon ECS clusters and services specified using the format <code><clustername>:<servicename></code>. Their target type is <code>ecsTarget</code>. </p> </li> <li> <p> For deployments that are deployed with CloudFormation, the target IDs are CloudFormation stack IDs. Their target type is <code>cloudFormationTarget</code>. </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDeploymentTargetsInput) -> dict:
    out: dict = {}
    out["deploymentId"] = value["deployment_id"]
    import capo_codedeploy.types.target_id_list

    out["targetIds"] = capo_codedeploy.types.target_id_list.serialize_aws_json_1_1(
        value["target_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDeploymentTargetsInput:
    out: BatchGetDeploymentTargetsInput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    else:
        out["deployment_id"] = ""
    if data.get("targetIds") is not None:
        import capo_codedeploy.types.target_id_list

        out["target_ids"] = (
            capo_codedeploy.types.target_id_list.deserialize_aws_json_1_1(
                data["targetIds"]
            )
        )
    else:
        out["target_ids"] = []
    return out
