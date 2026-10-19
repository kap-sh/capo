"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeSentimentDetectionJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.job_id


class DescribeSentimentDetectionJobRequest(TypedDict, closed=True):
    job_id: "capo_comprehend.types.job_id.JobId"
    """<p>The identifier that Amazon Comprehend generated for the job. The operation returns this identifier in its response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSentimentDetectionJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSentimentDetectionJobRequest:
    out: DescribeSentimentDetectionJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    return out
