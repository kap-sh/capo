"""Generated from Smithy shape ``com.amazonaws.glue#GetSystemLogsForJobRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.id_string
    import capo_glue.types.name_string


class GetSystemLogsForJobRunRequest(TypedDict, closed=True):
    job_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the job.</p>"""
    run_id: "capo_glue.types.id_string.IdString"
    """<p>The ID of the job run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSystemLogsForJobRunRequest) -> dict:
    out: dict = {}
    out["JobName"] = value["job_name"]
    out["RunId"] = value["run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSystemLogsForJobRunRequest:
    out: GetSystemLogsForJobRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    else:
        raise DeserializationError("GetSystemLogsForJobRunRequest.job_name required")
    if data.get("RunId") is not None:
        out["run_id"] = data["RunId"]
    else:
        raise DeserializationError("GetSystemLogsForJobRunRequest.run_id required")
    return out
