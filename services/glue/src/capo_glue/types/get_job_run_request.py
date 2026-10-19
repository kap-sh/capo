"""Generated from Smithy shape ``com.amazonaws.glue#GetJobRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.boolean_value
    import capo_glue.types.id_string
    import capo_glue.types.name_string


class GetJobRunRequest(TypedDict, closed=True):
    job_name: "capo_glue.types.name_string.NameString"
    """<p>Name of the job definition being run.</p>"""
    run_id: "capo_glue.types.id_string.IdString"
    """<p>The ID of the job run.</p>"""
    predecessors_included: NotRequired["capo_glue.types.boolean_value.BooleanValue"]
    """<p>True if a list of predecessor runs should be returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetJobRunRequest) -> dict:
    out: dict = {}
    out["JobName"] = value["job_name"]
    out["RunId"] = value["run_id"]
    if "predecessors_included" in value:
        out["PredecessorsIncluded"] = value["predecessors_included"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetJobRunRequest:
    out: GetJobRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    else:
        raise DeserializationError("GetJobRunRequest.job_name required")
    if data.get("RunId") is not None:
        out["run_id"] = data["RunId"]
    else:
        raise DeserializationError("GetJobRunRequest.run_id required")
    if data.get("PredecessorsIncluded") is not None:
        out["predecessors_included"] = data["PredecessorsIncluded"]
    return out
