"""Generated from Smithy shape ``com.amazonaws.inspector#CreateExclusionsPreviewResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.uuid


class CreateExclusionsPreviewResponse(TypedDict, closed=True):
    preview_token: "capo_inspector.types.uuid.UUID"
    """<p>Specifies the unique identifier of the requested exclusions preview. You can use the unique identifier to retrieve the exclusions preview when running the GetExclusionsPreview API.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateExclusionsPreviewResponse) -> dict:
    out: dict = {}
    out["previewToken"] = value["preview_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateExclusionsPreviewResponse:
    out: CreateExclusionsPreviewResponse = {}  # type: ignore[typeddict-item]
    if data.get("previewToken") is not None:
        out["preview_token"] = data["previewToken"]
    else:
        out["preview_token"] = ""
    return out
