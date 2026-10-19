"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#CreateAccessPreviewResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.access_preview_id


class CreateAccessPreviewResponse(TypedDict, closed=True):
    id: "capo_accessanalyzer.types.access_preview_id.AccessPreviewId"
    """<p>The unique ID for the access preview.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccessPreviewResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CreateAccessPreviewResponse:
    out: CreateAccessPreviewResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
