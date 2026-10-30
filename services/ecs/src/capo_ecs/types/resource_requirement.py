"""Generated from Smithy shape ``com.amazonaws.ecs#ResourceRequirement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.resource_type
    import capo_ecs.types.sharing_strategy
    import capo_ecs.types.string


class ResourceRequirement(TypedDict, closed=True):
    value: "capo_ecs.types.string.String"
    """<p>The value for the specified resource type.</p> <p>You must specify this parameter unless the type is <code>GPU</code> and you specify <code>sharingStrategy</code>.</p> <p>When the type is <code>GPU</code>, the value is the number of physical <code>GPUs</code> the Amazon ECS container agent reserves for the container. The number of GPUs that's reserved for all containers in a task can't exceed the number of available GPUs on the container instance that the task is launched on. You can also specify <code>ALL</code> to allocate all available GPUs on the instance to the container.</p> <p>When the type is <code>NeuronDevice</code>, the value must be <code>ALL</code>. This allocates all available Neuron devices on the instance to the container. Only one container in a task can specify <code>NeuronDevice</code> resources. This resource type is only supported on Managed Instances.</p> <p>When the type is <code>InferenceAccelerator</code>, the <code>value</code> matches the <code>deviceName</code> for an <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_InferenceAccelerator.html">InferenceAccelerator</a> specified in a task definition.</p>"""
    type: "capo_ecs.types.resource_type.ResourceType"
    """<p>The type of resource to assign to a container. </p>"""
    sharing_strategy: NotRequired["capo_ecs.types.sharing_strategy.SharingStrategy"]
    """<p>The strategy that the container uses to share a GPU with other containers. Specify a sharing strategy only when the type is <code>GPU</code>. For a GPU resource requirement, specify either <code>value</code> or <code>sharingStrategy</code>, but not both. If you don't specify a sharing strategy, the container has exclusive use of each GPU that Amazon ECS assigns to it. The containers in a task that request GPUs must all use the same option.</p> <p>You can use GPU sharing with tasks that run on Amazon EC2 instances or Amazon ECS Managed Instances. Task definitions that require <code>EXTERNAL</code> compatibility don't support GPU sharing.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceRequirement) -> dict:
    out: dict = {}
    out["value"] = value.get("value", "")
    import capo_ecs.types.resource_type

    out["type"] = capo_ecs.types.resource_type.serialize_aws_json_1_1(value["type"])
    if "sharing_strategy" in value:
        import capo_ecs.types.sharing_strategy

        out["sharingStrategy"] = capo_ecs.types.sharing_strategy.serialize_aws_json_1_1(
            value["sharing_strategy"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceRequirement:
    out: ResourceRequirement = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    if data.get("type") is not None:
        import capo_ecs.types.resource_type

        out["type"] = capo_ecs.types.resource_type.deserialize_aws_json_1_1(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast("capo_ecs.types.resource_type.ResourceType", "")
    if data.get("sharingStrategy") is not None:
        import capo_ecs.types.sharing_strategy

        out["sharing_strategy"] = (
            capo_ecs.types.sharing_strategy.deserialize_aws_json_1_1(
                data["sharingStrategy"]
            )
        )
    return out
