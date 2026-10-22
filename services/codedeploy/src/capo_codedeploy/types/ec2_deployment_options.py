"""Generated from Smithy shape ``com.amazonaws.codedeploy#EC2DeploymentOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.auto_scaling_group_processes_to_suspend_list


class EC2DeploymentOptions(TypedDict, closed=True):
    auto_scaling_group_processes_to_suspend: NotRequired[
        "capo_codedeploy.types.auto_scaling_group_processes_to_suspend_list.AutoScalingGroupProcessesToSuspendList"
    ]
    """<p>The Amazon EC2 Auto Scaling processes to suspend during the deployment. CodeDeploy suspends these processes before it deploys to instances in an Auto Scaling group, and resumes them when the deployment succeeds, fails, or is stopped. Valid values are <code>Terminate</code>, <code>AZRebalance</code>, <code>InstanceRefresh</code>, and <code>ScheduledActions</code>.</p> <p>This parameter applies only to in-place deployments on the EC2/On-premises compute platform. If the list is empty, or if the deployment does not target instances in an Auto Scaling group, no processes are suspended.</p> <p>The service role for the deployment group must have permission to call <code>autoscaling:SuspendProcesses</code> and <code>autoscaling:ResumeProcesses</code> on the target Auto Scaling groups. If the processes cannot be suspended, the deployment fails before any instance is updated.</p> <p>If you suspend <code>ScheduledActions</code>, scheduled actions with a start time during the deployment are skipped and do not run after the process resumes.</p> <note> <p>If CodeDeploy cannot resume the processes, the deployment fails and the processes stay suspended until you resume them with the Auto Scaling <code>ResumeProcesses</code> action. While <code>Terminate</code> is suspended, Auto Scaling does not replace unhealthy instances. If you suspend <code>Terminate</code>, configure a trigger that notifies you when a deployment fails.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2DeploymentOptions) -> dict:
    out: dict = {}
    if "auto_scaling_group_processes_to_suspend" in value:
        import capo_codedeploy.types.auto_scaling_group_processes_to_suspend_list

        out["autoScalingGroupProcessesToSuspend"] = (
            capo_codedeploy.types.auto_scaling_group_processes_to_suspend_list.serialize_aws_json_1_1(
                value["auto_scaling_group_processes_to_suspend"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EC2DeploymentOptions:
    out: EC2DeploymentOptions = {}  # type: ignore[typeddict-item]
    if data.get("autoScalingGroupProcessesToSuspend") is not None:
        import capo_codedeploy.types.auto_scaling_group_processes_to_suspend_list

        out["auto_scaling_group_processes_to_suspend"] = (
            capo_codedeploy.types.auto_scaling_group_processes_to_suspend_list.deserialize_aws_json_1_1(
                data["autoScalingGroupProcessesToSuspend"]
            )
        )
    return out
