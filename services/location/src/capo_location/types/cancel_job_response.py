"""Generated from Smithy shape ``com.amazonaws.location#CancelJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_location.types.geo_arn
    import capo_location.types.job_id
    import capo_location.types.job_status


class CancelJobResponse(TypedDict, closed=True):
    job_arn: "capo_location.types.geo_arn.GeoArn"
    """<p>Amazon Resource Name (ARN) of the cancelled job.</p>"""
    job_id: "capo_location.types.job_id.JobId"
    """<p>Unique job identifier.</p>"""
    status: "capo_location.types.job_status.JobStatus"
    """<p>Job status after cancellation request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelJobResponse) -> dict:
    out: dict = {}
    out["JobArn"] = value["job_arn"]
    out["JobId"] = value["job_id"]
    out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> CancelJobResponse:
    out: CancelJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobArn") is not None:
        out["job_arn"] = data["JobArn"]
    else:
        out["job_arn"] = ""
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    return out
