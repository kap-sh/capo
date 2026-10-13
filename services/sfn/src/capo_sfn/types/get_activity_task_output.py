"""Generated from Smithy shape ``com.amazonaws.sfn#GetActivityTaskOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.sensitive_data_job_input
    import capo_sfn.types.task_token


class GetActivityTaskOutput(TypedDict, closed=True):
    task_token: NotRequired["capo_sfn.types.task_token.TaskToken"]
    """<p>A token that identifies the scheduled task. This token must be copied and included in subsequent calls to <a>SendTaskHeartbeat</a>, <a>SendTaskSuccess</a> or <a>SendTaskFailure</a> in order to report the progress or completion of the task.</p>"""
    input: NotRequired["capo_sfn.types.sensitive_data_job_input.SensitiveDataJobInput"]
    """<p>The string that contains the JSON input data for the task. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetActivityTaskOutput) -> dict:
    out: dict = {}
    if "task_token" in value:
        out["taskToken"] = value["task_token"]
    if "input" in value:
        out["input"] = value["input"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetActivityTaskOutput:
    out: GetActivityTaskOutput = {}  # type: ignore[typeddict-item]
    if data.get("taskToken") is not None:
        out["task_token"] = data["taskToken"]
    if data.get("input") is not None:
        out["input"] = data["input"]
    return out


def redact_sensitive(value: GetActivityTaskOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input" in value:
        out["input"] = "*** Sensitive Data Redacted ***"
    return out
