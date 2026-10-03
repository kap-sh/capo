"""Generated from Smithy shape ``com.amazonaws.ecs#TaskOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.container_overrides
    import capo_ecs.types.ephemeral_storage
    import capo_ecs.types.inference_accelerator_overrides
    import capo_ecs.types.string


class TaskOverride(TypedDict, closed=True):
    container_overrides: NotRequired[
        "capo_ecs.types.container_overrides.ContainerOverrides"
    ]
    """<p>One or more container overrides that are sent to a task.</p>"""
    cpu: NotRequired["capo_ecs.types.string.String"]
    """<p>The CPU override for the task.</p>"""
    inference_accelerator_overrides: NotRequired[
        "capo_ecs.types.inference_accelerator_overrides.InferenceAcceleratorOverrides"
    ]
    """<p>The Elastic Inference accelerator override for the task.</p>"""
    execution_role_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the task execution role override for the task. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html">Amazon ECS task execution IAM role</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    memory: NotRequired["capo_ecs.types.string.String"]
    """<p>The memory override for the task.</p>"""
    task_role_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html">IAM Role for Tasks</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    ephemeral_storage: NotRequired["capo_ecs.types.ephemeral_storage.EphemeralStorage"]
    """<p>The ephemeral storage setting override for the task.</p> <note> <p>This parameter is only supported for tasks hosted on Fargate that use the following platform versions:</p> <ul> <li> <p>Linux platform version <code>1.4.0</code> or later.</p> </li> <li> <p>Windows platform version <code>1.0.0</code> or later.</p> </li> </ul> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskOverride) -> dict:
    out: dict = {}
    if "container_overrides" in value:
        import capo_ecs.types.container_overrides

        out["containerOverrides"] = (
            capo_ecs.types.container_overrides.serialize_aws_json_1_1(
                value["container_overrides"]
            )
        )
    if "cpu" in value:
        out["cpu"] = value["cpu"]
    if "inference_accelerator_overrides" in value:
        import capo_ecs.types.inference_accelerator_overrides

        out["inferenceAcceleratorOverrides"] = (
            capo_ecs.types.inference_accelerator_overrides.serialize_aws_json_1_1(
                value["inference_accelerator_overrides"]
            )
        )
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    if "memory" in value:
        out["memory"] = value["memory"]
    if "task_role_arn" in value:
        out["taskRoleArn"] = value["task_role_arn"]
    if "ephemeral_storage" in value:
        import capo_ecs.types.ephemeral_storage

        out["ephemeralStorage"] = (
            capo_ecs.types.ephemeral_storage.serialize_aws_json_1_1(
                value["ephemeral_storage"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskOverride:
    out: TaskOverride = {}  # type: ignore[typeddict-item]
    if data.get("containerOverrides") is not None:
        import capo_ecs.types.container_overrides

        out["container_overrides"] = (
            capo_ecs.types.container_overrides.deserialize_aws_json_1_1(
                data["containerOverrides"]
            )
        )
    if data.get("cpu") is not None:
        out["cpu"] = data["cpu"]
    if data.get("inferenceAcceleratorOverrides") is not None:
        import capo_ecs.types.inference_accelerator_overrides

        out["inference_accelerator_overrides"] = (
            capo_ecs.types.inference_accelerator_overrides.deserialize_aws_json_1_1(
                data["inferenceAcceleratorOverrides"]
            )
        )
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    if data.get("memory") is not None:
        out["memory"] = data["memory"]
    if data.get("taskRoleArn") is not None:
        out["task_role_arn"] = data["taskRoleArn"]
    if data.get("ephemeralStorage") is not None:
        import capo_ecs.types.ephemeral_storage

        out["ephemeral_storage"] = (
            capo_ecs.types.ephemeral_storage.deserialize_aws_json_1_1(
                data["ephemeralStorage"]
            )
        )
    return out
