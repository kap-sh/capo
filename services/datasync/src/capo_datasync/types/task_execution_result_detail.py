"""Generated from Smithy shape ``com.amazonaws.datasync#TaskExecutionResultDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.duration
    import capo_datasync.types.phase_status
    import capo_datasync.types.string


class TaskExecutionResultDetail(TypedDict, closed=True):
    prepare_duration: NotRequired["capo_datasync.types.duration.Duration"]
    """<p>The time in milliseconds that your task execution was in the <code>PREPARING</code> step. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses">Task execution statuses</a>.</p> <p>For Enhanced mode tasks, the value is always <code>0</code>. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/how-datasync-transfer-works.html#how-datasync-prepares">How DataSync prepares your data transfer</a>.</p>"""
    prepare_status: NotRequired["capo_datasync.types.phase_status.PhaseStatus"]
    """<p>The status of the <code>PREPARING</code> step for your task execution. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses">Task execution statuses</a>.</p>"""
    total_duration: NotRequired["capo_datasync.types.duration.Duration"]
    """<p>The time in milliseconds that your task execution ran.</p>"""
    transfer_duration: NotRequired["capo_datasync.types.duration.Duration"]
    """<p>The time in milliseconds that your task execution was in the <code>TRANSFERRING</code> step. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses">Task execution statuses</a>.</p> <p>For Enhanced mode tasks, the value is always <code>0</code>. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/how-datasync-transfer-works.html#how-datasync-transfers">How DataSync transfers your data</a>.</p>"""
    transfer_status: NotRequired["capo_datasync.types.phase_status.PhaseStatus"]
    """<p>The status of the <code>TRANSFERRING</code> step for your task execution. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses">Task execution statuses</a>.</p>"""
    verify_duration: NotRequired["capo_datasync.types.duration.Duration"]
    """<p>The time in milliseconds that your task execution was in the <code>VERIFYING</code> step. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses">Task execution statuses</a>.</p> <p>For Enhanced mode tasks, the value is always <code>0</code>. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/how-datasync-transfer-works.html#how-verifying-works">How DataSync verifies your data's integrity</a>.</p>"""
    verify_status: NotRequired["capo_datasync.types.phase_status.PhaseStatus"]
    """<p>The status of the <code>VERIFYING</code> step for your task execution. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses">Task execution statuses</a>.</p>"""
    error_code: NotRequired["capo_datasync.types.string.string"]
    """<p>An error that DataSync encountered during your task execution. You can use this information to help <a href="https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-locations-tasks.html">troubleshoot issues</a>.</p>"""
    error_detail: NotRequired["capo_datasync.types.string.string"]
    """<p>The detailed description of an error that DataSync encountered during your task execution. You can use this information to help <a href="https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-locations-tasks.html">troubleshoot issues</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskExecutionResultDetail) -> dict:
    out: dict = {}
    if "prepare_duration" in value:
        out["PrepareDuration"] = value["prepare_duration"]
    if "prepare_status" in value:
        import capo_datasync.types.phase_status

        out["PrepareStatus"] = capo_datasync.types.phase_status.serialize_aws_json_1_1(
            value["prepare_status"]
        )
    if "total_duration" in value:
        out["TotalDuration"] = value["total_duration"]
    if "transfer_duration" in value:
        out["TransferDuration"] = value["transfer_duration"]
    if "transfer_status" in value:
        import capo_datasync.types.phase_status

        out["TransferStatus"] = capo_datasync.types.phase_status.serialize_aws_json_1_1(
            value["transfer_status"]
        )
    if "verify_duration" in value:
        out["VerifyDuration"] = value["verify_duration"]
    if "verify_status" in value:
        import capo_datasync.types.phase_status

        out["VerifyStatus"] = capo_datasync.types.phase_status.serialize_aws_json_1_1(
            value["verify_status"]
        )
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_detail" in value:
        out["ErrorDetail"] = value["error_detail"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskExecutionResultDetail:
    out: TaskExecutionResultDetail = {}  # type: ignore[typeddict-item]
    if data.get("PrepareDuration") is not None:
        out["prepare_duration"] = data["PrepareDuration"]
    if data.get("PrepareStatus") is not None:
        import capo_datasync.types.phase_status

        out["prepare_status"] = (
            capo_datasync.types.phase_status.deserialize_aws_json_1_1(
                data["PrepareStatus"]
            )
        )
    if data.get("TotalDuration") is not None:
        out["total_duration"] = data["TotalDuration"]
    if data.get("TransferDuration") is not None:
        out["transfer_duration"] = data["TransferDuration"]
    if data.get("TransferStatus") is not None:
        import capo_datasync.types.phase_status

        out["transfer_status"] = (
            capo_datasync.types.phase_status.deserialize_aws_json_1_1(
                data["TransferStatus"]
            )
        )
    if data.get("VerifyDuration") is not None:
        out["verify_duration"] = data["VerifyDuration"]
    if data.get("VerifyStatus") is not None:
        import capo_datasync.types.phase_status

        out["verify_status"] = (
            capo_datasync.types.phase_status.deserialize_aws_json_1_1(
                data["VerifyStatus"]
            )
        )
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorDetail") is not None:
        out["error_detail"] = data["ErrorDetail"]
    return out
