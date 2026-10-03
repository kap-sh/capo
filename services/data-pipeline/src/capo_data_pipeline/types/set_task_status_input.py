"""Generated from Smithy shape ``com.amazonaws.datapipeline#SetTaskStatusInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_data_pipeline.types.error_message
    import capo_data_pipeline.types.string
    import capo_data_pipeline.types.task_id
    import capo_data_pipeline.types.task_status


class SetTaskStatusInput(TypedDict, closed=True):
    task_id: "capo_data_pipeline.types.task_id.taskId"
    """<p>The ID of the task assigned to the task runner. This value is provided in the response for <a>PollForTask</a>.</p>"""
    task_status: "capo_data_pipeline.types.task_status.TaskStatus"
    """<p>If <code>FINISHED</code>, the task successfully completed. If <code>FAILED</code>, the task ended unsuccessfully. Preconditions use false.</p>"""
    error_id: NotRequired["capo_data_pipeline.types.string.string"]
    """<p>If an error occurred during the task, this value specifies the error code. This value is set on the physical attempt object. It is used to display error information to the user. It should not start with string "Service_" which is reserved by the system.</p>"""
    error_message: NotRequired["capo_data_pipeline.types.error_message.errorMessage"]
    """<p>If an error occurred during the task, this value specifies a text description of the error. This value is set on the physical attempt object. It is used to display error information to the user. The web service does not parse this value.</p>"""
    error_stack_trace: NotRequired["capo_data_pipeline.types.string.string"]
    """<p>If an error occurred during the task, this value specifies the stack trace associated with the error. This value is set on the physical attempt object. It is used to display error information to the user. The web service does not parse this value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetTaskStatusInput) -> dict:
    out: dict = {}
    out["taskId"] = value["task_id"]
    import capo_data_pipeline.types.task_status

    out["taskStatus"] = capo_data_pipeline.types.task_status.serialize_aws_json_1_1(
        value["task_status"]
    )
    if "error_id" in value:
        out["errorId"] = value["error_id"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "error_stack_trace" in value:
        out["errorStackTrace"] = value["error_stack_trace"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SetTaskStatusInput:
    out: SetTaskStatusInput = {}  # type: ignore[typeddict-item]
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("SetTaskStatusInput.task_id required")
    if data.get("taskStatus") is not None:
        import capo_data_pipeline.types.task_status

        out["task_status"] = (
            capo_data_pipeline.types.task_status.deserialize_aws_json_1_1(
                data["taskStatus"]
            )
        )
    else:
        raise DeserializationError("SetTaskStatusInput.task_status required")
    if data.get("errorId") is not None:
        out["error_id"] = data["errorId"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    if data.get("errorStackTrace") is not None:
        out["error_stack_trace"] = data["errorStackTrace"]
    return out
