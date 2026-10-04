"""Generated from Smithy shape ``com.amazonaws.ecs#CreateExpressGatewayServiceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.express_cpu_architecture
    import capo_ecs.types.express_gateway_container
    import capo_ecs.types.express_gateway_scaling_target
    import capo_ecs.types.express_gateway_service_network_configuration
    import capo_ecs.types.string
    import capo_ecs.types.tags


class CreateExpressGatewayServiceRequest(TypedDict, closed=True):
    execution_role_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make Amazon Web Services API calls on your behalf. This role is required for Amazon ECS to pull container images from Amazon ECR, send container logs to Amazon CloudWatch Logs, and retrieve sensitive data from Amazon Web Services Systems Manager Parameter Store or Amazon Web Services Secrets Manager.</p> <p>The execution role must include the <code>AmazonECSTaskExecutionRolePolicy</code> managed policy or equivalent permissions. For Express services, this role is used during task startup and runtime for container management operations.</p>"""
    infrastructure_role_arn: "capo_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the infrastructure role that grants Amazon ECS permission to create and manage Amazon Web Services resources on your behalf for the Express service. This role is used to provision and manage Application Load Balancers, target groups, security groups, auto-scaling policies, and other Amazon Web Services infrastructure components.</p> <p>The infrastructure role must include permissions for Elastic Load Balancing, Application Auto Scaling, Amazon EC2 (for security groups), and other services required for managed infrastructure. This role is only used during Express service creation, updates, and deletion operations.</p>"""
    service_name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the Express service. This name must be unique within the specified cluster and can contain up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens. The name is used to identify the service in the Amazon ECS console and API operations.</p> <p>If you don't specify a service name, Amazon ECS generates a unique name for the service. The service name becomes part of the service ARN and cannot be changed after the service is created.</p>"""
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster on which to create the Express service. If you do not specify a cluster, the <code>default</code> cluster is assumed.</p>"""
    health_check_path: NotRequired["capo_ecs.types.string.String"]
    """<p>The path on the container that the Application Load Balancer uses for health checks. This should be a valid HTTP endpoint that returns a successful response (HTTP 200) when the application is healthy.</p> <p>If not specified, the default health check path is <code>/ping</code>. The health check path must start with a forward slash and can include query parameters. Examples: <code>/health</code>, <code>/api/status</code>, <code>/ping?format=json</code>.</p>"""
    primary_container: NotRequired[
        "capo_ecs.types.express_gateway_container.ExpressGatewayContainer"
    ]
    """<p>The primary container configuration for the Express service. This defines the main application container that will receive traffic from the Application Load Balancer.</p> <p>The primary container must specify at minimum a container image. You can also configure the container port (defaults to 80), logging configuration, environment variables, secrets, and startup commands. The container image can be from Amazon ECR, Docker Hub, or any other container registry accessible to your execution role.</p>"""
    task_role_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. This role allows your application code to access other Amazon Web Services services securely.</p> <p>The task role is different from the execution role. While the execution role is used by the Amazon ECS agent to set up the task, the task role is used by your application code running inside the container to make Amazon Web Services API calls. If your application doesn't need to access Amazon Web Services services, you can omit this parameter.</p>"""
    network_configuration: NotRequired[
        "capo_ecs.types.express_gateway_service_network_configuration.ExpressGatewayServiceNetworkConfiguration"
    ]
    """<p>The network configuration for the Express service tasks. This specifies the VPC subnets and security groups for the tasks.</p> <p>For Express services, you can specify custom security groups and subnets. If not provided, Amazon ECS will use the default VPC configuration and create appropriate security groups automatically. The network configuration determines how your service integrates with your VPC and what network access it has.</p>"""
    cpu: NotRequired["capo_ecs.types.string.String"]
    """<p>The number of CPU units used by the task. This parameter determines the CPU allocation for each task in the Express service. The default value for an Express service is 256 (.25 vCPU).</p>"""
    memory: NotRequired["capo_ecs.types.string.String"]
    """<p>The amount of memory (in MiB) used by the task. This parameter determines the memory allocation for each task in the Express service. The default value for an express service is 512 MiB.</p>"""
    cpu_architecture: NotRequired[
        "capo_ecs.types.express_cpu_architecture.ExpressCpuArchitecture"
    ]
    """<p>The CPU architecture that the task runs on. If you don't specify a value, the default is <code>X86_64</code>.</p> <p>Valid values:</p> <ul> <li> <p> <code>X86_64</code> - The x86 64-bit architecture.</p> </li> <li> <p> <code>ARM64</code> - The 64-bit ARM architecture.</p> </li> </ul> <p>Ensure that the container image you specify supports the architecture you choose. The operating system family for an Express service is always <code>LINUX</code>.</p> <p>You can't specify <code>cpuArchitecture</code> together with <code>taskDefinitionArn</code>.</p>"""
    scaling_target: NotRequired[
        "capo_ecs.types.express_gateway_scaling_target.ExpressGatewayScalingTarget"
    ]
    """<p>The auto-scaling configuration for the Express service. This defines how the service automatically adjusts the number of running tasks based on demand.</p> <p>You can specify the minimum and maximum number of tasks, the scaling metric (CPU utilization, memory utilization, or request count per target), and the target value for the metric. If not specified, the default target value for an Express service is 60.</p>"""
    tags: NotRequired["capo_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the Express service to help categorize and organize it. Each tag consists of a key and an optional value. You can apply up to 50 tags to a service.</p>"""
    task_definition_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of a task definition to use to create the Express Gateway service. This allows you to manage your own task definition, giving you more control over the service configuration such as adding sidecar containers.</p> <p>The task definition must have a container named <code>Main</code> with a single TCP port mapping that includes a container port and port name. The task definition must also have <code>FARGATE</code> compatibility.</p> <p>If you provide a task definition ARN, you cannot also specify <code>primaryContainer</code>, <code>executionRoleArn</code>, <code>taskRoleArn</code>, <code>cpu</code>, <code>memory</code>, or <code>cpuArchitecture</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateExpressGatewayServiceRequest) -> dict:
    out: dict = {}
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    out["infrastructureRoleArn"] = value["infrastructure_role_arn"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "cluster" in value:
        out["cluster"] = value["cluster"]
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
    if "tags" in value:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.serialize_aws_json_1_1(value["tags"])
    if "task_definition_arn" in value:
        out["taskDefinitionArn"] = value["task_definition_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateExpressGatewayServiceRequest:
    out: CreateExpressGatewayServiceRequest = {}  # type: ignore[typeddict-item]
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    if data.get("infrastructureRoleArn") is not None:
        out["infrastructure_role_arn"] = data["infrastructureRoleArn"]
    else:
        raise DeserializationError(
            "CreateExpressGatewayServiceRequest.infrastructure_role_arn required"
        )
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
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
    if data.get("tags") is not None:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.deserialize_aws_json_1_1(data["tags"])
    if data.get("taskDefinitionArn") is not None:
        out["task_definition_arn"] = data["taskDefinitionArn"]
    return out
