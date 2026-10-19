"""Generated from Smithy shape ``com.amazonaws.omics#StartAnnotationImportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.resource_id


class StartAnnotationImportResponse(TypedDict, closed=True):
    job_id: "capo_omics.types.resource_id.ResourceId"
    """<p>The job's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAnnotationImportResponse) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> StartAnnotationImportResponse:
    out: StartAnnotationImportResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    return out
