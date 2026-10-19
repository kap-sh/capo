"""Generated from Smithy shape ``com.amazonaws.codedeploy#BatchGetDeploymentInstancesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_id
    import capo_codedeploy.types.instances_list


class BatchGetDeploymentInstancesInput(TypedDict, closed=True):
    deployment_id: "capo_codedeploy.types.deployment_id.DeploymentId"
    """<p> The unique ID of a deployment. </p>"""
    instance_ids: "capo_codedeploy.types.instances_list.InstancesList"
    """<p>The unique IDs of instances used in the deployment. The maximum number of instance IDs you can specify is 25.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDeploymentInstancesInput) -> dict:
    out: dict = {}
    out["deploymentId"] = value["deployment_id"]
    import capo_codedeploy.types.instances_list

    out["instanceIds"] = capo_codedeploy.types.instances_list.serialize_aws_json_1_1(
        value["instance_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDeploymentInstancesInput:
    out: BatchGetDeploymentInstancesInput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    else:
        out["deployment_id"] = ""
    if data.get("instanceIds") is not None:
        import capo_codedeploy.types.instances_list

        out["instance_ids"] = (
            capo_codedeploy.types.instances_list.deserialize_aws_json_1_1(
                data["instanceIds"]
            )
        )
    else:
        out["instance_ids"] = []
    return out
