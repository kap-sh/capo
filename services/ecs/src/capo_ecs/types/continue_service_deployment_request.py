"""Generated from Smithy shape ``com.amazonaws.ecs#ContinueServiceDeploymentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.deployment_lifecycle_hook_action
    import capo_ecs.types.string


class ContinueServiceDeploymentRequest(TypedDict, closed=True):
    service_deployment_arn: "capo_ecs.types.string.String"
    """<p>The ARN of the service deployment to continue or roll back.</p>"""
    hook_id: "capo_ecs.types.string.String"
    """<p>The ID of the paused lifecycle hook to act on. You can find the <code>hookId</code> by calling <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceDeployments.html">DescribeServiceDeployments</a> and inspecting the <code>lifecycleHookDetails</code> field of the service deployment.</p>"""
    action: NotRequired[
        "capo_ecs.types.deployment_lifecycle_hook_action.DeploymentLifecycleHookAction"
    ]
    """<p>The action to take on the paused lifecycle hook. Valid values are:</p> <ul> <li> <p> <code>CONTINUE</code> - Proceeds the deployment to the next lifecycle stage.</p> </li> <li> <p> <code>ROLLBACK</code> - Rolls back the deployment to the previous service revision.</p> </li> </ul> <p>If no value is specified, the default action is <code>CONTINUE</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContinueServiceDeploymentRequest) -> dict:
    out: dict = {}
    out["serviceDeploymentArn"] = value["service_deployment_arn"]
    out["hookId"] = value["hook_id"]
    if "action" in value:
        import capo_ecs.types.deployment_lifecycle_hook_action

        out["action"] = (
            capo_ecs.types.deployment_lifecycle_hook_action.serialize_aws_json_1_1(
                value["action"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContinueServiceDeploymentRequest:
    out: ContinueServiceDeploymentRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceDeploymentArn") is not None:
        out["service_deployment_arn"] = data["serviceDeploymentArn"]
    else:
        raise DeserializationError(
            "ContinueServiceDeploymentRequest.service_deployment_arn required"
        )
    if data.get("hookId") is not None:
        out["hook_id"] = data["hookId"]
    else:
        raise DeserializationError("ContinueServiceDeploymentRequest.hook_id required")
    if data.get("action") is not None:
        import capo_ecs.types.deployment_lifecycle_hook_action

        out["action"] = (
            capo_ecs.types.deployment_lifecycle_hook_action.deserialize_aws_json_1_1(
                data["action"]
            )
        )
    return out
