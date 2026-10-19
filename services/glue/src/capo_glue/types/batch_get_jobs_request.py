"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.job_name_list


class BatchGetJobsRequest(TypedDict, closed=True):
    job_names: "capo_glue.types.job_name_list.JobNameList"
    """<p>A list of job names, which might be the names returned from the <code>ListJobs</code> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetJobsRequest) -> dict:
    out: dict = {}
    import capo_glue.types.job_name_list

    out["JobNames"] = capo_glue.types.job_name_list.serialize_aws_json_1_1(
        value["job_names"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetJobsRequest:
    out: BatchGetJobsRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobNames") is not None:
        import capo_glue.types.job_name_list

        out["job_names"] = capo_glue.types.job_name_list.deserialize_aws_json_1_1(
            data["JobNames"]
        )
    else:
        out["job_names"] = []
    return out
