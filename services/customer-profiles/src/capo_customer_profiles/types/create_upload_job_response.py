"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateUploadJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.uuid


class CreateUploadJobResponse(TypedDict, closed=True):
    job_id: "capo_customer_profiles.types.uuid.uuid"
    """<p>The unique identifier for the created upload job. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUploadJobResponse) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> CreateUploadJobResponse:
    out: CreateUploadJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    return out
