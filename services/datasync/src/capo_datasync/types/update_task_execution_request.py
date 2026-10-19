"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateTaskExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.options
    import capo_datasync.types.task_execution_arn


class UpdateTaskExecutionRequest(TypedDict, closed=True):
    task_execution_arn: "capo_datasync.types.task_execution_arn.TaskExecutionArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the task execution that you're updating.</p>"""
    options: "capo_datasync.types.options.Options"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTaskExecutionRequest) -> dict:
    out: dict = {}
    out["TaskExecutionArn"] = value["task_execution_arn"]
    import capo_datasync.types.options

    out["Options"] = capo_datasync.types.options.serialize_aws_json_1_1(
        value["options"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTaskExecutionRequest:
    out: UpdateTaskExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("TaskExecutionArn") is not None:
        out["task_execution_arn"] = data["TaskExecutionArn"]
    else:
        out["task_execution_arn"] = ""
    if data.get("Options") is not None:
        import capo_datasync.types.options

        out["options"] = capo_datasync.types.options.deserialize_aws_json_1_1(
            data["Options"]
        )
    else:
        raise DeserializationError("UpdateTaskExecutionRequest.options required")
    return out
