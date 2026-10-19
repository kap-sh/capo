"""Generated from Smithy shape ``com.amazonaws.braket#CancelJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_braket.types.cancellation_status
    import capo_braket.types.job_arn


class CancelJobResponse(TypedDict, closed=True):
    job_arn: "capo_braket.types.job_arn.JobArn"
    """<p>The ARN of the Amazon Braket job.</p>"""
    cancellation_status: "capo_braket.types.cancellation_status.CancellationStatus"
    """<p>The status of the hybrid job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelJobResponse) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    out["cancellationStatus"] = value["cancellation_status"]
    return out


def deserialize_json(data: dict) -> CancelJobResponse:
    out: CancelJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    else:
        out["job_arn"] = ""
    if data.get("cancellationStatus") is not None:
        out["cancellation_status"] = data["cancellationStatus"]
    else:
        out["cancellation_status"] = ""
    return out
