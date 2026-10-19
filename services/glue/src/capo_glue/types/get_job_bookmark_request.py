"""Generated from Smithy shape ``com.amazonaws.glue#GetJobBookmarkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.job_name
    import capo_glue.types.run_id


class GetJobBookmarkRequest(TypedDict, closed=True):
    job_name: "capo_glue.types.job_name.JobName"
    """<p>The name of the job in question.</p>"""
    run_id: NotRequired["capo_glue.types.run_id.RunId"]
    """<p>The unique run identifier associated with this job run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetJobBookmarkRequest) -> dict:
    out: dict = {}
    out["JobName"] = value["job_name"]
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetJobBookmarkRequest:
    out: GetJobBookmarkRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    else:
        out["job_name"] = ""
    if data.get("RunId") is not None:
        out["run_id"] = data["RunId"]
    return out
