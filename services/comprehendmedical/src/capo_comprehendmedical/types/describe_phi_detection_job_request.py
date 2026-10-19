"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#DescribePHIDetectionJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.job_id


class DescribePHIDetectionJobRequest(TypedDict, closed=True):
    job_id: "capo_comprehendmedical.types.job_id.JobId"
    """<p>The identifier that Amazon Comprehend Medical generated for the job. The <code>StartPHIDetectionJob</code> operation returns this identifier in its response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePHIDetectionJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePHIDetectionJobRequest:
    out: DescribePHIDetectionJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    return out
