"""Generated from Smithy shape ``com.amazonaws.ecs#Container``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.gpu_ids
    import capo_ecs.types.health_status
    import capo_ecs.types.managed_agents
    import capo_ecs.types.network_bindings
    import capo_ecs.types.network_interfaces
    import capo_ecs.types.neuron_device_ids
    import capo_ecs.types.sharing_strategy
    import capo_ecs.types.string


class Container(TypedDict, closed=True):
    container_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the container.</p>"""
    task_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN of the task.</p>"""
    name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the container.</p>"""
    image: NotRequired["capo_ecs.types.string.String"]
    """<p>The image used for the container.</p>"""
    image_digest: NotRequired["capo_ecs.types.string.String"]
    """<p>The container image manifest digest.</p>"""
    runtime_id: NotRequired["capo_ecs.types.string.String"]
    """<p>The ID of the Docker container.</p>"""
    last_status: NotRequired["capo_ecs.types.string.String"]
    """<p>The last known status of the container.</p>"""
    exit_code: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The exit code returned from the container.</p>"""
    reason: NotRequired["capo_ecs.types.string.String"]
    """<p>A short (1024 max characters) human-readable string to provide additional details about a running or stopped container.</p>"""
    network_bindings: NotRequired["capo_ecs.types.network_bindings.NetworkBindings"]
    """<p>The network bindings associated with the container.</p>"""
    network_interfaces: NotRequired[
        "capo_ecs.types.network_interfaces.NetworkInterfaces"
    ]
    """<p>The network interfaces associated with the container.</p>"""
    health_status: NotRequired["capo_ecs.types.health_status.HealthStatus"]
    """<p>The health status of the container. If health checks aren't configured for this container in its task definition, then it reports the health status as <code>UNKNOWN</code>.</p>"""
    managed_agents: NotRequired["capo_ecs.types.managed_agents.ManagedAgents"]
    """<p>The details of any Amazon ECS managed agents associated with the container.</p>"""
    cpu: NotRequired["capo_ecs.types.string.String"]
    """<p>The number of CPU units set for the container. The value is <code>0</code> if no value was specified in the container definition when the task definition was registered.</p>"""
    memory: NotRequired["capo_ecs.types.string.String"]
    """<p>The hard limit (in MiB) of memory set for the container.</p>"""
    memory_reservation: NotRequired["capo_ecs.types.string.String"]
    """<p>The soft limit (in MiB) of memory set for the container.</p>"""
    gpu_ids: NotRequired["capo_ecs.types.gpu_ids.GpuIds"]
    """<p>The IDs of each GPU assigned to the container.</p>"""
    neuron_device_ids: NotRequired["capo_ecs.types.neuron_device_ids.NeuronDeviceIds"]
    """<p>The IDs of each Neuron device assigned to the container.</p>"""
    gpu_sharing_strategy: NotRequired["capo_ecs.types.sharing_strategy.SharingStrategy"]
    """<p>The GPU sharing strategy that the task definition specifies for the container. This field is present only for containers whose resource requirements include <code>sharingStrategy</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Container) -> dict:
    out: dict = {}
    if "container_arn" in value:
        out["containerArn"] = value["container_arn"]
    if "task_arn" in value:
        out["taskArn"] = value["task_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "image" in value:
        out["image"] = value["image"]
    if "image_digest" in value:
        out["imageDigest"] = value["image_digest"]
    if "runtime_id" in value:
        out["runtimeId"] = value["runtime_id"]
    if "last_status" in value:
        out["lastStatus"] = value["last_status"]
    if "exit_code" in value:
        out["exitCode"] = value["exit_code"]
    if "reason" in value:
        out["reason"] = value["reason"]
    if "network_bindings" in value:
        import capo_ecs.types.network_bindings

        out["networkBindings"] = capo_ecs.types.network_bindings.serialize_aws_json_1_1(
            value["network_bindings"]
        )
    if "network_interfaces" in value:
        import capo_ecs.types.network_interfaces

        out["networkInterfaces"] = (
            capo_ecs.types.network_interfaces.serialize_aws_json_1_1(
                value["network_interfaces"]
            )
        )
    if "health_status" in value:
        import capo_ecs.types.health_status

        out["healthStatus"] = capo_ecs.types.health_status.serialize_aws_json_1_1(
            value["health_status"]
        )
    if "managed_agents" in value:
        import capo_ecs.types.managed_agents

        out["managedAgents"] = capo_ecs.types.managed_agents.serialize_aws_json_1_1(
            value["managed_agents"]
        )
    if "cpu" in value:
        out["cpu"] = value["cpu"]
    if "memory" in value:
        out["memory"] = value["memory"]
    if "memory_reservation" in value:
        out["memoryReservation"] = value["memory_reservation"]
    if "gpu_ids" in value:
        import capo_ecs.types.gpu_ids

        out["gpuIds"] = capo_ecs.types.gpu_ids.serialize_aws_json_1_1(value["gpu_ids"])
    if "neuron_device_ids" in value:
        import capo_ecs.types.neuron_device_ids

        out["neuronDeviceIds"] = (
            capo_ecs.types.neuron_device_ids.serialize_aws_json_1_1(
                value["neuron_device_ids"]
            )
        )
    if "gpu_sharing_strategy" in value:
        import capo_ecs.types.sharing_strategy

        out["gpuSharingStrategy"] = (
            capo_ecs.types.sharing_strategy.serialize_aws_json_1_1(
                value["gpu_sharing_strategy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Container:
    out: Container = {}  # type: ignore[typeddict-item]
    if data.get("containerArn") is not None:
        out["container_arn"] = data["containerArn"]
    if data.get("taskArn") is not None:
        out["task_arn"] = data["taskArn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("image") is not None:
        out["image"] = data["image"]
    if data.get("imageDigest") is not None:
        out["image_digest"] = data["imageDigest"]
    if data.get("runtimeId") is not None:
        out["runtime_id"] = data["runtimeId"]
    if data.get("lastStatus") is not None:
        out["last_status"] = data["lastStatus"]
    if data.get("exitCode") is not None:
        out["exit_code"] = data["exitCode"]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("networkBindings") is not None:
        import capo_ecs.types.network_bindings

        out["network_bindings"] = (
            capo_ecs.types.network_bindings.deserialize_aws_json_1_1(
                data["networkBindings"]
            )
        )
    if data.get("networkInterfaces") is not None:
        import capo_ecs.types.network_interfaces

        out["network_interfaces"] = (
            capo_ecs.types.network_interfaces.deserialize_aws_json_1_1(
                data["networkInterfaces"]
            )
        )
    if data.get("healthStatus") is not None:
        import capo_ecs.types.health_status

        out["health_status"] = capo_ecs.types.health_status.deserialize_aws_json_1_1(
            data["healthStatus"]
        )
    if data.get("managedAgents") is not None:
        import capo_ecs.types.managed_agents

        out["managed_agents"] = capo_ecs.types.managed_agents.deserialize_aws_json_1_1(
            data["managedAgents"]
        )
    if data.get("cpu") is not None:
        out["cpu"] = data["cpu"]
    if data.get("memory") is not None:
        out["memory"] = data["memory"]
    if data.get("memoryReservation") is not None:
        out["memory_reservation"] = data["memoryReservation"]
    if data.get("gpuIds") is not None:
        import capo_ecs.types.gpu_ids

        out["gpu_ids"] = capo_ecs.types.gpu_ids.deserialize_aws_json_1_1(data["gpuIds"])
    if data.get("neuronDeviceIds") is not None:
        import capo_ecs.types.neuron_device_ids

        out["neuron_device_ids"] = (
            capo_ecs.types.neuron_device_ids.deserialize_aws_json_1_1(
                data["neuronDeviceIds"]
            )
        )
    if data.get("gpuSharingStrategy") is not None:
        import capo_ecs.types.sharing_strategy

        out["gpu_sharing_strategy"] = (
            capo_ecs.types.sharing_strategy.deserialize_aws_json_1_1(
                data["gpuSharingStrategy"]
            )
        )
    return out
