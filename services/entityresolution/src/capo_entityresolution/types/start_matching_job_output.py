"""Generated from Smithy shape ``com.amazonaws.entityresolution#StartMatchingJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.job_id


class StartMatchingJobOutput(TypedDict, closed=True):
    job_id: "capo_entityresolution.types.job_id.JobId"
    """<p>The ID of the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMatchingJobOutput) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> StartMatchingJobOutput:
    out: StartMatchingJobOutput = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    return out
