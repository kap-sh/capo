"""Generated from Smithy shape ``com.amazonaws.pipes#EcsResourceRequirement``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.ecs_resource_requirement_type
    import capo_pipes.types.string


class EcsResourceRequirement(TypedDict, closed=True):
    type: "capo_pipes.types.ecs_resource_requirement_type.EcsResourceRequirementType"
    """<p>The type of resource to assign to a container. The supported values are <code>GPU</code> or <code>InferenceAccelerator</code>.</p>"""
    value: "capo_pipes.types.string.String"
    """<p>The value for the specified resource type.</p> <p>If the <code>GPU</code> type is used, the value is the number of physical <code>GPUs</code> the Amazon ECS container agent reserves for the container. The number of GPUs that's reserved for all containers in a task can't exceed the number of available GPUs on the container instance that the task is launched on.</p> <p>If the <code>InferenceAccelerator</code> type is used, the <code>value</code> matches the <code>deviceName</code> for an InferenceAccelerator specified in a task definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcsResourceRequirement) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> EcsResourceRequirement:
    out: EcsResourceRequirement = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
