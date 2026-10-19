"""Generated from Smithy shape ``com.amazonaws.glue#GetJobRunsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.generic_string
    import capo_glue.types.name_string
    import capo_glue.types.orchestration_page_size200


class GetJobRunsRequest(TypedDict, closed=True):
    job_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the job definition for which to retrieve all job runs.</p>"""
    next_token: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>A continuation token, if this is a continuation call.</p>"""
    max_results: NotRequired[
        "capo_glue.types.orchestration_page_size200.OrchestrationPageSize200"
    ]
    """<p>The maximum size of the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetJobRunsRequest) -> dict:
    out: dict = {}
    out["JobName"] = value["job_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetJobRunsRequest:
    out: GetJobRunsRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    else:
        out["job_name"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
