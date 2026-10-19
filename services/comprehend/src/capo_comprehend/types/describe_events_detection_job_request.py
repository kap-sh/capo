"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeEventsDetectionJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.job_id


class DescribeEventsDetectionJobRequest(TypedDict, closed=True):
    job_id: "capo_comprehend.types.job_id.JobId"
    """<p>The identifier of the events detection job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventsDetectionJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventsDetectionJobRequest:
    out: DescribeEventsDetectionJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    return out
