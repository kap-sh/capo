"""Generated from Smithy shape ``com.amazonaws.endusermessaging#JobResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.job_id
    import capo_endusermessaging.types.job_resource_identifier


class JobResult(TypedDict, closed=True):
    job_id: "capo_endusermessaging.types.job_id.JobId"
    """<p>The unique identifier of the asynchronous job. Use the GetJob operation to check the status of the job and to retrieve its results.</p>"""
    resource_identifier: (
        "capo_endusermessaging.types.job_resource_identifier.JobResourceIdentifier"
    )
    """<p>The identifier from your request that this job is processing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobResult) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["resourceIdentifier"] = value["resource_identifier"]
    return out


def deserialize_json(data: dict) -> JobResult:
    out: JobResult = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("JobResult.job_id required")
    if data.get("resourceIdentifier") is not None:
        out["resource_identifier"] = data["resourceIdentifier"]
    else:
        raise DeserializationError("JobResult.resource_identifier required")
    return out
