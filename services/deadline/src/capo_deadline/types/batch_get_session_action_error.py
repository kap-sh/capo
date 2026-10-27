"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionActionError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_session_action_error_code
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_id
    import capo_deadline.types.queue_id
    import capo_deadline.types.session_action_id
    import capo_deadline.types.string


class BatchGetSessionActionError(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the session action that could not be retrieved."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID of the session action that could not be retrieved."""
    job_id: "capo_deadline.types.job_id.JobId"
    """The job ID of the session action that could not be retrieved."""
    session_action_id: "capo_deadline.types.session_action_id.SessionActionId"
    """The session action ID of the session action that could not be retrieved."""
    code: "capo_deadline.types.batch_get_session_action_error_code.BatchGetSessionActionErrorCode"
    """The error code."""
    message: "capo_deadline.types.string.String"
    """The error message."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSessionActionError) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
    out["sessionActionId"] = value["session_action_id"]
    import capo_deadline.types.batch_get_session_action_error_code

    out["code"] = (
        capo_deadline.types.batch_get_session_action_error_code.serialize_json(
            value["code"]
        )
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchGetSessionActionError:
    out: BatchGetSessionActionError = {}  # type: ignore[typeddict-item]
    if data.get("farmId") is not None:
        out["farm_id"] = data["farmId"]
    else:
        out["farm_id"] = ""
    if data.get("queueId") is not None:
        out["queue_id"] = data["queueId"]
    else:
        out["queue_id"] = ""
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("sessionActionId") is not None:
        out["session_action_id"] = data["sessionActionId"]
    else:
        out["session_action_id"] = ""
    if data.get("code") is not None:
        import capo_deadline.types.batch_get_session_action_error_code

        out["code"] = (
            capo_deadline.types.batch_get_session_action_error_code.deserialize_json(
                data["code"]
            )
        )
    else:
        import typing

        out["code"] = typing.cast(
            "capo_deadline.types.batch_get_session_action_error_code.BatchGetSessionActionErrorCode",
            "",
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
