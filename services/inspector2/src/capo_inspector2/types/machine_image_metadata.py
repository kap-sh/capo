"""Generated from Smithy shape ``com.amazonaws.inspector2#MachineImageMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.machine_image_platform
    import capo_inspector2.types.tag_map


class MachineImageMetadata(TypedDict, closed=True):
    tags: NotRequired["capo_inspector2.types.tag_map.TagMap"]
    """<p>The tags associated with the machine image.</p>"""
    platform: NotRequired[
        "capo_inspector2.types.machine_image_platform.MachineImagePlatform"
    ]
    """<p>The platform of the machine image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MachineImageMetadata) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_inspector2.types.tag_map

        out["tags"] = capo_inspector2.types.tag_map.serialize_json(value["tags"])
    if "platform" in value:
        out["platform"] = value["platform"]
    return out


def deserialize_json(data: dict) -> MachineImageMetadata:
    out: MachineImageMetadata = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_inspector2.types.tag_map

        out["tags"] = capo_inspector2.types.tag_map.deserialize_json(data["tags"])
    if data.get("platform") is not None:
        out["platform"] = data["platform"]
    return out
