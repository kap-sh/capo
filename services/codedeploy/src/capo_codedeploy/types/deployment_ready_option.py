"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentReadyOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_ready_action
    import capo_codedeploy.types.duration


class DeploymentReadyOption(TypedDict, closed=True):
    action_on_timeout: NotRequired[
        "capo_codedeploy.types.deployment_ready_action.DeploymentReadyAction"
    ]
    """<p>Information about when to reroute traffic from an original environment to a replacement environment in a blue/green deployment.</p> <ul> <li> <p>CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment.</p> </li> <li> <p>STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic rerouting is started using <a>ContinueDeployment</a>. If traffic rerouting is not started before the end of the specified wait period, the deployment status is changed to Stopped.</p> </li> </ul>"""
    wait_time_in_minutes: "capo_codedeploy.types.duration.Duration"
    """<p>The number of minutes to wait before the status of a blue/green deployment is changed to Stopped if rerouting is not started manually. Applies only to the <code>STOP_DEPLOYMENT</code> option for <code>actionOnTimeout</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentReadyOption) -> dict:
    out: dict = {}
    if "action_on_timeout" in value:
        import capo_codedeploy.types.deployment_ready_action

        out["actionOnTimeout"] = (
            capo_codedeploy.types.deployment_ready_action.serialize_aws_json_1_1(
                value["action_on_timeout"]
            )
        )
    out["waitTimeInMinutes"] = value.get("wait_time_in_minutes", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentReadyOption:
    out: DeploymentReadyOption = {}  # type: ignore[typeddict-item]
    if data.get("actionOnTimeout") is not None:
        import capo_codedeploy.types.deployment_ready_action

        out["action_on_timeout"] = (
            capo_codedeploy.types.deployment_ready_action.deserialize_aws_json_1_1(
                data["actionOnTimeout"]
            )
        )
    if data.get("waitTimeInMinutes") is not None:
        out["wait_time_in_minutes"] = data["waitTimeInMinutes"]
    else:
        out["wait_time_in_minutes"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeploymentReadyOption) -> dict:
    out: dict = {}
    if "action_on_timeout" in value:
        import capo_codedeploy.types.deployment_ready_action

        out["actionOnTimeout"] = (
            capo_codedeploy.types.deployment_ready_action.serialize_cbor(
                value["action_on_timeout"]
            )
        )
    out["waitTimeInMinutes"] = value.get("wait_time_in_minutes", 0)
    return out


def deserialize_cbor(data: dict) -> DeploymentReadyOption:
    out: DeploymentReadyOption = {}  # type: ignore[typeddict-item]
    if data.get("actionOnTimeout") is not None:
        import capo_codedeploy.types.deployment_ready_action

        out["action_on_timeout"] = (
            capo_codedeploy.types.deployment_ready_action.deserialize_cbor(
                data["actionOnTimeout"]
            )
        )
    if data.get("waitTimeInMinutes") is not None:
        out["wait_time_in_minutes"] = data["waitTimeInMinutes"]
    else:
        out["wait_time_in_minutes"] = 0
    return out
