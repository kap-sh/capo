"""Generated from Smithy shape ``com.amazonaws.drs#DeleteJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.job_id


class DeleteJobRequest(TypedDict, closed=True):
    job_id: "capo_drs.types.job_id.JobID"
    """<p>The ID of the Job to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteJobRequest) -> dict:
    out: dict = {}
    out["jobID"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> DeleteJobRequest:
    out: DeleteJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobID") is not None:
        out["job_id"] = data["jobID"]
    else:
        out["job_id"] = ""
    return out
