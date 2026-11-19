"""Generated from Smithy shape ``com.amazonaws.codedeploy#BlueInstanceTerminationOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.duration
    import capo_codedeploy.types.instance_action


class BlueInstanceTerminationOption(TypedDict, closed=True):
    action: NotRequired["capo_codedeploy.types.instance_action.InstanceAction"]
    """<p>The action to take on instances in the original environment after a successful blue/green deployment.</p> <ul> <li> <p> <code>TERMINATE</code>: Instances are terminated after a specified wait time.</p> </li> <li> <p> <code>KEEP_ALIVE</code>: Instances are left running after they are deregistered from the load balancer and removed from the deployment group.</p> </li> </ul>"""
    termination_wait_time_in_minutes: "capo_codedeploy.types.duration.Duration"
    """<p>For an Amazon EC2 deployment, the number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.</p> <p> For an Amazon ECS deployment, the number of minutes before deleting the original (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original (blue) task set to a replacement (green) task set. </p> <p> The maximum setting is 2880 minutes (2 days). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlueInstanceTerminationOption) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_codedeploy.types.instance_action

        out["action"] = capo_codedeploy.types.instance_action.serialize_aws_json_1_1(
            value["action"]
        )
    out["terminationWaitTimeInMinutes"] = value.get(
        "termination_wait_time_in_minutes", 0
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BlueInstanceTerminationOption:
    out: BlueInstanceTerminationOption = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        import capo_codedeploy.types.instance_action

        out["action"] = capo_codedeploy.types.instance_action.deserialize_aws_json_1_1(
            data["action"]
        )
    if data.get("terminationWaitTimeInMinutes") is not None:
        out["termination_wait_time_in_minutes"] = data["terminationWaitTimeInMinutes"]
    else:
        out["termination_wait_time_in_minutes"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BlueInstanceTerminationOption) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_codedeploy.types.instance_action

        out["action"] = capo_codedeploy.types.instance_action.serialize_cbor(
            value["action"]
        )
    out["terminationWaitTimeInMinutes"] = value.get(
        "termination_wait_time_in_minutes", 0
    )
    return out


def deserialize_cbor(data: dict) -> BlueInstanceTerminationOption:
    out: BlueInstanceTerminationOption = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        import capo_codedeploy.types.instance_action

        out["action"] = capo_codedeploy.types.instance_action.deserialize_cbor(
            data["action"]
        )
    if data.get("terminationWaitTimeInMinutes") is not None:
        out["termination_wait_time_in_minutes"] = data["terminationWaitTimeInMinutes"]
    else:
        out["termination_wait_time_in_minutes"] = 0
    return out
