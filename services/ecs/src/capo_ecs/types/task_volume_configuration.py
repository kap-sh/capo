"""Generated from Smithy shape ``com.amazonaws.ecs#TaskVolumeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.ecs_volume_name
    import capo_ecs.types.task_managed_ebs_volume_configuration


class TaskVolumeConfiguration(TypedDict, closed=True):
    name: "capo_ecs.types.ecs_volume_name.ECSVolumeName"
    """<p>The name of the volume. This value must match the volume name from the <code>Volume</code> object in the task definition.</p>"""
    managed_ebs_volume: NotRequired[
        "capo_ecs.types.task_managed_ebs_volume_configuration.TaskManagedEBSVolumeConfiguration"
    ]
    """<p>The configuration for the Amazon EBS volume that Amazon ECS creates and manages on your behalf. These settings are used to create each Amazon EBS volume, with one volume created for each task. The Amazon EBS volumes are visible in your account in the Amazon EC2 console once they are created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskVolumeConfiguration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "managed_ebs_volume" in value:
        import capo_ecs.types.task_managed_ebs_volume_configuration

        out["managedEBSVolume"] = (
            capo_ecs.types.task_managed_ebs_volume_configuration.serialize_aws_json_1_1(
                value["managed_ebs_volume"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskVolumeConfiguration:
    out: TaskVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("managedEBSVolume") is not None:
        import capo_ecs.types.task_managed_ebs_volume_configuration

        out["managed_ebs_volume"] = (
            capo_ecs.types.task_managed_ebs_volume_configuration.deserialize_aws_json_1_1(
                data["managedEBSVolume"]
            )
        )
    return out
