"""Generated from Smithy shape ``com.amazonaws.ecs#TaskManagedEBSVolumeTerminationPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_boolean


class TaskManagedEBSVolumeTerminationPolicy(TypedDict, closed=True):
    delete_on_termination: "capo_ecs.types.boxed_boolean.BoxedBoolean"
    """<p>Indicates whether the volume should be deleted on when the task stops. If a value of <code>true</code> is specified, Amazon ECS deletes the Amazon EBS volume on your behalf when the task goes into the <code>STOPPED</code> state. If no value is specified, the default value is <code>true</code> is used. When set to <code>false</code>, Amazon ECS leaves the volume in your account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskManagedEBSVolumeTerminationPolicy) -> dict:
    out: dict = {}
    out["deleteOnTermination"] = value["delete_on_termination"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskManagedEBSVolumeTerminationPolicy:
    out: TaskManagedEBSVolumeTerminationPolicy = {}  # type: ignore[typeddict-item]
    if data.get("deleteOnTermination") is not None:
        out["delete_on_termination"] = data["deleteOnTermination"]
    else:
        out["delete_on_termination"] = False
    return out
