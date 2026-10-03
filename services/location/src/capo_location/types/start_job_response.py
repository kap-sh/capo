"""Generated from Smithy shape ``com.amazonaws.location#StartJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.geo_arn
    import capo_location.types.job_id
    import capo_location.types.job_status
    import capo_location.types.timestamp


class StartJobResponse(TypedDict, closed=True):
    created_at: "capo_location.types.timestamp.Timestamp"
    """<p>Job creation time in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sss</code>.</p>"""
    job_arn: "capo_location.types.geo_arn.GeoArn"
    """<p>The Amazon Resource Name (ARN) for the job resource. Used when you need to specify a resource across all Amazon Web Services.</p> <p>Format example: <code>arn:aws:geo:region:account-id:job/ExampleJob</code> </p>"""
    job_id: "capo_location.types.job_id.JobId"
    """<p>Unique job identifier.</p>"""
    status: "capo_location.types.job_status.JobStatus"
    """<p>Initial job status (always "Pending" for new jobs).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartJobResponse) -> dict:
    out: dict = {}
    import capo_location.types.timestamp

    out["CreatedAt"] = capo_location.types.timestamp.serialize_json(value["created_at"])
    out["JobArn"] = value["job_arn"]
    out["JobId"] = value["job_id"]
    out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> StartJobResponse:
    out: StartJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("CreatedAt") is not None:
        import capo_location.types.timestamp

        out["created_at"] = capo_location.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("StartJobResponse.created_at required")
    if data.get("JobArn") is not None:
        out["job_arn"] = data["JobArn"]
    else:
        raise DeserializationError("StartJobResponse.job_arn required")
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("StartJobResponse.job_id required")
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("StartJobResponse.status required")
    return out
