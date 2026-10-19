"""Generated from Smithy shape ``com.amazonaws.codedeploy#BatchGetDeploymentsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployments_list


class BatchGetDeploymentsInput(TypedDict, closed=True):
    deployment_ids: "capo_codedeploy.types.deployments_list.DeploymentsList"
    """<p> A list of deployment IDs, separated by spaces. The maximum number of deployment IDs you can specify is 25.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDeploymentsInput) -> dict:
    out: dict = {}
    import capo_codedeploy.types.deployments_list

    out["deploymentIds"] = (
        capo_codedeploy.types.deployments_list.serialize_aws_json_1_1(
            value["deployment_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDeploymentsInput:
    out: BatchGetDeploymentsInput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentIds") is not None:
        import capo_codedeploy.types.deployments_list

        out["deployment_ids"] = (
            capo_codedeploy.types.deployments_list.deserialize_aws_json_1_1(
                data["deploymentIds"]
            )
        )
    else:
        out["deployment_ids"] = []
    return out
