"""Generated from Smithy shape ``com.amazonaws.medicalimaging#ImageFrameInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.image_frame_id


class ImageFrameInformation(TypedDict, closed=True):
    image_frame_id: "capo_medical_imaging.types.image_frame_id.ImageFrameId"
    """<p>The image frame (pixel data) identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageFrameInformation) -> dict:
    out: dict = {}
    out["imageFrameId"] = value["image_frame_id"]
    return out


def deserialize_json(data: dict) -> ImageFrameInformation:
    out: ImageFrameInformation = {}  # type: ignore[typeddict-item]
    if data.get("imageFrameId") is not None:
        out["image_frame_id"] = data["imageFrameId"]
    else:
        out["image_frame_id"] = ""
    return out
