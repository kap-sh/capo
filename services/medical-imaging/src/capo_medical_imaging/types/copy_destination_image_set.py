"""Generated from Smithy shape ``com.amazonaws.medicalimaging#CopyDestinationImageSet``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.image_set_external_version_id
    import capo_medical_imaging.types.image_set_id


class CopyDestinationImageSet(TypedDict, closed=True):
    image_set_id: "capo_medical_imaging.types.image_set_id.ImageSetId"
    """<p>The image set identifier for the destination image set.</p>"""
    latest_version_id: "capo_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId"
    """<p>The latest version identifier for the destination image set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CopyDestinationImageSet) -> dict:
    out: dict = {}
    out["imageSetId"] = value["image_set_id"]
    out["latestVersionId"] = value["latest_version_id"]
    return out


def deserialize_json(data: dict) -> CopyDestinationImageSet:
    out: CopyDestinationImageSet = {}  # type: ignore[typeddict-item]
    if data.get("imageSetId") is not None:
        out["image_set_id"] = data["imageSetId"]
    else:
        out["image_set_id"] = ""
    if data.get("latestVersionId") is not None:
        out["latest_version_id"] = data["latestVersionId"]
    else:
        out["latest_version_id"] = ""
    return out
