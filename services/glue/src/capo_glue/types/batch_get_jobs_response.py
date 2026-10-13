"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetJobsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.job_list
    import capo_glue.types.job_name_list


class BatchGetJobsResponse(TypedDict, closed=True):
    jobs: NotRequired["capo_glue.types.job_list.JobList"]
    """<p>A list of job definitions.</p>"""
    jobs_not_found: NotRequired["capo_glue.types.job_name_list.JobNameList"]
    """<p>A list of names of jobs not found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetJobsResponse) -> dict:
    out: dict = {}
    if "jobs" in value:
        import capo_glue.types.job_list

        out["Jobs"] = capo_glue.types.job_list.serialize_aws_json_1_1(value["jobs"])
    if "jobs_not_found" in value:
        import capo_glue.types.job_name_list

        out["JobsNotFound"] = capo_glue.types.job_name_list.serialize_aws_json_1_1(
            value["jobs_not_found"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetJobsResponse:
    out: BatchGetJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Jobs") is not None:
        import capo_glue.types.job_list

        out["jobs"] = capo_glue.types.job_list.deserialize_aws_json_1_1(data["Jobs"])
    if data.get("JobsNotFound") is not None:
        import capo_glue.types.job_name_list

        out["jobs_not_found"] = capo_glue.types.job_name_list.deserialize_aws_json_1_1(
            data["JobsNotFound"]
        )
    return out


def redact_sensitive(value: BatchGetJobsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "jobs" in value:
        import capo_glue.types.job_list

        out["jobs"] = capo_glue.types.job_list.redact_sensitive(value["jobs"])
    return out
