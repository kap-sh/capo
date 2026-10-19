"""Generated from Smithy shape ``com.amazonaws.panorama#CreateNodeFromTemplateJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.job_id


class CreateNodeFromTemplateJobResponse(TypedDict, closed=True):
    job_id: "capo_panorama.types.job_id.JobId"
    """<p>The job's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNodeFromTemplateJobResponse) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> CreateNodeFromTemplateJobResponse:
    out: CreateNodeFromTemplateJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    return out
