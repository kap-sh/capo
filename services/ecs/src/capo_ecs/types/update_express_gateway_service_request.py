"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateExpressGatewayServiceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.express_cpu_architecture
    import capo_ecs.types.express_gateway_container
    import capo_ecs.types.express_gateway_scaling_target
    import capo_ecs.types.express_gateway_service_network_configuration
    import capo_ecs.types.string


class UpdateExpressGatewayServiceRequest(TypedDict, closed=True):
    service_arn: "capo_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the Express service to update.</p>"""
    execution_role_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the task execution role for the Express service.</p>"""
    health_check_path: NotRequired["capo_ecs.types.string.String"]
    """<p>The path on the container for Application Load Balancer health checks.</p>"""
    primary_container: NotRequired[
        "capo_ecs.types.express_gateway_container.ExpressGatewayContainer"
    ]
    """<p>The primary container configuration for the Express service.</p>"""
    task_role_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role for containers in this task.</p>"""
    network_configuration: NotRequired[
        "capo_ecs.types.express_gateway_service_network_configuration.ExpressGatewayServiceNetworkConfiguration"
    ]
    """<p>The network configuration for the Express service tasks. By default, the network configuration for an Express service uses the default VPC.</p>"""
    cpu: NotRequired["capo_ecs.types.string.String"]
    """<p>The number of CPU units used by the task.</p>"""
    memory: NotRequired["capo_ecs.types.string.String"]
    """<p>The amount of memory (in MiB) used by the task.</p>"""
    cpu_architecture: NotRequired[
        "capo_ecs.types.express_cpu_architecture.ExpressCpuArchitecture"
    ]
    """<p>The CPU architecture that the task runs on. If you don't specify a value, the service keeps its current architecture.</p> <p>Valid values:</p> <ul> <li> <p> <code>X86_64</code> - The x86 64-bit architecture.</p> </li> <li> <p> <code>ARM64</code> - The 64-bit ARM architecture.</p> </li> </ul> <p>Changing the architecture starts a new deployment that replaces the running tasks. Ensure that the container image you specify supports the architecture you choose. The operating system family for an Express service is always <code>LINUX</code>.</p> <p>You can't specify <code>cpuArchitecture</code> together with <code>taskDefinitionArn</code>.</p>"""
    scaling_target: NotRequired[
        "capo_ecs.types.express_gateway_scaling_target.ExpressGatewayScalingTarget"
    ]
    """<p>The auto-scaling configuration for the Express service.</p>"""
    task_definition_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of a task definition to use to update the Express Gateway service. This allows you to manage your own task definition, giving you more control over the service configuration such as adding sidecar containers.</p> <p>The task definition must have a container named <code>Main</code> with a single TCP port mapping that includes a container port and port name. The task definition must also have <code>FARGATE</code> compatibility.</p> <p>If you provide a task definition ARN, you cannot also specify <code>primaryContainer</code>, <code>executionRoleArn</code>, <code>taskRoleArn</code>, <code>cpu</code>, <code>memory</code>, or <code>cpuArchitecture</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateExpressGatewayServiceRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    if "health_check_path" in value:
        out["healthCheckPath"] = value["health_check_path"]
    if "primary_container" in value:
        import capo_ecs.types.express_gateway_container

        out["primaryContainer"] = (
            capo_ecs.types.express_gateway_container.serialize_aws_json_1_1(
                value["primary_container"]
            )
        )
    if "task_role_arn" in value:
        out["taskRoleArn"] = value["task_role_arn"]
    if "network_configuration" in value:
        import capo_ecs.types.express_gateway_service_network_configuration

        out["networkConfiguration"] = (
            capo_ecs.types.express_gateway_service_network_configuration.serialize_aws_json_1_1(
                value["network_configuration"]
            )
        )
    if "cpu" in value:
        out["cpu"] = value["cpu"]
    if "memory" in value:
        out["memory"] = value["memory"]
    if "cpu_architecture" in value:
        import capo_ecs.types.express_cpu_architecture

        out["cpuArchitecture"] = (
            capo_ecs.types.express_cpu_architecture.serialize_aws_json_1_1(
                value["cpu_architecture"]
            )
        )
    if "scaling_target" in value:
        import capo_ecs.types.express_gateway_scaling_target

        out["scalingTarget"] = (
            capo_ecs.types.express_gateway_scaling_target.serialize_aws_json_1_1(
                value["scaling_target"]
            )
        )
    if "task_definition_arn" in value:
        out["taskDefinitionArn"] = value["task_definition_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateExpressGatewayServiceRequest:
    out: UpdateExpressGatewayServiceRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError(
            "UpdateExpressGatewayServiceRequest.service_arn required"
        )
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    if data.get("healthCheckPath") is not None:
        out["health_check_path"] = data["healthCheckPath"]
    if data.get("primaryContainer") is not None:
        import capo_ecs.types.express_gateway_container

        out["primary_container"] = (
            capo_ecs.types.express_gateway_container.deserialize_aws_json_1_1(
                data["primaryContainer"]
            )
        )
    if data.get("taskRoleArn") is not None:
        out["task_role_arn"] = data["taskRoleArn"]
    if data.get("networkConfiguration") is not None:
        import capo_ecs.types.express_gateway_service_network_configuration

        out["network_configuration"] = (
            capo_ecs.types.express_gateway_service_network_configuration.deserialize_aws_json_1_1(
                data["networkConfiguration"]
            )
        )
    if data.get("cpu") is not None:
        out["cpu"] = data["cpu"]
    if data.get("memory") is not None:
        out["memory"] = data["memory"]
    if data.get("cpuArchitecture") is not None:
        import capo_ecs.types.express_cpu_architecture

        out["cpu_architecture"] = (
            capo_ecs.types.express_cpu_architecture.deserialize_aws_json_1_1(
                data["cpuArchitecture"]
            )
        )
    if data.get("scalingTarget") is not None:
        import capo_ecs.types.express_gateway_scaling_target

        out["scaling_target"] = (
            capo_ecs.types.express_gateway_scaling_target.deserialize_aws_json_1_1(
                data["scalingTarget"]
            )
        )
    if data.get("taskDefinitionArn") is not None:
        out["task_definition_arn"] = data["taskDefinitionArn"]
    return out
