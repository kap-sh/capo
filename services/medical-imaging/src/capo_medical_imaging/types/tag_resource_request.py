"""Generated from Smithy shape ``com.amazonaws.medicalimaging#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.arn
    import capo_medical_imaging.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_medical_imaging.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the medical imaging resource that tags are being added to.</p>"""
    tags: "capo_medical_imaging.types.tag_map.TagMap"
    """<p>The user-specified key and value tag pairs added to a medical imaging resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_medical_imaging.types.tag_map

    out["tags"] = capo_medical_imaging.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_medical_imaging.types.tag_map

        out["tags"] = capo_medical_imaging.types.tag_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
