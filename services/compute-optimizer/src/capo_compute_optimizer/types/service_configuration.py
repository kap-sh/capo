"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ServiceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.auto_scaling_configuration
    import capo_compute_optimizer.types.container_configurations
    import capo_compute_optimizer.types.nullable_cpu
    import capo_compute_optimizer.types.nullable_memory
    import capo_compute_optimizer.types.task_definition_arn


class ServiceConfiguration(TypedDict, closed=True):
    memory: NotRequired["capo_compute_optimizer.types.nullable_memory.NullableMemory"]
    """<p> The amount of memory used by the tasks in the Amazon ECS service. </p>"""
    cpu: NotRequired["capo_compute_optimizer.types.nullable_cpu.NullableCpu"]
    """<p> The number of CPU units used by the tasks in the Amazon ECS service. </p>"""
    container_configurations: NotRequired[
        "capo_compute_optimizer.types.container_configurations.ContainerConfigurations"
    ]
    """<p> The container configurations within a task of an Amazon ECS service. </p>"""
    auto_scaling_configuration: NotRequired[
        "capo_compute_optimizer.types.auto_scaling_configuration.AutoScalingConfiguration"
    ]
    """<p> Describes the Auto Scaling configuration methods for an Amazon ECS service. This affects the generated recommendations. For example, if Auto Scaling is configured on a service’s CPU, then Compute Optimizer doesn’t generate CPU size recommendations. </p> <p>The Auto Scaling configuration methods include:</p> <ul> <li> <p> <code>TARGET_TRACKING_SCALING_CPU</code> — If the Amazon ECS service is configured to use target scaling on CPU, Compute Optimizer doesn't generate CPU recommendations.</p> </li> <li> <p> <code>TARGET_TRACKING_SCALING_MEMORY</code> — If the Amazon ECS service is configured to use target scaling on memory, Compute Optimizer doesn't generate memory recommendations.</p> </li> </ul> <p>For more information about step scaling and target scaling, see <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html"> Step scaling policies for Application Auto Scaling</a> and <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html"> Target tracking scaling policies for Application Auto Scaling</a> in the <i>Application Auto Scaling User Guide</i>.</p>"""
    task_definition_arn: NotRequired[
        "capo_compute_optimizer.types.task_definition_arn.TaskDefinitionArn"
    ]
    """<p> The task definition ARN used by the tasks in the Amazon ECS service. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceConfiguration) -> dict:
    out: dict = {}
    if "memory" in value:
        out["memory"] = value["memory"]
    if "cpu" in value:
        out["cpu"] = value["cpu"]
    if "container_configurations" in value:
        import capo_compute_optimizer.types.container_configurations

        out["containerConfigurations"] = (
            capo_compute_optimizer.types.container_configurations.serialize_aws_json_1_0(
                value["container_configurations"]
            )
        )
    if "auto_scaling_configuration" in value:
        import capo_compute_optimizer.types.auto_scaling_configuration

        out["autoScalingConfiguration"] = (
            capo_compute_optimizer.types.auto_scaling_configuration.serialize_aws_json_1_0(
                value["auto_scaling_configuration"]
            )
        )
    if "task_definition_arn" in value:
        out["taskDefinitionArn"] = value["task_definition_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceConfiguration:
    out: ServiceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("memory") is not None:
        out["memory"] = data["memory"]
    if data.get("cpu") is not None:
        out["cpu"] = data["cpu"]
    if data.get("containerConfigurations") is not None:
        import capo_compute_optimizer.types.container_configurations

        out["container_configurations"] = (
            capo_compute_optimizer.types.container_configurations.deserialize_aws_json_1_0(
                data["containerConfigurations"]
            )
        )
    if data.get("autoScalingConfiguration") is not None:
        import capo_compute_optimizer.types.auto_scaling_configuration

        out["auto_scaling_configuration"] = (
            capo_compute_optimizer.types.auto_scaling_configuration.deserialize_aws_json_1_0(
                data["autoScalingConfiguration"]
            )
        )
    if data.get("taskDefinitionArn") is not None:
        out["task_definition_arn"] = data["taskDefinitionArn"]
    return out
